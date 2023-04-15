from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='user-register'),
    path('agents/', views.AgentList.as_view(), name='agent-list'),
    path('agents/<int:pk>/', views.AgentDetail.as_view(), name='agent-detail'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('achievements/', views.AchievementList.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', views.AchievementDetail.as_view(), name='achievement-detail'),
    path('ratings/', views.RatingList.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='rating-detail'),
]
