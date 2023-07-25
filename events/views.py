from django.shortcuts import render,HttpResponse,redirect
from .models import Event
def events(request):
    daysno=list()
    for i in range(0,31):
        daysno.append(i+1)
    event=Event.objects.all()
    campDays=[4,5]
    context={'daysno':daysno,'event':event,"campDays":campDays}
    return render(request,'home/events.html',context)