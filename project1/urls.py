"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic import TemplateView, ListView
from app1 import views as myapp
from app1.views import StaticView
from app1.models import Dreamreal

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/',myapp.hello,name='hello'),
    url(r'^article/(\d+)/',myapp.viewArticle,name='article'),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})',myapp.viewArticles , name = 'articles'),
    url(r'^crud/',myapp.crudops,name='crud'),
    url(r'^select/',myapp.datamanipulation,name='select'),
    url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',myapp.sendSimpleEmail, name = 'sendSimpleEmail'),
    url(r'^massEmail/(?P<emailto1>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<emailto2>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', myapp.sendMassEmail, name = 'sendMassEmail'),
    url(r'^emailManager/',myapp.sendManagersEmail,name='emailManager'),
    url(r'^emailAdmins/',myapp.sendAdminsEmail,name='emailAdmins'),
    url(r'^htmlemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,4})/',myapp.sendHTMLEmail, name = 'sendHTMLEmail'),
    url(r'^fileemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,4})/',myapp.sendEmailWithAttach, name = 'fileemail'),
    url(r'^statis/$',StaticView.as_view()),
    url(r'^statis1/',TemplateView.as_view(template_name = 'static.html')),
    path('dreamreals/', ListView.as_view(template_name = "dreamreal_list.html", model = Dreamreal, context_object_name = "dreamreals",)),
    path('connection/',TemplateView.as_view(template_name='login.html')),
    path('login/',myapp.login, name='login'),
    path('profile/',TemplateView.as_view(template_name='profile.html')),
    path('saved/',myapp.SaveProfile, name='saved'),
]
