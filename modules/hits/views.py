from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from services.hits.hitsService import create_hit, list_hits, get_hit_detail
from .serializers import HitViewSerializer


# Create your views here.
@swagger_auto_schema(
    method='post',
    operation_description="Create a Hit",
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER,
                          description=
                          "User Token Please put Bearer before the token. (Bearer Token). "
                          + "Go to /login/ to generate a new token.",
                          type=openapi.TYPE_STRING,
                          required=True, pattern="Bearer "),
    ],
    request_body=HitViewSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        500: "Server Error"
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_hit(request):
    authorized = None
    if (request.user.isManager == True) or (request.user.isBoss == True):
        authorized = True
    if not authorized:
        return Response(status=401)
    request.data['is_boss'] = request.user.isBoss
    request.data['created_by'] = request.user.id
    create_response = create_hit(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get the List of Hits",
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
def get_list_hits(request):
    if request.user.isBoss == True:
        hitman_id = None
    else:
        hitman_id = request.user.id
    hits_response = list_hits(hitman_id)
    return Response(data=hits_response, status=hits_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get Hits Detail",
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER,
                          description=
                          "User Token Please put Bearer before the token. (Bearer Token). "
                          + "Go to /login/ to generate a new token.",
                          type=openapi.TYPE_STRING,
                          required=True, pattern="Bearer "),
        openapi.Parameter('hit_id', openapi.IN_PATH, 
                          description="hit ID", 
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
def get_hit_details(request, hit_id):
    hit_response = get_hit_detail(hit_id, request.user)
    return Response(data=hit_response, status=hit_response['status'])
