import logging
from venv import create
from modules.hits.serializers import HitSerializer, HitViewSerializer
from modules.hits.models import Hits
from rest_framework import status
from utils.responses import success_response, fail_response



def list_hits(hitman_id = None) -> dict:
    try:
        if hitman_id:
            hits = Hits.objects.filter(assignee=hitman_id) | Hits.objects.filter(created_by=hitman_id)
        else:
            hits = Hits.objects.filter()
        serializer = HitViewSerializer(hits, many=True)
        return success_response("List of Hits", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to get all Hits: {}".format(str(e)))
        return fail_response("Error to get all Hits: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_hit_detail(hit_id: int, user_request) -> dict:
    try:
        if user_request.isBoss:
            hit = Hits.objects.filter(id=hit_id)
        elif user_request.isManager:
            hit = Hits.objects.filter(id=hit_id, created_by=user_request.id) | Hits.objects.filter(id=hit_id, assignee=user_request.id)
        else:
            hit = Hits.objects.filter(id=hit_id, assignee=user_request.id)
        if not hit:
            return fail_response("Hit not found", 
                                status.HTTP_404_NOT_FOUND)
        serializer = HitViewSerializer(hit[0])
        return success_response("Hit details", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to get all Hits: {}".format(str(e)))
        return fail_response("Error to get all Hits: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_hit(data) -> dict:
    try:
        serializer = HitSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Error al crear un Hit", 
                                 status.HTTP_400_BAD_REQUEST, 
                                 serializer.errors)
        Hits.objects.create(**serializer.validated_data)
        serializer = HitViewSerializer(serializer.validated_data)
        return success_response("Hit created!", 
                                 status.HTTP_201_CREATED, 
                                 serializer.data)
    except Exception as e:
        logging.error("Error to create a Hit: {}".format(str(e)))
        return fail_response("Error to create a Hit: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def reassignment_hits(hit_id, hitman_id) -> dict:
    pass
