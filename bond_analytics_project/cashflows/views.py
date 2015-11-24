from django.http import JsonResponse
from django.views.generic import View
from bond_analytics_project.cashflows.models import Bond


# Create your views here.
class AddBondView(View):
    model = Bond
