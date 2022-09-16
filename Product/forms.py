from dataclasses import field
from tkinter import Widget
from django import forms
from Product.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = (
            'review_text',
            'rating'
        )
        widgets = {
            'review_text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            # 'rating': forms.IntegerField(attrs={
            #     'class': 'rating'
            # }),
           
        }
  
