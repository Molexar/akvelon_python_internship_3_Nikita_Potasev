from django.contrib.auth.models import User
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Transaction
from task_1.serializers import TransactionSerializer, UserListSerializer, TransactionCreateSerializer


class TransactionDetail(views.APIView):
    def get(self, request, pk):
        """Get detail transaction"""
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)


class TransactionList(views.APIView):
    def get(self, request):
        """Get all transactions"""
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'amount': openapi.Schema(type=openapi.TYPE_INTEGER),
            'date': openapi.Schema(type=openapi.FORMAT_DATE)
        }
    ))
    @api_view(['POST'])
    def post(self, request):
        # Create new transaction
        """Create new transaction"""
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
    """
    Endpoint that allows to view all user's payments without filtering
    """
    def get(self, request, pk):
        transactions = Transaction.objects.filter(user=pk)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class UserTransactionByDay(views.APIView):
    """
    Filtering transactions by user, date(or range), type of transaction and order
    """
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'date': openapi.Schema(type=openapi.FORMAT_DATE),
            'date_start': openapi.Schema(type=openapi.FORMAT_DATE),
            'date_end': openapi.Schema(type=openapi.FORMAT_DATE),
            'type': openapi.Schema(type=openapi.TYPE_STRING, description='income/outcome'),
            'order_by': openapi.Schema(type=openapi.TYPE_STRING, description='- if need reversed'),
        }
    ))
    @api_view(['POST'])
    def post(self, request):
        user_id = request.data.get('user')

        date = request.data.get('date')
        date_start, date_end = request.data.get('date_start'), request.data.get('date_end')

        order = request.data.get('order_by')

        type = request.data.get('type')

        if user_id:
            transactions = Transaction.objects.filter(user=user_id)
        else:
            transactions = Transaction.objects.all()

        if date:
            transactions = transactions.filter(date=date)
        elif date_start and date_end:
            transactions = transactions.filter(date__range=[date_start, date_end])
        if type == 'income':
            transactions.filter(amount__gt=0)
        elif type == 'outcome':
            transactions.filter(amount__lt=0)
        if order:
            transactions.order_by(order)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)




