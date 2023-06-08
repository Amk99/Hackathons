from django.urls import path
from .views import SubmissionCreateAPIView,SubmissionListAPIView


urlpatterns = [
    path('create/<int:hackathon_id>/', SubmissionCreateAPIView.as_view(), name='create-submission'),
    path('my_submissions/<int:hackathon_id>/', SubmissionListAPIView.as_view(), name='my-submission'),

]