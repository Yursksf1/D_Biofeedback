from django.contrib import admin
from .models import Paciente, HistoriaMedica, Terapia
# Register your models here.
admin.site.register(Paciente)
admin.site.register(HistoriaMedica)
admin.site.register(Terapia)