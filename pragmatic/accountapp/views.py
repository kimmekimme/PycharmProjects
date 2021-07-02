from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld() #객체생성
        new_hello_world.text = temp
        new_hello_world.save() #객체 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world')) #루트/파일명
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})  # 루트/파일명

class AccountCreateView(CreateView):
    model = User #User: 장고제공 클래스
    form_class = UserCreationForm #장고제공 클래스
    success_url = reverse_lazy('accountapp:hello_world') #장고제공 함수(클래스형)
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'


class AccountUpdateView(UpdateView):
    model = User #User: 장고제공 클래스
    form_class = AccountUpdateForm #장고제공 클래스
    success_url = reverse_lazy('accountapp:hello_world') #장고제공 함수(클래스형)
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'