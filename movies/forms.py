from django import forms
from .models import Movie


class MovieFilterForm(forms.Form):
    query = forms.CharField(label="Film Adı", required=False)
    genre = forms.ChoiceField(label="Tür", choices=[('', 'Tüm Türler')] + [(g, g) for g in Movie.objects.values_list('genre', flat=True).distinct()], required=False)
    min_year = forms.IntegerField(label="Başlangıç Yılı", required=False)
    max_year = forms.IntegerField(label="Bitiş Yılı", required=False)
    min_rating = forms.FloatField(label="En Düşük Puan", required=False, min_value=1, max_value=10)
    max_rating = forms.FloatField(label="En Yüksek Puan", required=False, min_value=1, max_value=10)

