from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.alunoModel import AlunoModel
from ..models.tarefaModel import TarefaModel
from ..serializer.tarefaSerializer import TarefaSerializer

# Definição de uma classe de visualização chamada ListaTarefasAluno
class ListaTarefasAluno(APIView):
    def get(self, request, pk, format=None):
        """
        Implementa a operação GET para listar todas as tarefas de um aluno específico.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            pk (int): A chave primária do aluno a ser consultado.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados das tarefas do aluno ou uma mensagem de erro.
        """
        try:
            # Tentar encontrar um aluno com a chave primária especificada
            aluno = AlunoModel.objects.get(pk=pk)
        except AlunoModel.DoesNotExist:
            # Se o aluno não for encontrado, retornar uma resposta de erro 404
            return Response({"message": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # Filtrar as tarefas associadas ao aluno
        tarefas = TarefaModel.objects.filter(aluno=aluno)
        
        # Serializar os dados das tarefas
        serializer = TarefaSerializer(tarefas, many=True)
        
        # Retornar uma resposta HTTP com os dados serializados das tarefas
        return Response(serializer.data)
