from django.urls import path

from .views.pool import PoolView

urlpatterns = [
    path('pools', PoolView.as_view()),
]
