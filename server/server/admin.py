from django.contrib import admin
from .models import User, Dado, Sinal

class SinalAdmin(admin.ModelAdmin):
    readonly_fields = ("hora",)

class DadoAdmin(admin.ModelAdmin):
    readonly_fields = ("visto",)

admin.site.register(User)
admin.site.register(Dado, DadoAdmin)
admin.site.register(Sinal, SinalAdmin)