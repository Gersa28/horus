from django.shortcuts import render


import sys
sys.path.append('../../') # esto es necesario para importar lo que sigue

from app.wsgi import *
from core.erp.models import Type
from core.erp.models import Employee

# # Create your views here.
query = Type.objects.all()
print(query)

# # Inserción
# t = Type()
# t.name = 'Ingeniero'
# t.save()

# # Edición
# t = Type.objects.get(id=7)
# t.name = "Accionista_1"
# t.save()
# print(t.name)

## Elimación
# t = Type.objects.get(id=1)
# t.delete()
# query = Type.objects.all()
# print(query)


# # Edición
# try:
#     t = Type.objects.get(id=7)
#     t.name = "Accionista_1"
#     t.save()
#     print(t.name)
# except Exception as e:
#     print("Error:",e)

# obj = Type.objects.filter(name__contains='Pres') # esto distinque mayúsculas de minúsculas
# obj = Type.objects.filter(name__icontains='pres') # esto NO distinque mayúsculas de minúsculas
# obj = Type.objects.filter(name__startswith='P')# esto distinque mayúsculas de minúsculas
# obj = Type.objects.filter(name__istartswith='p')
obj = Type.objects.all().count() # Total de registros
print (obj)

# si queremos el ver el codigo SQL que se ejecuta utilizo la plabra query al final
# obj = Type.objects.filter(name__contains='Pres')
# print (obj)
# obj = Type.objects.filter(name__contains='Pres').query
# print (obj)
# obj = Type.objects.filter(name__endswith='o').exclude(id=5) #Excluir id 5, esto que vamos teniendo son arreglos iterables.
# print (obj)

objt = Employee.objects.filter(type_id=1)

for i in Type.objects.filter(name__endswith='o').exclude(id=5)[:2]: #iterable al cual le pido solo los 2 ultimos elementos
    print (i.name)
