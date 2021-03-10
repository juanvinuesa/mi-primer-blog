from django.db import models





class Sc_Article(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, help_text="Ingrese el nombre del autor del articulo")
    doi= models.CharField('DOI',max_length=30)
    def __str__(self):

        return self.titulo

class Autor(models.Model):

    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False,null = False)

    def __str__(self):
        return self.nombre
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)

    def __str__(self):
        return self.titulo



