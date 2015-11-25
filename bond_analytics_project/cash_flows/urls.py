from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from bond_analytics_project.cash_flows import viewsets
from bond_analytics_project.cash_flows.views import BondValuation

router = DefaultRouter()
router.register(r'bonds', viewsets.BondViewSet)

urlpatterns = [
    url(
        regex=r'^add/',
        view=BondValuation.as_view(),
        name='addBond'
    ),

    url(
        regex=r'^api/v1/',
        view=include(router.urls)
    ),
]
