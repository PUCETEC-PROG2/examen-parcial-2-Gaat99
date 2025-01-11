from django.db import models

class Movie(models.Model):
    
    name_movie = models.CharField(max_length=100, null=False)  
    genre = models.CharField(max_length=50, null=False)  
    director = models.CharField(max_length=50, null=False)  
    release_date = models.DateField(null=True, blank=True) 
    synopsis = models.TextField(null=False)  

    def __str__(self):
        return f"{self.name_movie} ({self.release_date.year})"