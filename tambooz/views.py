from django.shortcuts import render,HttpResponse,redirect
from events.models import Gallery,Testonomials
def homepage(request):
    testonomials=Testonomials.objects.all()[0:4]
    context={'testonomials':testonomials}
    return render(request,'home/home.html',context)

def gallery(request):
    gallery=Gallery.objects.all()
    context={'galleryObject':gallery}
    return render(request,'home/gallery.html',context)

