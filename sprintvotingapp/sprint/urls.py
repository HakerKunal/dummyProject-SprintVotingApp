from django.urls import path

from . import views

urlpatterns = [
    path('sprint', views.SprintC.as_view(), name='add'),
    path('sprint/<int:id>', views.SprintC.as_view(), name='update'),

]
