from rest_framework.response import Response
from rest_framework.views import APIView

from app.utils import get_query_param_filters

from app.pools.models.pool_user import PoolUser
from app.transactions.models.transaction import Transaction
from app.transactions.serializers.transaction import TransactionSerializer

class TransactionView(APIView):
    @staticmethod
    def get_filtered_transactions(request):
        viewable_pools = PoolUser.objects.filter(user=request.user)
        print('hm ', get_query_param_filters(request))

        return Transaction.objects.filter(pool__in=viewable_pools.values_list('pool', flat=True), **get_query_param_filters(request))

    @staticmethod
    def get(request):
        """
        description: List transactions
        """
        transactions = TransactionView.get_filtered_transactions(request)

        return Response(TransactionSerializer(transactions, many=True).data)

    @staticmethod
    def post(request):
        """
        :param request: 
        :return: 
        """
        transaction = TransactionSerializer(data=request.data)
        print('haskdlfjaslf', request.data)
        transaction.is_valid(raise_exception=True)
        transaction.save()
        return Response(transaction.data)