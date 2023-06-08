from rest_framework import generics, permissions
from .models import Submission, Hackathon
from .serializers import SubmissionSerializer
from rest_framework.decorators import  authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

class SubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        hackathon_id = self.kwargs['hackathon_id']
        hackathon = Hackathon.objects.get(id=hackathon_id)
        serializer.save(user=self.request.user, hackathon=hackathon)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class SubmissionListAPIView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hackathon_id = self.kwargs['hackathon_id']
        return Submission.objects.filter(user=self.request.user, hackathon__id=hackathon_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)