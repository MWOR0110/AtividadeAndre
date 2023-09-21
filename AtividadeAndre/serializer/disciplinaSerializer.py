from rest_framework import serializers
from AtividadeAndre.models.disciplinaModel import DisciplinaModel

# Definição de um serializador chamado DisciplinaSerializer
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Metaclasse que define as configurações do serializador.

        Atributos:
            model (class): O modelo de dados associado a este serializador (DisciplinaModel).
            fields (str or tuple): Especifica quais campos do modelo serão serializados. 
                No caso de '__all__', todos os campos do modelo serão incluídos.
        """
        model = DisciplinaModel
        fields = '__all__'
