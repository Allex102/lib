from django.contrib import admin
from core.models import *


@admin.register(Readers, Outs, Authors)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True

