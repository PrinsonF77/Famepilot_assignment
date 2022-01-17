from django import forms
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class RegisterForm(forms.ModelForm):

    cur_year = datetime.datetime.today().year
    year_range = tuple([i for i in range(cur_year, cur_year - 120,-1)])

    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email','style': 'width:100%', 'class':'input_field'}))
    password    = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder' : 'Password','style': 'width:100%', 'class':'input_field'}))
    password2   = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','style': 'width:100%', 'class':'input_field'}))
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years = year_range,attrs={'class':'input_field'}))
    name = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder':'Full Name','style': 'width:100%', 'class':'input_field'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder':'Phone Number','style': 'width:100%', 'class':'input_field'}))

    class Meta:
        model = User
        fields = ("email","password","password2","date_of_birth","name","phone")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password']
        )
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        
        return user

class LoginForm(forms.Form):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width:100%', 'class':'input_field'}))
    password    = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style': 'width:100%', 'class':'input_field'}))

