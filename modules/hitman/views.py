from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from services.login import get_token
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from services.hitmen.hitmenService import create_hitman, get_hitman_detail, get_managed_profiles
from services.hitmen.hitmenService import get_list_hitmen
from rest_framework.response import Response
from .serializers import HitmanSerializer, UserSerializer



@swagger_auto_schema(
    method='post',
    operation_description="Register a new Hitman",
    request_body=HitmanSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_hitman(request):
    create_response = create_hitman(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='post',
    operation_description="Login to generate Token for the API",
    request_body=UserSerializer,
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def get_tokens_for_user(request):
    refresh = get_token(request)
    return Response(refresh, refresh["status"])


@swagger_auto_schema(
    method='get',
    operation_description="Get the List of Hitmen",
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER,
                          description=
                          "User Token Please put Bearer before the token. (Bearer Token). "
                          + "Go to /login/ to generate a new token.",
                          type=openapi.TYPE_STRING,
                          required=True, pattern="Bearer "),
    ],
    responses={
        200: "OK",
        400: "Bad Request",
        401: "Unauthorized",
        500: "Server Error"
    }
)
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


@swagger_auto_schema(
    method='get',
    operation_description="Get Hitman Detail",
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER,
                          description=
                          "User Token Please put Bearer before the token. (Bearer Token). "
                          + "Go to /login/ to generate a new token.",
                          type=openapi.TYPE_STRING,
                          required=True, pattern="Bearer "),
        openapi.Parameter('hitman_id', openapi.IN_PATH, 
                          description="hitman ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: "OK",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Server Error"
    }
)
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
