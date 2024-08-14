from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Profile

class MemberShipForm(forms.ModelForm):
    
    USER_CATEGORIES = [
        ("General_User","일반 유저"),
        ("Business_User","사업자 유저")
    ]

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=USER_CATEGORIES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-size: 16px; width: 300px;'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="내용", widget=forms.Textarea(attrs={
        'rows':5,
        'class': 'form-control',
        'placeholder':'내용을 입력하세요',
    }))
    

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password']
        widgets = {
            'password' : forms.PasswordInput
        }

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match")
        
        validate_password(password)
        return password2
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profile = Profile(user=user, category=self.cleaned_data['category'],address = self.cleaned_data["address"])
            profile.save()
        return user