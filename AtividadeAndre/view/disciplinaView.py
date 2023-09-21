from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.disciplinaModel import DisciplinaModel
from ..serializer.disciplinaSerializer import DisciplinaSerializer

# Definição de uma classe de visualização chamada DisciplinaView
class DisciplinaView(APIView):
    """
    Referente a Disciplinas
    """
    def get(self, request, format=None):
        """
        Implementa a operação GET para listar todas as disciplinas.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados de todas as disciplinas.
        """
        disciplina = DisciplinaModel.objects.all()
        serializer = DisciplinaSerializer(disciplina, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Implementa a operação POST para criar uma nova disciplina.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP contendo os dados da nova disciplina.
            format (str, optional): O formato de resposta desejado (por padrão, None).

        Returns:
            Response: Uma resposta HTTP com os dados da nova disciplina criada ou uma mensagem de erro.
        """
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Disciplina não criada"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
