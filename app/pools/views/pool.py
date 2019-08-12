from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from app.pools.models.pool import Pool
from app.pools.serializers.pool import PoolListSerializer, PoolDetailSerializer

# pools
class PoolView(APIView):

    @staticmethod
    def get(request):
        """
        description: List pools
        """
        print(request.user)
        if request.user.is_anonymous:
            return Response(data=[])

        pools = Pool.objects.filter(pool_users__user=request.user)

        return Response(PoolListSerializer(pools, many=True).data)

# pools/{pool_identifier}
class PoolDetailView(APIView):

    @staticmethod
    def get(request, pool_identifier):
        """
        description: Single pool detail
        """
        pool = Pool.objects.prefetch_related('pool_users').get(identifier=pool_identifier)

        return Response(PoolDetailSerializer(pool).data)
