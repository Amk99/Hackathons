from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
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

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
        
        
        user_profile.register_hackathon(hackathon)
        
        return Response({'message': 'User successfully registered for the hackathon.'})
    


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EnrolledHackathonListAPIView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        user = request.user
        enrolled_hackathons = user.userprofile.registered_hackathons.all()
        hackathon_data = [
            {
                'id': hackathon.id,
                'title': hackathon.title,
                'description': hackathon.description,
            }
            for hackathon in enrolled_hackathons
        ]
        return Response(hackathon_data)