from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('add/', ClientCreateView.as_view(), name='add_client'),
    path('edit/<uuid:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('delete/<uuid:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]