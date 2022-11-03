from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'is_moved', 'file')



admin.site.register(Product, ProductAdmin)

from .models import PaperKind

admin.site.register(PaperKind)

from .models import PaperType

admin.site.register(PaperType)

from .models import PaperDensity

admin.site.register(PaperDensity)

from .models import PaperWidth

admin.site.register(PaperWidth)

from .models import PaperHeight

admin.site.register(PaperHeight)

from .models import PaperFormat

admin.site.register(PaperFormat)
