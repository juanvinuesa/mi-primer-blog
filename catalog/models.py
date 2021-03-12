from django.db import models




class Autor(models.Model):

    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False,null = False)

    def __str__(self):
        return self.nombre
class Claves(models.Model):


    w = models.CharField(max_length=50)

    def __str__(self):

        return self.w
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13)
    palabras = models.ManyToManyField(Claves)
    def __str__(self):
        return self.titulo



class Sc_Article(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    doi= models.CharField('DOI',max_length=30)
    palabras = models.ManyToManyField(Claves)
    def __str__(self):

        return self.titulo
