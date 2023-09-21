from rest_framework import serializers
from AtividadeAndre.models.disciplinaTarefaModel import DisciplinaTarefaModel

# Definição de um serializador chamado DisciplinaTarefaSerializer
class DisciplinaTarefaSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Metaclasse que define as configurações do serializador.

        Atributos:
            model (class): O modelo de dados associado a este serializador (DisciplinaTarefaModel).
            fields (str or tuple): Especifica quais campos do modelo serão serializados. 
                No caso de '__all__', todos os campos do modelo serão incluídos.
        """
        model = DisciplinaTarefaModel
        fields = '__all__'
