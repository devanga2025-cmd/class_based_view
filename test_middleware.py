import os
import django
import sys
from django.test import RequestFactory

sys.path.append(r'd:\class_based_views')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classbased.settings')
django.setup()

from app import views
from app.middleware import RequestInfoMiddleware

def get_response(request):
    return views.content_view.as_view()(request)

middleware = RequestInfoMiddleware(get_response)

rf = RequestFactory()
request = rf.get('/content/')

try:
    response = middleware(request)
    print(f"Status: {response.status_code}")
    print(f"Content: {response.content.decode('utf-8')}")
except Exception as e:
    import traceback
    traceback.print_exc()
