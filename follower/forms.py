from django import forms
from .models import Fallower
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'enter password',
        'class': "form-control",

    }))
    confirm_password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' confirm_password'
        
    }))
    class Meta:
        model=Fallower
        fields=['name', 'surname', 'age','email','password', ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='enter name'
        self.fields['surname'].widget.attrs['placeholder']='enter surname'
        self.fields['email'].widget.attrs['placeholder']='enter name'
        self.fields['age'].widget.attrs['placeholder']='enter age'
        self.fields['password'].widget.attrs['placeholder']='enter password'
        
        for field in self.fields:
            self.fields[field].widget.atters['class']='form-control'     






# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model=Fallower
#         fields=('name', 'surname', 'age','email', )



# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserCreationForm):
#         model=Fallower
#         fields=('name', 'surname', 'age','email', )


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model =Fallower
#         fields=['name', 'surname', 'age','email', 'password'] 