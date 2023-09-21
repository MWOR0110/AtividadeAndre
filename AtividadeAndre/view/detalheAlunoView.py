from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models.alunoModel import AlunoModel
from ..serializer.alunoSerializer import AlunoSerializer

# Definição de uma classe de visualização chamada DetalheAlunoView
class DetalheAlunoView(APIView):

    def existeOuNao(self, pk):
        """
        Verifica se um aluno com a chave primária especificada existe.

        Args:
            pk (int): A chave primária do aluno a ser verificado.

        Returns:
            AlunoModel: O objeto AlunoModel se existir, caso contrário, levanta uma exceção Http404.
        """
        try:
            return AlunoModel.objects.get(pk=pk)
        except AlunoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Implementa a operação GET para buscar detalhes de um aluno específico.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária do aluno a ser consultado.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os detalhes do aluno ou uma mensagem de erro 404.
        """
        aluno = self.existeOuNao(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Implementa a operação PUT para atualizar os detalhes de um aluno específico.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados de atualização do aluno.
            pk (int): A chave primária do aluno a ser atualizado.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados atualizados do aluno ou uma mensagem de erro 400.
        """
        aluno = self.existeOuNao(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Aluno não editado"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Implementa a operação DELETE para excluir um aluno específico.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária do aluno a ser excluído.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP de status 204 indicando que o aluno foi excluído com sucesso.
        """
        aluno = self.existeOuNao(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
