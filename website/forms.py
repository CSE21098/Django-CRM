from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    name = forms.CharField(label="",max_length="30", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><li>At least 8 characters</li><li>Contains a number</li><li>Contains a symbol</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text ='<span class="form-text text-muted"><li>Enter the same password as before, for verification.</li></span>'
        
class RecordForm(forms.ModelForm):
    name = forms.CharField(label="",max_length="30", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    phone = forms.CharField(label="",max_length="10", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    address = forms.CharField(label="",max_length="200", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    zipcode = forms.CharField(label="",max_length="6", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}))



    class Meta:
        model = Record
        # fields = ['name', 'phone', 'email', 'address', 'zipcode']
        exclude = ('user',)
    