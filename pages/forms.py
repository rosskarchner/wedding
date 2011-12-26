from models import Song

from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    secret = forms.CharField(max_length=300, label="the bride or grooms last name")
    
    def clean_secret(self):
        secret = self.cleaned_data['secret']
        if secret.lower().strip() not in ['string', 'karchner']:
        	raise forms.ValidationError("That's not right!")
        	
        	

class SongForm(ModelForm):
     class Meta:
         model = Song
         fields = ('title', 'artist', 'comment', 'your_name')