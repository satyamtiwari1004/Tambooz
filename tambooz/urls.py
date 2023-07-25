from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "Tambooz Admin"
admin.site.site_title = "Tambooz Admin Page"
admin.site.index_title = "Welcome to Tambooz"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/',include('booking.urls')),
    path('payment/',include('payment.urls')),
    path('events/',include('events.urls')),
    path('accounts/',include('accounts.urls')),
    path('gallery/',views.gallery),
    path('',views.homepage)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
