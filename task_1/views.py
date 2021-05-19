from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, permissions, views
from rest_framework.response import Response

from .models import Transaction
from task_1.serializers import TransactionSerializer, UserListSerializer, TransactionCreateSerializer


class TransactionList(views.APIView):
    """Endpoint that works with CRUD queries for Transaction model"""
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        transaction = TransactionCreateSerializer(data=request.data)
        if transaction.is_valid():
            transaction.save()
        return Response(status=201)

    def put(self, request):
        user_id = request.data.get('user')
        amount = request.data.get('amount')
        date = request.data.get('date')
        if amount != "" and date != "":
            obj = Transaction.objects.get(user=user_id)
            obj.update(amount=amount)
            obj.update(date=date)
        return Response(status=201)

    def delete(self, request):
        user_id = request.data.get('user')
        Transaction.objects.filter(user=user_id).delete()
        return Response(status=201)


class UserViewSet(viewsets.ModelViewSet):
    """Standard viewSet for model User that implements get,post,put,delete"""
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserListSerializer


class UserTransactions(views.APIView):
    """Endpoint that allows to view all user's payments without filtering
        getting: user_id parameter
    """
    def get(self, request, pk):
        transactions = Transaction.objects.filter(user=pk)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class UserTransactionByDay(views.APIView):
    """Endpoint that allows view transactions of user by a day with argument for sorting
        getting: user_id, date, order_by parameters
    """
    # TODO: filter by income/outcome
    def post(self, request):
        date = request.data.get('date')
        user_id = request.data.get('user')
        order = request.data.get('order_by')
        transactions = Transaction.objects.filter(Q(date=date) & Q(user=user_id))
        if order != "":
            transactions.order_by(order)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)




