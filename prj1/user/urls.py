from django.urls import path
from . import views

urlpatterns = [
 path('',views.log,name='login'),
 path('reg',views.reg,name='reg'),
 path('ho',views.hom,name='home'),


  path('login_btn',views.login_btn),
  path('register',views.register)
]
