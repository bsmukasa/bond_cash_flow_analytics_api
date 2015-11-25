from rest_framework.viewsets import ModelViewSet

from bond_analytics_project.cashflows.models import Bond
from bond_analytics_project.cashflows.serializers import BondSerializer


class BondViewSet(ModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()

    def get_queryset(self):
        queryset = Bond.objects.filter(user=self.request.user)
        return queryset
