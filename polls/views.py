from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Pergunta

def index(request):
    # SELECT * FROM Pergunta ORDER BY data_publicacao DESC LIMIT 5
    lista_perguntas_mais_recentes = Pergunta.objects.order_by("-data_publicacao")[:5]
    context = {"lista_perguntas_mais_recentes": lista_perguntas_mais_recentes}
    return render(request, "polls/index.html", context)



def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "polls/detalhe.html", {"pergunta": pergunta})


def resultados(request, pergunta_id):
    response = f"Você está buscando os resultados da pergunta {pergunta_id}"
    return HttpResponse(response)

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")

