from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)
