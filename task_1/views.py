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
        getting: user_id, date, date_start, date_end, is income/outcome, order_by parameters
    """
    # TODO: filter by income/outcome
    def post(self, request):
        user_id = request.data.get('user')

        date = request.data.get('date')
        date_start, date_end = request.data.get('date_start'), request.data.get('date_end')

        order = request.data.get('order_by')

        is_income = request.data.get('income')
        is_outcome = request.data.get('outcome')

        transactions = Transaction.objects.filter(user=user_id)

        if date:
            transactions = transactions.filter(date=date)
        elif date_start and date_end:
            transactions = transactions.filter(date__range=[date_start, date_end])
        if is_income:
            transactions.filter(amount__gt=0)
        elif is_outcome:
            transactions.filter(amount__lt=0)
        if order:
            transactions.order_by(order)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)




