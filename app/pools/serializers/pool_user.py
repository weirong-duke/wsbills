from rest_framework import serializers
from app.users.serializers.user import UserSerializer

from app.pools.models.pool_user import PoolUser

class PoolUserListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PoolUser
        fields = '__all__'