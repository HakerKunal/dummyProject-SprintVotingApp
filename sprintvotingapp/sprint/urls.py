from django.urls import path

from . import views

urlpatterns = [
    path('sprint', views.SprintC.as_view(), name='add'),
    path('sprint/<int:id>', views.SprintC.as_view(), name='update'),
    path('param', views.VoteParameter.as_view(), name='add-parameter'),
    path('param/<int:id>', views.VoteParameter.as_view(), name='update-parameter'),
    path('sprint/<int:id>/vote', views.Voting.as_view(), name='user-votes'),
    path('sprint/<int:id>/result', views.Result.as_view(), name='result'),

]
