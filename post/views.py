from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserForm, NeuForm, ManForm, EleForm
from .models import electricas, manuales, neumaticas

#---------------------------------------------------------------

class HomePageView(ListView):
	model = electricas
	template_name = 'home.html'
	context_object_name = 'docs_list'

class ProductosPageView(ListView):
	model = manuales
	template_name = 'productos.html'
	context_object_name = 'docs_list'

class ElectricasPageView(ListView):
	model = neumaticas
	template_name = 'electricas.html'
	context_object_name = 'docs_list'

class NeumaticasPageView(ListView):
	model = electricas
	template_name = 'neumaticas.html'
	context_object_name = 'docs_list'


class AcercaPageView(ListView):
	model = electricas
	template_name = 'acercade.html'
	context_object_name = 'docs_list'

#---------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = electricas
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

#---------------------------------------------------------------

def agregarMan (request):
	data = {
		'form':ManForm()
	}

	if request.method == 'POST':
		formulario = ManForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='productos')
		else:
			data['form'] = formulario

	return render(request, 'agregarMan.html',data)


def modificarMan (request, id):

	Man = get_object_or_404(manuales, id=id)

	data = {
		'form': ManForm(instance=Man)
	}

	if request.method == 'POST':
		formulario = ManForm(data=request.POST, instance=Man)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='productos')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

def eliminarMan (request, id):
	Man = get_object_or_404(manuales, id=id)
	Man.delete()

	return redirect(to = "productos")

#---------------------------------------------------------------

def agregarEle (request):
	data = {
		'form':EleForm()
	}

	if request.method == 'POST':
		formulario = EleForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='electricas')
		else:
			data['form'] = formulario

	return render(request, 'agregarEle.html',data)


def modificarEle (request, id):

	Ele = get_object_or_404(electricas, id=id)

	data = {
		'form': EleForm(instance=Ele)
	}

	if request.method == 'POST':
		formulario = EleForm(data=request.POST, instance=Ele)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='electricas')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

def eliminarEle (request, id):
	Ele = get_object_or_404(electricas, id=id)
	Ele.delete()

	return redirect(to = "electricas")


#---------------------------------------------------------------

def agregarNeu (request):
	data = {
		'form':NeuForm()
	}

	if request.method == 'POST':
		formulario = NeuForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='neumaticas')
		else:
			data['form'] = formulario

	return render(request, 'agregarNeu.html',data)


def modificarNeu (request, id):

	Neu = get_object_or_404(neumaticas, id=id)

	data = {
		'form': NeuForm(instance=Neu)
	}

	if request.method == 'POST':
		formulario = NeuForm(data=request.POST, instance=Neu)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='neumaticas')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

def eliminarNeu (request, id):
	Neu = get_object_or_404(neumaticas, id=id)
	Neu.delete()

	return redirect(to = "neumaticas")
