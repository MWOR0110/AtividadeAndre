from django.db import models

# Definição de um modelo chamado AlunoModel
class AlunoModel(models.Model):
    # Campo para armazenar o nome do aluno com no máximo 50 caracteres
    nome = models.CharField(max_length=50)
    
    # Campo para armazenar o endereço de e-mail do aluno com no máximo 100 caracteres
    e_mail = models.CharField(max_length=100)

    # Método para representação em string do objeto AlunoModel
    def __str__(self) -> str:
        """
        Retorna uma representação em string do objeto AlunoModel.

        Retorna:
            str: Uma string formatada contendo o nome e o e-mail do aluno.
        """
        return "Aluno [%s com o e-mail: %s]" % (self.nome, self.e_mail)
