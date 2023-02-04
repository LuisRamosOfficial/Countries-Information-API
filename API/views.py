from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WorkBook
import os
from openpyxl import load_workbook

path = f"{os.path.dirname(__file__)[:-3]}API\Data\Countries_data.xlsx"
workbook = load_workbook(path)

wb = WorkBook(workbook)

# Create your views here.

@api_view(['GET'])
def getData(request):
    person = {
        'Name': 'Joao',
        'Age': 10
    }
    return Response(person)

@api_view(['GET'])
def getNames(request):
    
    return Response(wb.get_names())

@api_view(['GET'])
def getCountry(request, name):
    
    return Response(wb.get_countries_data(name))