from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path ('cadence/', views.CadenceView),
    path ('cadence/<int:pk>/', views.CadenceDetailView),

    # path('employees/', views.EmployeeList.as_view()),
    # path ('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogsDetail.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view())
]