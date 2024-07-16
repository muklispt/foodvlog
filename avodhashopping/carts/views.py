from django.shortcuts import render,redirect,get_object_or_404
from home.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def cartd(request,tot=0,count=0,cart_items=None):
    try:

        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=item.objects.filter(cart=ct,active=True)
        for i in ct_items: 

            tot += (i.prodt.price*i.quan)
            count += i.quan
    except ObjectDoesNotExist:    
                     pass  
                   
    return render(request,'cart.html',{'ci' : ct_items,'t' : tot,'c' : count})               
  
    

    
    
           


    
       
        

   
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()

        
    return ct_id
def add_cart(request,product_id):
    prod= prodect.objects.get(id=product_id)
    try:
        ct= cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_item=item.objects.get(prodt=prod,cart=ct)
        if c_item.quan < c_item.prodt.stock:
            c_item.quan += 1
            c_item.save()
    except item.DoesNotExist:
        c_item=item.objects.create(prodt=prod,cart=ct,quan=1)
        c_item.save()
          
    return  redirect('cart') 
def main_cart(requst,product_id):
     ct=cartlist.objects.get(cart_id=c_id(requst))
     prod=get_object_or_404(prodect, id=product_id)
     c_item=item.objects.get(prodt=prod,cart=ct)
     if c_item.quan> 1:
          c_item.quan -= 1
          c_item.save()
     else:      
      c_item.delete()
     
     
          
     return redirect('cart')  
def remove_cart(requst,product_id):
       ct=cartlist.objects.get(cart_id=c_id(requst))
       prod=get_object_or_404(prodect, id=product_id)
       c_item=item.objects.get(prodt=prod,cart=ct)
       c_item.delete()
      
       return redirect('cart')
             
               
    




          

     
     
                             



    

