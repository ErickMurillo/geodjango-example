from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import *
from django.views.generic import ListView,DetailView

# Create your views here.

# def index(request):
# 	return render_to_response('index.html', {
#     })

class IndexView(ListView):
	template_name = 'index.html'
	model = WorldBorder

class MapaDetailView(DetailView):
	template_name = 'detail-map.html'
	model = WorldBorder