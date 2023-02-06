from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeSlider,HomeProducts,Homeabout,OurProducts,AboutOur,AboutTeam,AboutHappy,AboutPart,ContactUs
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request): 
        slider = HomeSlider.objects.all()
        products =HomeProducts.objects.all()
        homeabout =Homeabout.objects.all()
        
        return render(request, self.template_name, context={
            'slider':slider, 
            'products':products,
            'homeabout': homeabout
            
            })
    

class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request): 
        contactus =ContactUs.objects.all()
        return render(request, self.template_name, context={
            'contactus':contactus
            })
    

class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request): 
        aboutour =AboutOur.objects.all()
        aboutteam =AboutTeam.objects.all()
        abouthappy=AboutHappy.objects.all()
        aboutpart=AboutPart.objects.all()
        return render(request, self.template_name, context={
            'aboutour':aboutour,
            'aboutteam': aboutteam,
            'abouthappy':abouthappy,
            'aboutpart':aboutpart
        })
    

class ProductsListView(ListView):
    template_name = 'products.html'

    def get(self, request): 
        ourproducts =OurProducts.objects.all()
        return render(request, self.template_name, context={
            'ourproducts':ourproducts

        })
