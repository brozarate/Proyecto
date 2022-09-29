from django.db import models

# Create your models here.

# Un modelo es una tabla en la DB y cada uno de los atributos representa un campo en la base de datos

# Un modelo se define con una clase en python. Las clases usan una notación CamelCase

class GerenteDeCuenta(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    email = models.EmailField(max_length = 254, verbose_name='Correo')

    def __str__(self):
        return self.first_name

class Meta:
    verbose_name = 'Gerente de cuenta'
    verbose_name = 'Gerentes de cuenta'
    db_table = 'gerente_de_cuenta'
    ordering = ['id']

class Asesor(models.Model):
    #asesor_id = ['id']
    first_name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    phone = models.IntegerField(verbose_name='Celular')
    email = models.EmailField(max_length = 254, verbose_name='Correo')
    #commission = models.IntegerField(verbose_name='Comisión')
    advisory_status = models.CharField(max_length=10, verbose_name='Estado Asesor')
    GerenteDeCuenta = models.ForeignKey(GerenteDeCuenta, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Meta:
    verbose_name = 'Asesor'
    verbose_name = 'Asesores'
    db_table = 'asesor'
    ordering = ['id']

#objs = [Asesor(first_name=asesor) for asesor in Asesor]
# Asesor.objects.bulk_create(objs)    

elegir_destino = [
    (1, 'Villa de Leyva'),
    (2, 'Lago de Tota'),
    (3, 'Hacienda Napoles'),
    (4, 'Desierto de la Tatacoa'),
    (5, 'Eje Cafetero'),
    (6, 'Medellin y Guatapé'),
    (7, 'Santander'),
    (8, 'Cartagena'),
    (9, 'Guajira'),
    (10, 'San Andres'),
    (11, 'Santa Marta'),
    (12, 'Amazonas'),
    (13, 'Bahía Solano'),
    (14, 'Capurgana'),
    (15, 'Ciudad Perdida'),
    (16, 'Caño Cristales'),
    (17, 'Deportes Extremos Nimaima'),
    (18, 'Nevado del Cocuy'),
    (19, 'Cuatrimotos Villa de Leyva'),
    (20, 'Parapente Villavicencio'),
]

estado_comision = [
    (1, 'Pendiente'),
    (2, 'Pagada'),
    (3, 'Anulada')
]

class Comision(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    Asesor = models.ForeignKey(Asesor, null=False, blank=False, on_delete=models.CASCADE)
    destino = models.IntegerField(null=False, blank=False, choices=elegir_destino)
    total_sale = models.DecimalField(max_digits = 19, decimal_places = 2, verbose_name='Valor venta')
    advisory_commission = models.IntegerField(verbose_name='Comisión')
    commission_to_pay = models.DecimalField(max_digits = 19, decimal_places = 2, verbose_name='Comisión a pagar')
    commission_status = models.IntegerField(null=False, blank=False, choices=estado_comision, default=1, verbose_name='Estado de comisión')
    # estado_comision = models.CharField(max_length=10, verbose_name='Estado de comisión')

    # @property
    # def calculo_comision(self):
    #     return((self.total_sale * self.advisory_commision) * 100)

    # def save(self):
    #     self.commission_to_pay = self.calculo_comision
    #     super(Comision, self).save()

    def __str__(self):
        return str(self.Asesor)          

class Meta:
    verbose_name = 'Comision'
    verbose_name = 'Comisiones'
    db_table = 'comision'
    ordering = ['id']


