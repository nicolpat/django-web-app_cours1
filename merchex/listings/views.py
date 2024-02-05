from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Title

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Title.objects.all()
    return HttpResponse(f"""
            <h1>Liste !</h1>
            <p>Les evenements à venir sont :<p>
            <ul>
                <li>{titles[0].name}</li>
                <li>{titles[1].name}</li>
                <li>{titles[2].name}</li>
            </ul>
    """)

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p></p>')