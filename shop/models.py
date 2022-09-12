from django.db import models
from django.db.models import JSONField
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name='Родительская категория')
    # slug = models.SlugField(unique=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        # unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        # order_with_respect_to='slug'

    category =  TreeForeignKey(Category, blank=True, null=True, related_name='category', verbose_name="Категория", on_delete=models.PROTECT)
    name = models.CharField(max_length=250, verbose_name='Название')
    # slug=models.SlugField(unique=True)
    # image1 = models.ImageField(verbose_name='Главное изображение')
    # image2 = models.ImageField(null=True,blank=True, verbose_name='Изображение 2')
    # image3 = models.ImageField(null=True,blank=True, verbose_name='Изображение 3')
    # image4 = models.ImageField(null=True,blank=True, verbose_name='Изображение 4')
    # image5 = models.ImageField(null=True,blank=True, verbose_name='Изображение 5')
    
    # characteristics = JSONField(blank=True, null=True)
    characteristics = JSONField()
    
    # available = models.BooleanField(default=True)
    # description = models.TextField(verbose_name='Описание товара',null=True)
    # price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')


    def __str__(self):
        return self.name