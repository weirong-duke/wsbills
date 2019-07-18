from django.urls import path

from app.transactions.views.transaction import TransactionView

urlpatterns = [
    path('transactions', TransactionView.as_view()),
]
