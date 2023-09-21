from django.db import models

# Definição de um modelo chamado DisciplinaModel
class DisciplinaModel(models.Model):
    # Campo para armazenar o nome da disciplina com no máximo 50 caracteres
    nome = models.CharField(max_length=50)
    
    # Campo para armazenar a descrição da disciplina com no máximo 255 caracteres
    descricao = models.CharField(max_length=255)

    # Método para representação em string do objeto DisciplinaModel
    def __str__(self) -> str:
        """
        Retorna uma representação em string do objeto DisciplinaModel.

        Retorna:
            str: Uma string formatada contendo o nome e a descrição da disciplina.
        """
        return "Disciplina [%s é %s]" % (self.nome, self.descricao)
