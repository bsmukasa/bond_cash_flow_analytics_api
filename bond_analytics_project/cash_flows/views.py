import numpy as np
from django.http import JsonResponse
from django.views.generic import View
from bond_analytics_project.cash_flows.models import Bond


# Create your views here.
class BondValuation(View):
    model = Bond

    def post(self, request):
        """ Conducts bond valuation.

        Args:
            request: Request which must include the following:
                * name
                * coupon_payment_frequency
                * face_value
                * maturity
                * coupon_rate
                * yield_to_maturity_type

        Returns:
            JsonResponse dictionary with a status and message.
        """
        request_dict = request.POST.dict()
        new_bond = self.model(
            name=request_dict['name'],
            coupon_payment_frequency=request_dict['coupon_payment_frequency'],
            face_value=request_dict['face_value'],
            maturity=request_dict['maturity'],
            coupon_rate=request_dict['coupon_rate'],
            yield_to_maturity_type=request_dict['yield_to_maturity_type'],
        )

        periodic_coupon_payment = np.pmt(
            rate=request_dict['coupon_rate'] / 100 / 12,
            nper=request_dict['maturity'],
            pv=request_dict['bond_price'],
            fv=request_dict['face_value']
        )

        new_bond.discount_rate_per_period = np.rate(
            nper=request_dict['maturity'],
            pmt=periodic_coupon_payment,
            pv=request_dict['bond_price'],
            fv=request_dict['face_value'],
        )

        new_bond.yield_to_maturity = yield_to_maturity(
            yield_to_maturity_type=request_dict['yield_to_maturity_type'],
            period_discount_rate=period_discount_rate,
            coupon_payment_frequency=request_dict['coupon_payment_frequency']
        )

        new_bond.bond_price = np.pv(
            rate=period_discount_rate,
            nper=request_dict['maturity'],
            pmt=periodic_coupon_payment,
            fv=request_dict['face_value']
        )

        new_bond.save()

        return JsonResponse({'status': 'PASS', 'message': 'Bond Saved'})


# def discount_rate_per_period(nper, pv, fv, coupon):
#     """ Calculates the discount rate per period of a bond.
#
#     Using the numpy.pmt financial function the monthly payment against principal plus interest is determined.
#     Then the numpy.rate financial function is used to calculate the rate of interest per period.
#
#     Args:
#         nper: The number of payment periods in an annuity.
#         pv: The present value or current bond price.
#         fv: The future value or face value of the bond.
#         coupon: The stated annual interest rate.
#
#     Returns:
#         The discount rate per period as a float.
#     """
#     rate = coupon / 100 / 12
#     pmt = np.pmt(rate, nper, pv, fv)
#
#     return np.rate(nper, pmt, pv, fv)


def yield_to_maturity(yield_to_maturity_type, period_discount_rate, coupon_payment_frequency):
    """ Calculates the Yield to Maturity of the bond.

    When Yield to Maturity is calculated as the Annual Percentage Rate, it is simply the Discount Rate per
    Period multiply with the Coupon Payment Frequency. This is basically the discount rate per annum. When
    the Effective Annual Rate is required, the following formula is used:

        EXP(Coupon Payment Frequency*LN(Discount Rate per Period+1))-1
        *EXP – Exponent function*
        *LN – Natural Logarithm function*

    Args:
        yield_to_maturity_type: Whether the annual rate is the Annual Percentage Rate or the Effective Annual Rate.
        period_discount_rate: The discount rate per period of the bond.
        coupon_payment_frequency: Whether the coupon is paid annually or semi-annually.

    Returns:
        The yield to maturity as a float.
    """
    if yield_to_maturity_type == 1:
        return period_discount_rate * coupon_payment_frequency
    elif yield_to_maturity_type == 2:
        x = period_discount_rate + 1
        lan = np.log(x)
        y = coupon_payment_frequency * lan
        return np.exp(y) - 1
