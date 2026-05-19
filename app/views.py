from multiprocessing import context

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HelloView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = 10
        b = 20
        context['result'] = a + b
        return context  
