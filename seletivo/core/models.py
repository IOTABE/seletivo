from __future__ import unicode_literals
from django.db import models


class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    sigla = models.SlugField(max_length=10)
    fone = models.CharField(max_length=15)
    logotipo = models.ImageField(upload_to=None)
    logomarca = models.ImageField(upload_to=None)

    class Meta:
        verbose_name_plural = "Instituicoes"

    def __str__(self):
        return self.nome


class Curso(models.Model):
    ATIVO = (
        ('S', 'Ativo'),
        ('N', 'Inativo')
    )
    inst = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_inst')
    nome_curso = models.CharField(max_length=80)
    sigla_curso = models.SlugField(max_length=10)
    grau = models.CharField(max_length=30)
    duracao = models.CharField(max_length=30)
    autorizacao = models.CharField(max_length=50)
    situacao = models.CharField(
        max_length=1,
        choices=ATIVO,
        default='N',)

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome_curso


class Seletivos(models.Model):
    inst_seletivo = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    nome_seletivo = models.CharField(max_length=50)
    sigla_seletivo = models.SlugField(max_length=30)

    class Meta:
        verbose_name_plural = "Seletivos"

    def __str__(self):
        return self.nome_seletivo
