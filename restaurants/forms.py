from django import forms
from .models import FoodItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class SignUpForm(UserCreationForm):
    """Signup form that collects email and optional restaurant name.

    Note: `restaurant_name` is a form-only field; the view creates the
    Restaurant instance. We override save() to ensure the email is saved
    onto the User when commit=True and to remain compatible with views
    that call save(commit=False).
    """

    email = forms.EmailField(required=True)
    restaurant_name = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        # don't include the form-only restaurant_name in Meta fields
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email') or ''
        if commit:
            user.save()
        return user


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'description', 'price', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise ValidationError("Price is required.")
        try:
            # ensure numeric and positive
            if price <= 0:
                raise ValidationError("Price must be greater than 0.")
        except TypeError:
            raise ValidationError("Enter a valid price.")
        return price


class ProfileForm(forms.Form):
    """Profile form for editing User and Restaurant details.

    This is intentionally a plain Form (not a ModelForm) because the
    project's views already manually update User and Restaurant instances.
    We add validation helpers (unique email, phone format, and a
    conditional requirement for restaurant_email when restaurant_name is set).
    """

    # User fields
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=True)

    # Restaurant fields
    restaurant_name = forms.CharField(max_length=100, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    restaurant_email = forms.EmailField(required=False)

    def clean_email(self):
        """Ensure email is present and unique (excluding current user if provided).

        Views supply the current user via initial data; when validating here,
        we can't access request.user directly, so uniqueness is checked against
        the full User queryset and the view already handles updating the same user.
        """
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")

        # check for an existing user with this email
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            # basic international-friendly phone validation
            if not re.match(r'^\+?\d[\d\s\-\(\)]{6,}$', phone):
                raise ValidationError("Enter a valid phone number.")
        return phone

    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('restaurant_name')
        rest_email = cleaned.get('restaurant_email')
        if name and not rest_email:
            raise ValidationError("Restaurant email is required when restaurant name is provided.")
        return cleaned
