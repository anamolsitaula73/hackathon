# venues/forms.py
from django.contrib.auth.models import User
from .models import VenueOwner
from .models import Venue, PricingPackage
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Venue, PricingPackage
from django.contrib.auth import get_user_model
# venues/forms.py
from .models import Booking

# forms.py
# venues/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import VenueOwner, Venue, PricingPackage

class VenueOwnerSignUpForm(UserCreationForm):
    business_registration_number = forms.CharField(max_length=100)
    business_registration_photo = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'business_registration_number', 'business_registration_photo']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PricingPackageForm(forms.ModelForm):
    class Meta:
        model = PricingPackage
        fields = ['package_name', 'price', 'details', 'contact_email']
        widgets = {
            'contact_email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        initial_email = kwargs.pop('initial_email', None)
        super().__init__(*args, **kwargs)

        if initial_email:
            self.fields['contact_email'].initial = initial_email
            self.fields['contact_email'].widget.attrs['readonly'] = True
            self.fields['contact_email'].widget.attrs['disabled'] = True

        self.fields['contact_email'].widget.attrs['class'] = 'form-control'
        self.fields['package_name'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['details'].widget.attrs['class'] = 'form-control'

# venues/forms.py



from django import forms
from .models import Venue

class VenueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(VenueForm, self).__init__(*args, **kwargs)
        
        # Set initial value and disable field if user is authenticated
        if user and user.is_authenticated:
            self.fields['contact_email'].initial = user.email
            self.fields['contact_email'].widget.attrs['readonly'] = True
        
        # Add CSS classes to fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = Venue
        fields = ['name', 'address', 'description', 'contact_email', 'contact_num', 'zip_code', 'average_cost_per_person', 'occupancy', 'total_slots', 'image']

       
class VenueImageForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 3 * 1024 * 1024:
                raise forms.ValidationError("Image file size should not exceed 3 MB.")
        return image


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_guests', 'contact_email']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'contact_email': forms.EmailInput(attrs={'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        user_email = kwargs.pop('user_email', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if user_email:
            self.fields['contact_email'].initial = user_email


