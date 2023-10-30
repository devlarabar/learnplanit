from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms


class CustomSignupForm(forms.Form):
    alphanumeric = RegexValidator(
        r"^[0-9a-zA-Z_]*$", "Only alphanumeric characters are allowed.")
    alphanumeric_and_symbols = RegexValidator(
        r"^[A-Za-z0-9!@#$]*$", "Only alphanumeric characters or symbols !@#$ are allowed.")

    username = forms.CharField(
        label="Username",
        min_length=3,
        max_length=25,
        validators=[alphanumeric]
    )
    password1 = forms.CharField(
        label="Password",
        validators=[alphanumeric_and_symbols],
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirm password",
        validators=[alphanumeric_and_symbols],
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(
        label="Your E-mail Address",
    )

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        username_exists = User.objects.filter(username__iexact=username)
        if username_exists.count():
            raise forms.ValidationError("Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        email_exists = User.objects.filter(email=email)
        if email_exists.count():
            raise forms.ValidationError("E-mail already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"]
        )

        return self.cleaned_data["username"], self.cleaned_data["password1"]
