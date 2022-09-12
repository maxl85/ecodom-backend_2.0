from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Category


# class CategorySerializer(serializers.ModelSerializer):
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    children = RecursiveField(many=True, label='Children')
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['url', 'id', 'name', 'level', 'parent', 'children']