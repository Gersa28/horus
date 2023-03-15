from django.db import models
from datetime import datetime

# Create your models here.
# En DJANGO cuando creamos tablas por defecto se va a crear la columna 'id' como PK, no es necesario declararla-

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    verbose_name= 'Categoria'
    verbose_name_plural = 'Categorias'
    # db_table = 'tipo'
    ordering = ['id']

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']



class Employee(models.Model): #Aplicamos herencia y heredamos de la clase models
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE) #esta función me relaciona esta clase con la clase Type
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default='django.utils.timezone.now()', verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    satate = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True) # los archivos e imagenes se van a guardar en la carpeta avatar 
    cvitae = models.ImageField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
