from django import forms
from main.models import Employee, Company

class EmployeeAssociationForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Select an employee")
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select a company")
