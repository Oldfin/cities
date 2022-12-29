from django.shortcuts import render


def main(request):
    path = request.path
    path = path.replace('/', '')
    if path == "":
        path = 'main'
    cities = ['Москва', 'Санкт-петербург', 'Калининград', 'Белосток', 'Минск', 'Севастополь', 'Казань']
    return render(request, f"{path}.html", {'cities': cities})
# Create your views here.
