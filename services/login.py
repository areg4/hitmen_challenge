from rest_framework_simplejwt.tokens import RefreshToken
from modules.hitman.models import Hitmen
from rest_framework import status
from modules.hitman.serializers import UserSerializer
from utils.responses import fail_response, success_response

def get_token(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return fail_response("Error de autenticación", 
                             status.HTTP_400_BAD_REQUEST, 
                             serializer.errors)
    user = Hitmen.objects.filter(
        email=serializer.validated_data['email'], 
        password=serializer.validated_data['password'])
    if not user:
        return fail_response("Error de autenticación", 
                             status.HTTP_400_BAD_REQUEST, 
                             serializer.errors)
    refresh = RefreshToken.for_user(user[0])
    
    response = {
        'access': str(refresh.access_token)
    }
    return success_response("Login!", status.HTTP_200_OK, data=response)
