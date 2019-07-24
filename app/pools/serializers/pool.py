from rest_framework import serializers

from app.pools.models.pool import Pool
from app.pools.serializers.pool_user import PoolUserListSerializer

class PoolListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pool
        fields = '__all__'

class PoolDetailSerializer(serializers.ModelSerializer):
    pool_users = PoolUserListSerializer(many=True)
    class Meta:
        model = Pool
        fields = '__all__'