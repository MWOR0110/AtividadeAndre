from rest_framework import serializers
from AtividadeAndre.models.alunoModel import AlunoModel

# Definição de um serializador chamado AlunoSerializer
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Metaclasse que define as configurações do serializador.

        Atributos:
            model (class): O modelo de dados associado a este serializador (AlunoModel).
            fields (str or tuple): Especifica quais campos do modelo serão serializados. 
                No caso de '__all__', todos os campos do modelo serão incluídos.
        """
        model = AlunoModel
        fields = '__all__'
