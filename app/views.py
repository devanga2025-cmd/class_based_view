from multiprocessing import context
from urllib import request

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
    
class  content_view(TemplateView):
      def get(self, request):
        context = {
            "message": request.custom_message,
            "ip": request.user_ip,
            "method": request.request_method,
            "path": request.path
        }

        return render(request, "content.html", context)
    

