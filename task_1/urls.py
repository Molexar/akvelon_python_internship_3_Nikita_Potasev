from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from task_1 import views

# Adding urls for api:
# 1. ViewSets using for default view of models: CRUD
router = routers.DefaultRouter()
# Router for userList, detailUser
router.register('api/users', views.UserViewSet, 'users')

# 2. Adding urls for other operations
urlpatterns = [
    # Endpoint that works with CRUD queries for Transaction model
    path('api/transactions/', views.TransactionList.as_view()),
    # Endpoint transaction detail
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view()),
    # Endpoint that allows to view all user's payments without filtering
    path('api/payments/<int:pk>/', views.UserTransactions.as_view()),
    # Endpoint that allows view transactions of user by a day or range with argument for sorting
    path('api/payments/', views.UserTransactionByDay.as_view()),

]

urlpatterns += router.urls
