
from django import forms
from Cart.models import Billing_details
from Cart.models import Shipping_info



class Shipping_infoForm(forms.ModelForm):
    class Meta:
        model=Shipping_info
        fields = (
            'first_name',
            'last_name',
            'company',
            'address',
            'city',
            'country',
            'email',
            'phone',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
        
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control'
            
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),

             'city': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
             'country': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            

            })
        }





class  Billing_detailsForm(forms.ModelForm):
    class Meta:
        model= Billing_details
        fields = (
            'firstname',
            'lastname',
            'company',
            'address',
            'city',
            'country',
            'email',
            'phone',
        )
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control'
        
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control'
            
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),

             'city': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
             'country': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            

            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            

            })
    }