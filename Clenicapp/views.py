from django.shortcuts import render
from .models import Clinec_site, Clinic_about_us


# Create your views here.

def main_page(request):
    cardInfo = Clinec_site.objects.all()
    cards_list = []
    for i in cardInfo:
        cards_list.append({"i": i})
    name = request.GET.get('name') or ''
    context = {"cards_list": cards_list,
               'name': name}
    return render(request, 'home.html', context)


def about_us(request):
    about = Clinic_about_us.objects.all()
    aboutList = []
    for a in about:
        aboutList.append({'a': a})
    name = request.GET.get('name') or ''
    context = {'aboutList': aboutList,
               'name': name}
    return render(request, 'about_us.html', context)


def connect(request):
    return render(request, 'connect_us.html')


def details(request):
    detailInfo = Clinec_site.objects.all()
    details_list = []
    for i in detailInfo:
        details_list.append({"i": i})
    name = Clinec_site.healName
    context = {"details_list": details_list,
               "name": name,
               }
    return render(request, 'details.html', context)


def knee_pain(request):
    return render(request, 'knee_pain.html')


def fakry(request):
    return render(request, 'fakry.html')


def PG_injuries(request):
    return render(request, 'PG_injuries.html')
