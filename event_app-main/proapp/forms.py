
from django import forms
from .models import Booking  
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'

        widgets={
            'bookig_date':DateInput(),
        }

        labels={
            'cus_name':"Your Name :",
            'cus_ph':"Your Phone Numbar:",
            'name':"Wihc Event:",
            'booking_date':"Event Date:",
        }

