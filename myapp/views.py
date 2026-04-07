from django.shortcuts import render, HttpResponse
from .models import Contact
from django.shortcuts import redirect


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
   if request.method == 'POST':
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       email = request.POST.get('email')
       msg = request.POST.get('msg')
       c = Contact(name=name, phone=phone, email=email, msg=msg)
       c.save()
       return redirect('/contact')
   data = Contact.objects.all()

   return render(request, 'contact.html', {'data': data})

def product(request):
    return render(request, 'product.html')
