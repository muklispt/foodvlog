from django.contrib import admin
from .models import categ, prodect


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(categ, catadmin)


class proadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'img', 'category']
    list_editable = ['price', 'stock', 'img', 'category']
    prepopulated_fields = {'slug': ('name', 'category')}
    ordering = ['name', 'category']
    search_fields = ['name', 'category']
    list_per_page = 20


admin.site.register(prodect, proadmin)
