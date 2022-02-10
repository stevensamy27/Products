from msilib.schema import Class
from django import forms 
from .models import Login


#THERE ARE SOME ATTRIBUTES LIKE max_length
#  
#   label
#   initial
#   disabled
#   help_text
#   widget
#   required

class LoginForm(forms.ModelForm):
    class Meta:
        model =Login
        fields = '__all__'
