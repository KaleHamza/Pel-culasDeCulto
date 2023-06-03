from django.contrib import admin
from .models import PeliculasDeCulto,Category
# Register your models here.

@admin.register(PeliculasDeCulto)
class PeliculasDeCultoAdmin(admin.ModelAdmin):
    list_display = ("title","slug","category")
    list_display_links=("title","slug")
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title", "isActive", "category")
    read_only_fields = ("slug")
    search_fields = ("title","date")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields = {"slug": ("name",),}