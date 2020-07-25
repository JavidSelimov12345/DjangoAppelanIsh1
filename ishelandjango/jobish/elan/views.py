from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
from django.core.paginator import Paginator

class HomeView(ListView):
    context_object_name='javid'
    template_name='index.html'
    paginate_by=6
    queryset = Elan.objects.all()
    
    def get_context_data(self, **kwargs):
            context = super(HomeView, self).get_context_data(**kwargs)
            context['Categoriess'] = Categories.objects.all()
            context['Elans'] = self.queryset
            return context

class DEview(DetailView):
    template_name='job-details.html'
    model=Elan
    