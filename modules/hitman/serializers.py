from rest_framework import serializers
from .models import Hitmen


class HitmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hitmen
        fields = ['id', 'name', 'email', 'password', 'desc', 'isActive', 'isManager', 'managedBy', 'isBoss']
        # read_only_fields = ['isActive', 'isManager']
        write_only_fields = ['password']
        
    def validate(self, attrs):
        if "isBoss" in attrs and attrs['isBoss'] == True and there_is_boss():
            raise serializers.ValidationError({
                "isBoss": "No puede haber dos Boss en este negocio."
            })
            
        if "managedBy" in attrs and attrs['managedBy'] and not is_hitman_manager(attrs['managedBy']):
            raise serializers.ValidationError({
                "managedBy":
                "El id del Manager es incorrecto o no existe, favor de envíar un id de un manager"})
        
        return super().validate(attrs)
    

def is_hitman_manager(hitman_id: int) -> bool:
    try:
        hitman = Hitmen.objects.get(id=hitman_id)
        return hitman.isManager
    except:
        return False

def there_is_boss() -> bool:
    try:
        boss = Hitmen.objects.filter(isBoss=True)
        if boss:
            return True
        return False
    except:
        return True
    
    
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)
    password = serializers.CharField(max_length=250)