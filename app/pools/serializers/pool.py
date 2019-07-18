from rest_framework import serializers

from app.pools.models.pool import Pool

class PoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pool
        fields = '__all__'

# class CollaborationListSerializer(serializers.ModelSerializer)