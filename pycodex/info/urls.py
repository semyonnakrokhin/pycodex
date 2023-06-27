from django.urls import path
from info.views import index, course


urlpatterns = [
    path('', index, name='home'),
    path('course/<int:pk>/', course, name='course')
]