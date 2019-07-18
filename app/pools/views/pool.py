from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from app.pools.models.pool import Pool
from app.pools.serializers.pool import PoolSerializer

# pools
class PoolView(APIView):

    @staticmethod
    def get(request):
        """
        description: List pools
        """

        pools = Pool.objects.all()

        return Response(PoolSerializer(pools, many=True).data)
