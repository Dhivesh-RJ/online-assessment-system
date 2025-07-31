from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.take_test, name='take_test'),
    path('submit/', views.submit_test, name='submit_test'),
    path('results/', views.all_results, name='all_results'),
]
