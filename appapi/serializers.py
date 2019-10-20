from rest_framework import serializers
from .models import todo
class todoserializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'title',
            'description'
        )
        model=todo