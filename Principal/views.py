from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email,password=password)

            if user is not None and user.is_active:
                login(request,user)
                return redirect('/privado')
            else:
                return HttpResponse('Error de autentificacion')
        else:
            return HttpResponse('El formulario no es valido')
    else:
        form = AuthenticationForm()
    ctx = {'form':form}
    return render(request,'index.html',ctx)

def privado(request):
    if request.user.is_authenticated():
        return HttpResponse('Bienvenido: DNI = %s<br> EMAIL = %s' % (request.user.dni,request.user.email));
    else:
        return redirect('/')