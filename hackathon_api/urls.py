from django.urls import path
from .views import HackathonListAPIView,HackathonCreateAPIView,HackathonRegistrationAPIView

urlpatterns = [
    path('hackathons/', HackathonListAPIView.as_view(), name='hackathons'),
    path('create/', HackathonCreateAPIView.as_view(), name='hackathon-create'),
    path('register/<int:hackathon_id>/', HackathonRegistrationAPIView.as_view(), name='hackathon-register'),
]

