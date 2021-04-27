from django.urls import path

from .views import (MainView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView, 
                    
                    )


urlpatterns = [
    path('',MainView.as_view(), name='home'),
    path('detail/<int:pk>/',BlogDetailView.as_view(), name='post_detail' ),
    path('detail/new/', BlogCreateView.as_view(), name='post_new'), 
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete')

]