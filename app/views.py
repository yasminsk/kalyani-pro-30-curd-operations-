from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Cricket')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__gte='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lte='2012-07-25')
    
    d={'access':LOA}
    return render(request,'display_access.html',context=d)
