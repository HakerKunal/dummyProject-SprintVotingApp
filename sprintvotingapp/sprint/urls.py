from django.urls import path

from . import views

urlpatterns = [
    path('sprints', views.SprintC.as_view(), name='add'),
    path('sprints/<int:id>', views.SprintC.as_view(), name='update'),
    path('params', views.VoteParameter.as_view(), name='add-parameter'),
    path('params/<int:id>', views.VoteParameter.as_view(), name='update-parameter'),
    path('sprints/<int:id>/votes', views.Voting.as_view(), name='user-votes'),
    path('sprints/<int:id>/results', views.Result.as_view(), name='result'),
    path('sprintdata', views.SprintData.as_view(), name='sprintdata')

]
