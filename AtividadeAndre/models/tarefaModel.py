from django.db import models
from AtividadeAndre.models.alunoModel import AlunoModel
from AtividadeAndre.models.disciplinaModel import DisciplinaModel

class TarefaModel(models.Model):
    aluno = models.ForeignKey(AlunoModel, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricão = models.CharField(max_length=255)
    data_entrega = models.CharField(max_length=10)
    concluido = models.BooleanField()
    disciplina = models.ManyToManyField(DisciplinaModel,blank=True, related_name='tags', through='DisciplinaTarefaModel')




    def __str__(self) -> str:
        return "Tarefa [%s - %s - %s - %r]" % (self.titulo, self.descricão, self.data_entrega, self.concluido)