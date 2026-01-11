from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Products, ProductCategory
from django.contrib import messages
from django.db.models import Min, Max
from collections import defaultdict
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core import serializers

def login_view(request):
    return render(request, 'MSMEOrderingWebApp/login.html', {
        'background_color': request.session.get('background_color', 'white'),
        'font_family': request.session.get('font_family', 'sans-serif'),
    })
