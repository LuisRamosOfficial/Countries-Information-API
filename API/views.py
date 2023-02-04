from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getData(request):
    person = {
        'Name': 'Joao',
        'Age': 10
    }
    return Response(person)