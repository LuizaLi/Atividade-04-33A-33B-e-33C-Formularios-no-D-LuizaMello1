from django.shortcuts import render, redirect
from .models import Vantagens, Desvantagens, Tabela

# Create your views here.
def home(request):
  vant = Vantagens.objects.all()
  desvant = Desvantagens.objects.all()
  tabe = Tabela.objects.all()
  return render(request, "home.html",context={
    "vantagens":vant,
    "desvantagens":desvant,
    "tabelas":tabe})

def create_vantagem(request):
  if request.method == "POST":
    Vantagens.objects.create(
      title = request.POST["title"],
      argumento = request.POST["argumento"],
      vanttrabalho = request.POST["vanttrabalho"],
      vantlazer = request.POST["vantlazer"],
    )
    return redirect("home")
  return render(request,"forms.html", context={"action": "Adicionar"})

def update_vantagem(request, id):
  vant = Vantagens.objects.get(id = id)
  if request.method == "POST":
      vant.title = request.POST["title"]
      vant.argumento = request.POST["argumento"]
      vant.vanttrabalho = request.POST["vanttrabalho"]
      vant.vantlazer = request.POST["vantlazer"]
      vant.save()
    
      return redirect("home")
  return render(request,"forms.html", context={"action": "Atualizar","vant":vant})

def delete_vantagem(request, id):
  vant = Vantagens.objects.get(id = id)
  if request.method == "POST":
      if "confirm" in request.POST:
        vant.delete()
    
      return redirect("home")
  return render(request,"areyousure.html", context={"action": "Deletar","vant":vant})

def create_desvantagem(request):
  if request.method == "POST":
    Desvantagens.objects.create(
      title = request.POST["title"],
      argumento = request.POST["argumento"],
      desvpessoais = request.POST["desvpessoais"],
      desvtrabalho = request.POST["desvtrabalho"],
    )
    return redirect("home")
  return render(request,"forms2.html", context={"action": "Adicionar"})

def update_desvantagem(request, id):
  desv = Desvantagens.objects.get(id = id)
  if request.method == "POST":
      desv.title = request.POST["title"]
      desv.argumento = request.POST["argumento"]
      desv.desvpessoais = request.POST["desvpessoais"]
      desv.desvtrabalho = request.POST["desvtrabalho"]
      desv.save()
    
      return redirect("home")
  return render(request,"forms2.html", context={"action": "Atualizar","desv":desv})

def delete_desvantagem(request, id):
  desv = Desvantagens.objects.get(id = id)
  if request.method == "POST":
      if "confirm" in request.POST:
        desv.delete()
    
      return redirect("home")
  return render(request,"areyousure2.html", context={"action": "Deletar","desv":desv})