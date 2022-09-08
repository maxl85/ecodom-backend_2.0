from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name='Родительская категория')
    # slug = models.SlugField()
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        # unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name