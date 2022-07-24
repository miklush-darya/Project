from rest_framework  import serializers
from .models import User, Shop



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 
                'username',
                'created',
                )


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name_shop', 
                'unp',
                'user',
                )