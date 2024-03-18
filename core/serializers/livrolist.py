from rest_framework.serializers import ModelSerializer

from core.models import Livro 

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco"]