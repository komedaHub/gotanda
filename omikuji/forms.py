from django import forms
from .models import Omikuji

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)

class OmikujiForm(forms.ModelForm):
    class Meta:
        model = Omikuji
        fields = ('name',)
