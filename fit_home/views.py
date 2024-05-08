from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hallo, hier wird zu Übungszwecken\
        eine fiktive Seite für eine Fitnessclub entstehen,\
        auf der man eine Mitgliedschaft abschließen kann\
        und verschiedene Sachen einmalig oder im Abo kaufen\
        kann. Auch wird es möglich sein über ein Benutzkonto\
        Rezessionen und Kommentare zu hinterlassen.\
        Als nächstes wird die Planung dafür erstellt und in\
        der Readme Datei gespeichert.')
