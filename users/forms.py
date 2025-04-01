from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Введите действующий email")

    class Meta:
        model = CustomUser
        fields = ["username", "phone_number", "gender", "email", "password1", "password2"]
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже зарегистрирован.")
        return email
            