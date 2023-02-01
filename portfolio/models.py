from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo") #Este campo es obligatorio
    description = models.TextField(verbose_name="Descripción") 
    image = models.ImageField(verbose_name="Imagen",upload_to="projects") 
    link = models.URLField(verbose_name = "Dirección Web",null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") #Este campo se actualiza automaticamente cuando se crea el objeto
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") #Este campo se actualiza automaticamente cuando se actualiza el objeto
    

    class Meta: 
        verbose_name = "Portafolio" # Este campo es para que en el admin se muestre el nombre que queramos
        verbose_name_plural = "Portafolios" 
        ordering = ["-created"] # el guión indica que se ordene de forma descendente sin el guión sería ascendente

    def __str__(self):
        return self.title # Este método es para que cuando se muestre el objeto en el admin se muestre el título