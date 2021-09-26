from django.shortcuts import render,redirect
from . models import Product,Location,ProductMovement
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

#Product--------------------------------
class ProductView(ListView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'productCreate.html'
    fields = ['product_id',]

    success_url = '/product'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'productUpdate.html'
    fields = ['product_id',]
    success_url = "/product"

#Location--------------------------------

class LocationView(ListView):
    template_name = 'location.html'
    model = Location
    context_object_name = 'locations'

class LocationCreateView(CreateView):
    model = Location
    template_name = 'locationCreate.html'
    fields = ['location_id',]

    success_url = '/location'

class LocationUpdateView(UpdateView):
    model = Location
    template_name = 'locationUpdate.html'
    fields = ['location_id',]
    success_url = "/location"

#Movement--------------------------------

class MovementView(ListView):
    template_name = 'movement.html'
    model = ProductMovement
    context_object_name = 'movements'

class MovementCreateView(CreateView):
    model = ProductMovement
    template_name = 'movementCreate.html'
    fields = ['movement_id', 'from_location', 'to_location', 'product_id', 'qty']
    success_url = '/movement'

class MovementUpdateView(UpdateView):
    model = ProductMovement
    template_name = 'movementUpdate.html'
    fields = ['from_location', 'to_location', 'product_id', 'qty']
    success_url = "/movement"

class MovementToView(UpdateView):
    model = ProductMovement
    template_name = 'movementTo.html'
    fields = ['to_location',]

    def form_valid(self,form):
        instance = form.save(commit=False)
        
        instance.from_location = None
        instance.save()

        return redirect('movement_list_view')

class MovementOutView(UpdateView):
    model = ProductMovement
    template_name = 'movementOut.html'
    fields = ['from_location',]

    def form_valid(self,form):
        instance = form.save(commit=False)
        
        instance.to_location = None
        instance.save()

        return redirect('movement_list_view')
    
    # success_url = "/movement"

# Reports------------------------
class ReportView(ListView):
    template_name = 'report.html'
    model = ProductMovement
    context_object_name = 'reports'