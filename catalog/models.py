from django.db import models





class Sc_Article(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, help_text="Ingrese el nombre del autor del articulo")
    doi= models.CharField('DOI',max_length=30)
    def __str__(self):

        return self.titulo

class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")
    segundo=models.CharField(max_length=200)
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name


