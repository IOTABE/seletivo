from django.contrib import admin
# Register your models here.
from django.forms import TextInput, ModelForm, Textarea, Select
from suit.admin import SortableTabularInline, SortableModelAdmin
from .models import Instituicao, Curso, Seletivos


class CursoInlineForm(ModelForm):
    class Meta:
        widgets = {
            'nome_curso':  TextInput(attrs={'class': 'input-medium'}),
            'sigla': TextInput(attrs={'class': 'input-medium'}),
            'grau': TextInput(attrs={'class': 'input-mini'}),
            'duracao': TextInput(attrs={'class': 'input-mini'}),
            'autorizacao': TextInput(attrs={'class': 'input-mini'}),
            'situacao': TextInput(attrs={'class': 'input-mini'}),
        }


class CursoInline(SortableTabularInline):
    form = CursoInlineForm
    model = Curso
    fields = ('nome_curso', 'sigla_curso', 'grau', 'duracao', 'autorizacao', 'situacao')
    extra = 0
    verbose_name_plural = 'Cursos'
    sortable = 'nome_curso'
#    suit_classes = 'suit-tab suit-tab-cursos'


class SeletivoInlineForm(ModelForm):
    class Meta:
        widgets = {
            'nome_seletivo':  TextInput(attrs={'class': 'input-medium'}),
            'sigla_seletivo': TextInput(attrs={'class': 'input-medium'}),
        }


class SeletivoInline(SortableTabularInline):
    form = SeletivoInlineForm
    model = Seletivos
    fields = ('nome_seletivo', 'sigla_seletivo')
    extra = 0
    verbose_name_plural = 'Seletivos'
    sortable = 'sigla_seletivo'
#    suit_classes = 'suit-tab suit-tab-cursos'


class InstituicaoForm(ModelForm):
    class Meta:
        widgets = {
            'nome': TextInput(attrs={'class': 'input-medium'}),
            'endereco': Textarea(),
            'sigla': TextInput(attrs={'class': 'input-mini'}),
            'fone': TextInput(attrs={'class': 'input-medium'}),
            'logotipo': TextInput(attrs={'class': 'input-medium'}),
            'logomarca': TextInput(attrs={'class': 'input-medium'}),
            }


class InstituicaoAdmin(SortableModelAdmin):
        form = InstituicaoForm
        search_fields = ('nome',)
        list_display = ('nome', 'endereco', 'sigla', 'fone', 'logotipo', 'logomarca')
        inlines = (CursoInline, SeletivoInline,)
        sortable = 'nome'

        fieldsets = [
            (None, {
                'classes': ('suit-tab suit-tab-general',),
                'fields': ['nome', 'endereco', 'sigla', 'fone', 'logotipo', 'logomarca']
                 }),
            ]

        suit_form_tabs = (('general', 'Instituicao'), ('cursos', 'Cursos'), ('seletivos', 'Seletivos'))


admin.site.register(Instituicao, InstituicaoAdmin)
