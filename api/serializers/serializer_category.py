from rest_framework import serializers

from api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'age', 'genre', 'importation_file_name')

