
#difinimos la funcion inicio 
# el parametro request es una peticion
#return la peticion y el html
from django.shortcuts import render
def inicio(request):
  return render(request,"inicio.html")