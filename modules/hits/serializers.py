from rest_framework import serializers
from .models import Hits
from services.hitmen.hitmenService import get_is_lackey, hitman_exist, get_status_hitman


class HitSerializer(serializers.ModelSerializer):
    is_boss = serializers.BooleanField(default=False)
    class Meta:
        model = Hits
        fields = ['id', 'assignee', 'desc', 'target', 'status', 'created_by', "is_boss"]
        write_only_fields = ['is_boss']
        
    def validate(self, attrs):
        if not hitman_exist(attrs['assignee']) and not get_status_hitman(attrs['assignee']):
            raise serializers.ValidationError({
                "assignee": "No puede asignar a este Hitman no existe o no está disponible"
            })
            
        if not is_lackeys(attrs['assignee'], attrs['created_by'].id, attrs['is_boss']):
            raise serializers.ValidationError({
                "assignee": "No puede asignar a este Hitman"
            })
            
        if attrs['assignee'] == attrs['created_by'].id:
            raise serializers.ValidationError({
                "assignee": "No puede asignar a sí mismo"
            })
            
        attrs.pop('is_boss')
        return super().validate(attrs)
   
    
class HitViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hits
        fields = ['id', 'assignee', 'desc', 'target', 'status', 'created_by']
    
    
def is_lackeys(hitman_id, manager_id: int, is_boss: bool) -> bool:
    try:
        if is_boss:
            return True
        return get_is_lackey(hitman_id, manager_id)
    except:
        return False
    