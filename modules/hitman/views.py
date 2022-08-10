from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from services.login import get_token
from drf_yasg.utils import swagger_auto_schema
from services.hitmen.hitmenService import create_hitman, get_hitman_detail, get_managed_profiles
from services.hitmen.hitmenService import get_list_hitmen
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def register_hitman(request):
    create_response = create_hitman(request.data)
    return Response(data=create_response, status=create_response['status'])


@api_view(['POST'])
@permission_classes([AllowAny])
def get_tokens_for_user(request):
    refresh = get_token(request)
    return Response(refresh, refresh["status"])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_hitmen(request):
    authorized = None
    if (request.user.isManager == True) or (request.user.isBoss == True):
        authorized = True
    if not authorized:
        return Response(status=401)
    if (request.user.isManager == True):
        list_response = get_list_hitmen(request.user.id)
    else:
        list_response = get_list_hitmen()
    return Response(data=list_response, status=list_response['status'])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hitman_detail(request, hitman_id):
    authorized = None
    if (request.user.isManager == True) or (request.user.isBoss == True):
        authorized = True
    if not authorized and (request.user.id != hitman_id):
        return Response(status=401)
    if request.user.isManager == True:
        hitman_response = get_hitman_detail(hitman_id, request.user.id)
    else:
        hitman_response = get_hitman_detail(hitman_id)
    hitman_response = get_managed_profiles(hitman_response)
    return Response(data=hitman_response, status=hitman_response['status'])
