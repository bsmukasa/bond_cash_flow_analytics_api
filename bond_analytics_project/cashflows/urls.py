from django.conf.urls import url

from bond_analytics_project.cashflows.views import BondValuation

urlpatterns = [
    url(
        regex=r'^add/',
        view=BondValuation.as_view(),
        name='addBond'
    ),
]
