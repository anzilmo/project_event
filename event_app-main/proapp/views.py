from urllib import request
from django.shortcuts import render ,redirect
from . models import Event
from .forms import BookingForm 

# Create your views here. 
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def booking(request):
     if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home page or another appropriate page
     else:
        form = BookingForm()
     return render(request, 'booking.html', {'form': form})
def eventes(request):
    dict_eve={
        'eve':Event.objects.all()
    }

    return render(request,'eventes.html',dict_eve)



from .forms import BookingForm  # Correct import

    
