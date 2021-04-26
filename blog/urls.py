from django.urls import path

from .views import MainView,BlogDetailView

urlpatterns = [
    path('',MainView.as_view(), name='home'),
    path('detail/<int:pk>/',BlogDetailView.as_view(), name='post_detail' ),
]