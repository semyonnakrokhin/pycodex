from django.urls import path
from info.views import index, course


urlpatterns = [
    path('', index, name='home'),
    path('courses/<int:pk>/', course, name='course')
]