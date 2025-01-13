from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ClientListView(ListView):
    model = Client
    template_name = 'crm/client_list.html'
    context_object_name = 'client_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        sort_option = self.request.GET.get('sort', 'first_name')  # Default sort
    
        if search_query:
            queryset = queryset.filter(
                first_name__icontains=search_query
            ) | queryset.filter(
                last_name__icontains=search_query
            ) | queryset.filter(
                email__icontains=search_query
            )
        
        return queryset.order_by(sort_option)
    
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'crm/add_client.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'crm/edit_client.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'crm/delete_client.html'
    success_url = reverse_lazy('client_list')


