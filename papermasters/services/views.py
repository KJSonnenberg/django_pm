from django.shortcuts import render, get_object_or_404
from .models import Service

def index(request):
    services = Service.objects.all()
    context = {
        'services': services
    }

    return render(request, 'services/index.html', context)