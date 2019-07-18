from rest_framework import serializers
from app.users.serializers.user import UserSerializer

from app.pools.models.pool_user import PoolUser
from app.transactions.models.transaction import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def validate(self, data):
        if PoolUser.objects.filter(pool=data['pool'], user=data['user_id']).count() == 0:
            raise serializers.ValidationError('User does not have access to this pool')
        return data


# class TransactionListSerializer(serializers.ModelSerializer)

# class TransactionSerializerCreate(serializers.ModelSerializer):
