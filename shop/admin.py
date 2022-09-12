from django.contrib import admin
from .models import Category, Product
from mptt.admin import DraggableMPTTAdmin


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

# admin.site.register(Product)
from flat_json_widget.widgets import FlatJsonWidget
from django.db.models import JSONField


class JsonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    JSONField: {'widget': FlatJsonWidget }
  }

admin.site.register(Product, JsonAdmin)


# https://tretyakov.net/post/drevovidnye-kategorii-v-django/
# from django_mptt_admin.admin import DjangoMpttAdmin
# class CategoryAdmin(DjangoMpttAdmin):
#         pass

# admin.site.register(Category, CategoryAdmin)
