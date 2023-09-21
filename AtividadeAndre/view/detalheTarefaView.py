from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models.tarefaModel import TarefaModel
from ..serializer.tarefaSerializer import TarefaSerializer

# Definição de uma classe de visualização chamada DetalheTarefaView
class DetalheTarefaView(APIView):

    def existeOuNao(self, pk):
        """
        Verifica se uma tarefa com a chave primária especificada existe.

        Args:
            pk (int): A chave primária da tarefa a ser verificada.

        Returns:
            TarefaModel: O objeto TarefaModel se existir, caso contrário, levanta uma exceção Http404.
        """
        try:
            return TarefaModel.objects.get(pk=pk)
        except TarefaModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Implementa a operação GET para buscar detalhes de uma tarefa específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária da tarefa a ser consultada.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os detalhes da tarefa ou uma mensagem de erro 404.
        """
        tarefa = self.existeOuNao(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Implementa a operação PUT para atualizar os detalhes de uma tarefa específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados de atualização da tarefa.
            pk (int): A chave primária da tarefa a ser atualizada.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados atualizados da tarefa ou uma mensagem de erro 400.
        """
        tarefa = self.existeOuNao(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Tarefa não editada"}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Implementa a operação DELETE para excluir uma tarefa específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária da tarefa a ser excluída.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP de status 204 indicando que a tarefa foi excluída com sucesso.
        """
        tarefa = self.existeOuNao(pk)
        tarefa.delete()
        return Response({"message": "Tarefa excluída"}, status=status.HTTP_204_NO_CONTENT)
