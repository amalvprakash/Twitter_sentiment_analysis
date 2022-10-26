from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('get-sentiments', views.getSentiments, name="get-sentiments"),

    # path('',views.index,name='index'),
    path('reg/',views.reg,name='reg'),
    path('login/',views.login,name='login'),
    path('userhome/',views.userhome,name='userhome'),
    path('userlog/',views.userlog,name='userlog'),
    path('result/',views.result,name='result'),
    path('viewresult/',views.viewresult,name='viewresult'),
]