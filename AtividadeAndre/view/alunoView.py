from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.alunoModel import AlunoModel
from ..serializer.alunoSerializer import AlunoSerializer

# Definição de uma classe de visualização chamada AlunoView
class AlunoView(APIView):
    """
    Referente a Alunos
    """
    def get(self, request, format=None):
        """
        Implementa a operação GET para listar todos os alunos.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados de todos os alunos.
        """
        aluno = AlunoModel.objects.all()
        serializer = AlunoSerializer(aluno, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Implementa a operação POST para criar um novo aluno.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados do novo aluno.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados do novo aluno criado ou uma mensagem de erro.
        """
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Aluno não criado"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
