"""featReqApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from feature import views

urlpatterns = [
    url(r'^hello$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.feature_list, name='feature_list'),
    url(r'^features/create/$', views.feature_create, name='feature_create'),
    url(r'^features/(?P<pk>\d+)/update/$', views.feature_update, name='feature_update'),
    url(r'^features/(?P<pk>\d+)/delete/$', views.feature_delete, name='feature_delete'),
    url(r'^client/create/$', views.create_client, name='create_client'),
    url(r'^client/(?P<clientId>\d+)/maxPriorityAvail/$', views.client_max_priority, name='client_max_priority'),
]
