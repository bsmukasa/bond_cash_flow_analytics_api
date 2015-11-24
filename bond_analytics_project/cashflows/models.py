from django.db import models


# Create your models here.
class Bond(models.Model):
    """A Django model class for Bond.

    A bond is a financial instrument issued by the government or corporations when they need to
    borrow money from the public on a long term basis to finance certain projects. Interest payments
    called coupons are typically paid out to bond holders on a regular basis while the entire loan
    amount called the Face or Par value is repaid at the end.

    Attributes:
        coupon_payment_frequency: Whether the coupon is paid annually or semi-annually.
        face_value: The principal of the bond to be repaid at the end of the maturity period.
        maturity: Number of periods to maturity is related to the Coupon Payment Frequency.
        coupon_rate: The stated annual interest rate payments for a Bond.
        yield_to_maturity_type: Whether the annual rate is the Annual Percentage Rate or the Effective Annual Rate.
        bond_price: The current price of the bond in the market.
        discount_rate_per_period: Yield to Maturity is typically quoted annually. This is the exact rate per period.
        yield_to_maturity: The interest rate received if a bond is held to the maturity date.

    Notes:
        The value must be an object which can be compared to all of the other values that will be
        in other nodes.
    """
    name = models.CharField(max_length=128)
    coupon_payment_frequency = models.CharField(max_length=100)
    face_value = models.DecimalField(max_digits=20, decimal_places=2)
    maturity = models.DecimalField(max_digits=20, decimal_places=4)
    coupon_rate = models.DecimalField(max_digits=5, decimal_places=4)
    yield_to_maturity_type = models.CharField(max_length=100)
    bond_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate_per_period = models.DecimalField(max_digits=10, decimal_places=4)
    yield_to_maturity = models.DecimalField(max_digits=5, decimal_places=4)
