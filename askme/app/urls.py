from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('questions/', views.questions, name='questions'),
    path('question/<int:question_id>', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('settings/', views.settings, name='settings'),
    path('', views.settings, name='index')
]