from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.operations,name='addition'),
    # path('sub/',views.operations,name='substraction'),
    # path('mul/',views.operations,name='multiplication'),
    # path('div/',views.operations,name='division')



]
