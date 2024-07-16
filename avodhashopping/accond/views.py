from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth # type: ignore
from django.contrib import messages 

# Create your views here.
def login (request):
   if request.method=='POST':
      
      username=request.POST['username']
      password=request.POST['pass']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.info(request,'invalid credentials')
         return redirect('login')
   else:
      return render (request,'login.html')
      
      
      


      
      
   
def mu(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        Username=request.POST['username']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            
            if User.objects.filter(username=Username).exists():
               messages.info(request,"username alrady taken")
               return redirect('mu')
            elif User.objects.filter(email=email).exists():
             messages.info(request,"email alrady taken")
             return redirect('mu')
            else:
              
                  
             
             user=User.objects.create_user(first_name=firstname,username=Username,email=email,last_name=lastname,password=password)
             user.save()
             print('user creat')
             return redirect('login') 
        return redirect('mu')
    else:
     
     return render(request,'mu.html')
def logout(request):
   auth.logout(request)
   return redirect('/')               
         
    
     
                  
            
    
     

 
          
      
               
        
                      
                    
   
              
              
                
        
         
         
         
        
    

         
         
           
            
                    
              
              
        
          
        
          
        
            
    
           
            
           

            
    

    
    
          

        
             


        
        
             
             
             
           
             
            
        
            

             
             

                

       
    

        
         
        
          

  
         
    
                
 
            
                          

       
                              
    

