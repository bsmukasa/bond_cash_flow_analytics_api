import numpy as np
from django.http import JsonResponse
from django.views.generic import View
from bond_analytics_project.cashflows.models import Bond


# Create your views here.
class BondValuationYield(View):
    model = Bond

    def post(self, request):
        request_dict = request.POST.dict()
        new_bond = self.model(
            name=request_dict['name'],
            coupon_payment_frequency=request_dict['coupon_payment_frequency'],
            face_value=request_dict['face_value'],
            maturity=request_dict['maturity'],
            coupon_rate=request_dict['coupon_rate'],
            yield_to_maturity_type=request_dict['yield_to_maturity_type'],
            bond_price=request_dict['bond_price']
        )

        new_bond.discount_rate_per_period = discount_rate_per_period(
            nper=request_dict['maturity'],
            pv=request_dict['bond_price'],
            fv=request_dict['face_value'],
            coupon=request_dict['coupon_rate']
        )

        new_bond.save()

        return JsonResponse({'status': 'PASS', 'message': 'Bond Saved'})
