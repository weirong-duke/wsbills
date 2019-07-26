from rest_framework import serializers
from app.pools.serializers.pool_user import PoolUserListSerializer

from app.pools.models.pool_user import PoolUser
from app.transactions.models.transaction import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    pool_user_id = serializers.IntegerField(write_only=True)
    pool_user = PoolUserListSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def validate(self, data):
        if PoolUser.objects.filter(pool=data['pool'], id=data['pool_user_id']).exists():
            return data
        raise serializers.ValidationError('User does not have access to this pool')


# class TransactionListSerializer(serializers.ModelSerializer)

# class TransactionSerializerCreate(serializers.ModelSerializer):
