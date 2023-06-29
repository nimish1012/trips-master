"""
URL configuration for travelpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from tripapp import views
from tripmaster import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('trips', views.trips, name='trips'),
    path('blog', views.blog, name='blog'),
    path('triper/<int:id>/', views.trip_single, name='triper'),
    path('register/', views.register, name='register'),
    path('log_in', views.log_in, name='log_in'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('addstory', views.addstory, name='addstory'),
    path('addtrip', views.addtrip, name='addtrip'),
    path('single/<int:id>/', views.single, name='single'),
    path('option', views.option, name='option'),
    path('javascript', views.javascript, name='javascript'),




              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
