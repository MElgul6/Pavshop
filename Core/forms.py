from django import forms
from Core.models import Contact,Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Enter your email address'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        # fields= '__all__'
        fields = (
            'fullname',
            'email',
            'phone',
            'subject',
            'message'
        )
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows':7
            })
        }