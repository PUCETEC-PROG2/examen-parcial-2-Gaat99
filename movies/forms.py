from django import forms 
from movies.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'  
        labels = {
            'name_movie': 'Nombre', 
            'genre': 'Género',      
            'director': 'Director',
            'release_date': 'Fecha',  
            'synopsis': 'Sinopsis',   
        }