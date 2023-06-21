from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import *

# Create your views here.
def place_in_region(request, region_slug=None):
    current_region = None
    regions = Region.objects.all()
    places = Place.objects.all()

    if region_slug:
        current_region = get_object_or_404(Region, slug=region_slug)
        places = places.filter(region=current_region)

    return render(request, 'volunteer/list.html', {'current_region': current_region, 'regions': regions, 'places': places})

def place_detail(request, id, place_slug=None):
    place = get_object_or_404(Place, id=id, slug=place_slug)
    return render(request, 'volunteer/detail.html', {'place': place})

class PlaceUploadView(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['region', 'name', 'slug', 'image', 'description']
    template_name = 'volunteer/upload.html'
    success_url = reverse_lazy('volunteer:place_all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    '''
    model = Place
    fields = ['region', 'name', 'image', 'description']
    template_name = 'volunteer/upload.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})
    '''

class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Place
    success_url = '/'
    template_name = 'volunteer/delete.html'

class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Place
    fields = ['region', 'name', 'image', 'description']
    template_name = 'volunteer/update.html'
