from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Company, Employee
from main.forms import EmployeeAssociationForm

# Create your views here.

def companies_view(request):
    if request.method == 'POST':
        form = EmployeeAssociationForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            employee = form.cleaned_data['employee']
            company.employees.add(employee)
            return redirect('companies_view')
    else:
        form = EmployeeAssociationForm()

    companies = Company.objects.all()
    return render(request, 'companies.html', {"companies": companies, "form": form})


