from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from services.hits.hitsService import create_hit, list_hits, get_hit_detail

# Create your views here.
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_hits(request):
    if request.user.isBoss == True:
        hitman_id = None
    else:
        hitman_id = request.user.id
    hits_response = list_hits(hitman_id)
    return Response(data=hits_response, status=hits_response['status'])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_hit_details(request, hit_id):
    hit_response = get_hit_detail(hit_id, request.user)
    return Response(data=hit_response, status=hit_response['status'])
