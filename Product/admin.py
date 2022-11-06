from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_format', 'p_type', 'p_kind', 'p_density', 'p_width', 'p_height',  'created_at', 'updated_at', 'is_moved', 'file')
    list_display_links = ('id', 'file')
    search_fields = ['id', 'p_format', 'p_type', 'p_kind', 'p_density', 'p_width', 'p_height', 'created_at',
                     'updated_at', 'is_moved', 'file']
    list_editable = ['is_moved']
    list_filter = ('id', 'p_format', 'p_type', 'p_kind', 'p_density', 'p_width', 'p_height',  'created_at', 'updated_at', 'is_moved', 'file')

admin.site.register(Product, ProductAdmin)

from .models import (PaperKind, PaperType, PaperDensity, PaperWidth, PaperHeight, PaperFormat)
admin.site.register(PaperKind)
admin.site.register(PaperType)
admin.site.register(PaperDensity)
admin.site.register(PaperWidth)
admin.site.register(PaperHeight)
admin.site.register(PaperFormat)
