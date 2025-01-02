from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'core/index.html')

@login_required
def solicitar_brinde(request):
    return render(request, 'core/solicitar_brinde.html')

@login_required
def minhas_solicitacoes(request):
    return render(request, 'core/minhas_solicitacoes.html') 