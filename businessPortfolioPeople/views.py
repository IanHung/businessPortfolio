# Create your views here.
from django.shortcuts import render
from businessPortfolioPeople.models import Person


def index(request):
    people_list = Person.objects.order_by('lastName', 'firstName')
    return render(request, 'businessPortfolioPeople/people.html', {'people_list': people_list})
