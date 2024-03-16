from django import forms
from .models import Dechets

class DechetForm(forms.ModelForm):
    class Meta:
        model = Dechets
        fields = ['Type_dechet', 'Description', 'Date_ajout', 'Etat']
class ImageUploadForm(forms.Form):
    image = forms.ImageField()