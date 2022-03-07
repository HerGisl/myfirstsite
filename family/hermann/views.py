from django.shortcuts import render

hermann = [
    {'first_name': 'Hermann',
     'middle_name': 'Þór',
     'last_name': 'Gíslason',
     'age': '44 ára'
     }
]

# Create your views here.
def index(request):
    return render(request, 'hermann/index.html', context={ 'hermann': hermann })