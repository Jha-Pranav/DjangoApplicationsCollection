from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pools'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:question_id>/', views.details, name='detail'),
    path('<int:pk>/', views.DetailsValue.as_view(), name='detail'),
    # path('<int:question_id>/result', views.results, name='result'),
    path('<int:pk>/result', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
