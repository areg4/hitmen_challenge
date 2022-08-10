import logging
from modules.hitman.models import Hitmen
from modules.hitman.serializers import HitmanSerializer
from utils.responses import success_response, fail_response
from rest_framework import status


def get_list_hitmen(manager_id: int = None) -> dict:
    try:
        if manager_id:
            hitmen = Hitmen.objects.filter(managedBy=manager_id)
        else:
            hitmen = Hitmen.objects.filter()
        serializer = HitmanSerializer(hitmen, many=True)
        return success_response("List of Hitmen", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to get Hitmen list: {}".format(str(e)))
        return fail_response("Error to get Hitmen list: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        

def create_hitman(data) -> dict:
    try:
        serializer = HitmanSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Error al dar de alta un Hitman", 
                                status.HTTP_400_BAD_REQUEST, serializer.errors)
        
        Hitmen.objects.create(**serializer.validated_data)
        return success_response("Hitman registered!", 
                                status.HTTP_201_CREATED, serializer.validated_data)
    except Exception as e:
        logging.error("Error to create a Hitman: {}".format(str(e)))
        return fail_response("Error to create a Hitman: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

def get_hitman_detail(hitman_id: int, manager_id: int = None) -> dict:
    try:
        if manager_id:
            hitman = Hitmen.objects.filter(id=hitman_id, managedBy = manager_id)
        else:
            hitman = Hitmen.objects.filter(id=hitman_id)
        if not hitman:
            return fail_response("Hitman not found", 
                                status.HTTP_404_NOT_FOUND)
        serializer = HitmanSerializer(hitman[0])
        return success_response("Hitman detail", 
                                status.HTTP_200_OK,
                                serializer.data)
    except Exception as e:
        logging.error("Error to get Hitman details: {}".format(str(e)))
        return fail_response("Error to get Hitman details: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def change_status_hitman(id) -> dict:
    pass


def get_managed_profiles(data):
    if data['success'] == True and data['data']['isManager']:
        profiles = Hitmen.objects.filter(managedBy=data['data']['id'])
        serializer = HitmanSerializer(profiles, many=True)
        data['data']['hitmen_managed'] = serializer.data
        return data
    return data


def get_is_lackey(hitman_id: int, manager_id: int) -> bool:
    try:
        hitman = Hitmen.objects.filter(id=hitman_id).filter(managedBy=manager_id)
        if hitman:
            return True
        return False
    except:
        return False
    
    
def hitman_exist(hitman_id: int):
    try:
        Hitmen.objects.get(id=hitman_id)
        return True
    except:
        return False
    

def get_status_hitman(hitman_id: int):
    try:
        Hitmen.objects.get(id=hitman_id, status='Active')
        return True
    except:
        return False