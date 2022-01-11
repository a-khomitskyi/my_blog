from django import forms
from django.core.exceptions import ValidationError

import re


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, label='Your name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=320, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=12, label='Phone', required=False, help_text='You phone must be ukrainian',
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', help_text='Enter your message here', widget=forms.Textarea(attrs={
        'class': 'form-control', 'cols': 30, 'rows': 7}))

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-_]{0,}\.[a-z|A-Z]{2,}]{,254}$"
        if re.match(pattern, email):
            return email
        raise ValidationError('Not valid E-mail address')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'[a-zA-Z]', name):
            raise ValidationError('Enter your real name (not nic)')
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r"[380|0][\d]{9}"
        if re.match(pattern, phone):
            return phone
        raise ValidationError('Not valid phone number')
