from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Pergunta, Alternativa

def index(request):
    # SELECT * FROM Pergunta ORDER BY data_publicacao DESC LIMIT 5
    lista_perguntas_mais_recentes = Pergunta.objects.order_by("-data_publicacao")[:5]
    context = {"lista_perguntas_mais_recentes": lista_perguntas_mais_recentes}
    return render(request, "polls/index.html", context)



def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "polls/detalhe.html", {"pergunta": pergunta})


def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "polls/resultados.html", {'pergunta': pergunta})


def votar(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        alternativa_selecionada = pergunta.alternativa_set.get(pk=request.POST["alternativa"])
    except (KeyError, Alternativa.DoesNotExist):
        # Exibir novamente o formulário de votação
        return render(
            request,
            "polls/detalhe.html",
            {
                "pergunta": pergunta,
                "error_message": "Você não selecionou uma alternativa.",
            },
        )
    else:
        alternativa_selecionada.votos = F("votos") + 1
        alternativa_selecionada.save()
        return HttpResponseRedirect(reverse("polls:resultados", args=(pergunta.id,)))


