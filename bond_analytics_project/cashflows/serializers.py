from rest_framework.serializers import ModelSerializer
from bond_analytics_project.cashflows.models import Bond


class BondSerializer(ModelSerializer):
    class Meta:
        model = Bond
        fields = (
            'name', 'coupon_payment_frequency',
            'face_value', 'maturity',
            'coupon_rate', 'bond_price',
            'yield_to_maturity_type', 'discount_rate_per_period',
            'yield_to_maturity'
        )
