from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.tarefaModel import TarefaModel
from ..serializer.tarefaSerializer import TarefaSerializer

# Definição de uma classe de visualização chamada TarefaView
class TarefaView(APIView):
    """
    Referente a Tarefas
    """
    def get(self, request, format=None):
        """
        Implementa a operação GET para listar todas as tarefas.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados de todas as tarefas.
        """
        tarefas = TarefaModel.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Implementa a operação POST para criar uma nova tarefa.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados da nova tarefa.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados da nova tarefa criada ou uma mensagem de erro.
        """
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
