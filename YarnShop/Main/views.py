from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tovar, Category
from users.models import CustomUser
from .forms import TovarForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.messages.views import messages



def lk(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)

    context = {'user_profile': user_profile}
    return render(request, 'Main/LK.html', context)


class TovarDetailView(DetailView):
    model = Tovar
    template_name = 'Main/DVTovar.html'
    context_object_name = 'tovar'


class TovarUpdateView(UpdateView):
    model = Tovar
    success_url = '/catalog'
    template_name = 'Main/Create.html'
    form_class = TovarForm


class TovarDeleteView(DetailView):
    model = Tovar
    success_url = '/catalog'
    template_name = 'Main/Tovar-delete.html'


def index(request):
    return render(request, 'Main/Index.html')


def about(request):
    return render(request, 'Main/About.html')


def catalog(request):
    tovar = Tovar.objects.all()
    return render(request, 'Main/Catalog.html', {'tovar': tovar})


def create(request):
    error = ''
    if request.method == "POST":
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TovarForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'Main/Create.html', data)

