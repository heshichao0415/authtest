"""authtest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from apitest import views
from product import proviews
from bug import bugviews
from set import setviews
from apptest import appviews
from webtest import webviews



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    url(r'^login/', views.login),
    url(r'^home/', views.home),
    url(r'^logout/', views.logout),
    url(r'^product_manage/', proviews.product_manage),
    url(r'^apitest_manage/', views.apitest_manage),
    url(r'^apistep_manage/', views.apistep_manage),
    url(r'^apis_manage/', views.apis_manage),
    url(r'^bug_manage/', bugviews.bug_manage),
    url(r'^set_manage/', setviews.set_manage),
    url(r'^user/', setviews.set_user),
    url(r'^appcase_manage/', appviews.appcase_manage),
    url(r'^appcasestep_manage/', appviews.appcasestep_manage),
    url(r'^webcase_manage/', webviews.webcase_manage),
    url(r'^webcasestep_manage/', webviews.webcasestep_manage),
    url(r'^test_report/', views.test_report),                     #测试报告
    url(r'^left/', views.left),
    url(r'^''/', views.login)

]

