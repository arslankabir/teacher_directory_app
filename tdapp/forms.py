from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.core import validators
from django.contrib import messages

def check_subj_length(value):
    if len(value)>5:
        raise forms.ValidationError("You can teach only 5 Subjects")
        

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    # email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    OPTIONS = (
        ("Mathematics", "Mathematics"),
        ("English", "English"),
        ("Computer Science", "Computer Science"),
        ("Biology", "Biology"),
        ("Chemistry", "Chemistry"),
        ("Physics", "Physics"),
        ("Geography", "Geography"),
        ("History", "History"),
        ("Arabic", "Arabic"),
        ("Linear Algebra", "Linear Algebra"),
    )
    subject_taught = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS,
                                          validators=[check_subj_length])
    
    
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','phone_number','room_number','subject_taught')
