from django.urls import path
from .views import HackathonListAPIView,HackathonCreateAPIView,HackathonRegistrationAPIView,EnrolledHackathonListAPIView

urlpatterns = [
    path('hackathons/', HackathonListAPIView.as_view(), name='hackathons'),
    path('create/', HackathonCreateAPIView.as_view(), name='hackathon-create'),
    path('register/<int:hackathon_id>/', HackathonRegistrationAPIView.as_view(), name='hackathon-register'),
    path('enrolled/', EnrolledHackathonListAPIView.as_view(), name='enrolled-hackathon-list'),

]   

