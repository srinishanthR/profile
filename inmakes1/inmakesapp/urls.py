from . import views
from django.urls import path

urlpatterns = [
# PASSING VALUS FROM ONE PAGE TO ANOTHER
    # path('',views.demo1,name='demo1'),
    # path('add/',views.addition,name='addition')
# STATIC WEBSITE
    path('',views.demo,name='demo')
]