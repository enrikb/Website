from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Inseration


class InsertionForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Inseration
        fields = ('title', 'description', 'category', 'subcategory', 'size', 'images')


class InsertionUpdateForm(forms.ModelForm):

    class Meta:
        model = Inseration
        fields = ('title', 'description', 'category',  'subcategory', 'size', 'images')

    def remove_insertion(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Inseration.objects.exclude(pk=self.instance.pk).get(email=email)
            except Inseration.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)