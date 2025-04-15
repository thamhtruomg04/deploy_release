# myapp/views.py
from django.http import HttpResponse, JsonResponse
from .models import MyModel

def health_check(request):
    return HttpResponse("OK", status=200)

def home(request):
    return JsonResponse({"message": "Welcome to My Django App"})