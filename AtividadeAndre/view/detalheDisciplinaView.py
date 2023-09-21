from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models.disciplinaModel import DisciplinaModel
from ..serializer.disciplinaSerializer import DisciplinaSerializer

# Definição de uma classe de visualização chamada DetalheDisciplinaView
class DetalheDisciplinaView(APIView):

    def existeOuNao(self, pk):
        """
        Verifica se uma disciplina com a chave primária especificada existe.

        Args:
            pk (int): A chave primária da disciplina a ser verificada.

        Returns:
            DisciplinaModel: O objeto DisciplinaModel se existir, caso contrário, levanta uma exceção Http404.
        """
        try:
            return DisciplinaModel.objects.get(pk=pk)
        except DisciplinaModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Implementa a operação GET para buscar detalhes de uma disciplina específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária da disciplina a ser consultada.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os detalhes da disciplina ou uma mensagem de erro 404.
        """
        disciplina = self.existeOuNao(pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Implementa a operação PUT para atualizar os detalhes de uma disciplina específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados de atualização da disciplina.
            pk (int): A chave primária da disciplina a ser atualizada.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados atualizados da disciplina ou uma mensagem de erro 400.
        """
        disciplina = self.existeOuNao(pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Aluno não editada"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Implementa a operação DELETE para excluir uma disciplina específica.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária da disciplina a ser excluída.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP de status 204 indicando que a disciplina foi excluída com sucesso.
        """
        disciplina = self.existeOuNao(pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
