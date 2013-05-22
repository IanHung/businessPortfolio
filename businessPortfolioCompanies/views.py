# Create your views here.
from django.shortcuts import render
from businessPortfolioCompanies.models import Company

def index(request):
    companies_list = Company.objects.order_by('-success', 'dateFounded')
    return render(request, 'businessPortfolioCompanies/companies.html', {'companies_list': companies_list})