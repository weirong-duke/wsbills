from django.urls import path

from .views.pool import PoolView, PoolDetailView

urlpatterns = [
    path('pools', PoolView.as_view()),
    path('pools/<pool_identifier>', PoolDetailView.as_view()),
]
