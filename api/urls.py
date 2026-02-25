from django.urls import path
from . import views

urlpatterns = [
    path ('cadence/', views.CadenceView),
    path ('cadence/<int:pk>/', views.CadenceDetailView),
    path('employees/', views.EmployeeList.as_view()),
    path ('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]