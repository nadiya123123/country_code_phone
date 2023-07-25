from django import forms
from .models import Person
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PersonForm(forms.ModelForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')#default country code setting
    )


    class Meta:
        model=Person
        fields="__all__"