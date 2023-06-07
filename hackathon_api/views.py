from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Hackathon
from .serializers import HackathonSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



@authentication_classes([])
@permission_classes([AllowAny])
class HackathonListAPIView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

@authentication_classes([])
@permission_classes([AllowAny])
class HackathonCreateAPIView(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class HackathonRegistrationAPIView(generics.GenericAPIView):
    
    def post(self, request, hackathon_id, *args, **kwargs):
        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            return Response({'message': 'Hackathon does not exist.'}, status=404)
        
        user_profile = request.user.userprofile
        
        if user_profile.is_registered_for_hackathon(hackathon):
            return Response({'message': 'User is already registered for the hackathon.'})
        
        # Perform any additional validation or business logic before registering the user
        
        user_profile.register_hackathon(hackathon)
        
        return Response({'message': 'User successfully registered for the hackathon.'})