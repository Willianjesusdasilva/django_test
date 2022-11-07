from django import forms
from .models import client

class formularioCadastro(forms.ModelForm):
    class Meta:
        model = client
        fields = ('name','email','cellphone')