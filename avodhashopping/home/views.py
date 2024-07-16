from django.shortcuts import render, get_object_or_404  # type: ignore
from django.core.paginator import Paginator, EmptyPage, InvalidPage 
from .models import *
from django.db.models import Q


# Create your views here.
# views.py
def home(request, c_slug=None):

    ca= None  
    prot = None
    prodt = None
    cat= categ.objects.all()
    
    
    if c_slug!=None:

     ca = get_object_or_404(categ, slug=c_slug) 

     prodt = prodect.objects.filter(category=ca,avilable=True)

    else: 
     prod = prodect.objects.all().filter(avilable=True)  
     paginator = Paginator(prod,4)
     try:  
       
          
        page = int(request.GET.get('page', '1'))     
   
     except:
        page = 1
     try:
          prot = paginator.page(page)
     except(InvalidPage,EmptyPage):
         prot = paginator.page(paginator.num_pages)   
              

         
           
        
            
         
              
         
        
        
     
            
    
           
            
      
             

     

     
         
         
        

            
      
            
                     
    return render(request, 'home.html', { 'cat': cat ,'pg': prot})            


def details(request, ct_slug, prodect_slug):
    prodecte = get_object_or_404(prodect, category__slug=ct_slug, slug=prodect_slug)

    return render(request, 'details.html', {'prodecte': prodecte})


def sarchea(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = prodect.objects.all().filter(Q(name__contains=query) | Q(dic__contains=query))
    return render(request, 'sarch.html', {'qrn': query, 'pr': prod})
