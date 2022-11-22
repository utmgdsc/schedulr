from django.urls import path
from . import views
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoute),
    path('notes', views.getNotes),
    path('huh', views.getTcourses),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('events/', views.getEvents, name='events'),
]