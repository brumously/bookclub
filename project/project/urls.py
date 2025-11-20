"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
import bookclub.views as bookclub

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookclub.index),
    path('home/', bookclub.homepage),
    path('<int:pid>/<str:del_pass>/', bookclub.index),
    url(r'^captcha', include('captcha.urls')),
    path('login/', bookclub.login),
    path('logout/', bookclub.logout),
    #path('userinfo/', bookclub.userinfo),
    path('accounts/', include('registration.backends.default.urls')),
    path('booklog/', bookclub.booklog),
    path('booklog/<int:id>/', bookclub.viewBook),
    path('tbr/', bookclub.tbr),
    path('tbr/<int:id>/', bookclub.viewTbr),
    path('ask/', bookclub.rec),
    path('ask/<int:id>/', bookclub.viewAsk),
    path('ask/<int:id>/rec/', bookclub.submitRec),
    path('ask/<int:id>/del/', bookclub.delAsk),
    path('profile/<str:user>/', bookclub.viewProfile),
]
