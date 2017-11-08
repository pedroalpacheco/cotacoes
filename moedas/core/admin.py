from django.contrib import admin
from .models import  Dolar


class DolarAdmin(admin.ModelAdmin):
    fields = ['data','venda','compra']
    list_display = ['data','venda','compra']
    list_filter = ['data']
    search_fields = ['data']
    save_on_top = True

admin.site.register(Dolar, DolarAdmin)