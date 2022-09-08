from django.contrib import admin
from .models import Category
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



# https://tretyakov.net/post/drevovidnye-kategorii-v-django/
# from django_mptt_admin.admin import DjangoMpttAdmin
# class CategoryAdmin(DjangoMpttAdmin):
#         pass

# admin.site.register(Category, CategoryAdmin)
