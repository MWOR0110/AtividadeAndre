from rest_framework import serializers
from AtividadeAndre.models.tarefaModel import TarefaModel

# Definição de um serializador chamado TarefaSerializer
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Metaclasse que define as configurações do serializador.

        Atributos:
            model (class): O modelo de dados associado a este serializador (TarefaModel).
            fields (str or tuple): Especifica quais campos do modelo serão serializados. 
                No caso de '__all__', todos os campos do modelo serão incluídos.
        """
        model = TarefaModel
        fields = '__all__'
