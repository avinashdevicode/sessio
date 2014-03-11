'''
Created on Mar 11, 2014

@author: avinash
'''

from django import forms
from .models import products

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = products
        fields = ('product_name','product_description','product_photo')