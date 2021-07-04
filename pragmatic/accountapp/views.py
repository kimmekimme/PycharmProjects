from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from accountapp.decorators import account_ownership_required
from articleapp.models import Article
from projectapp.views import ProjectDetailView

has_ownership = [
    account_ownership_required,
    login_required
]


@login_required  # 데코레이터
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  # 객체생성
        new_hello_world.text = temp
        new_hello_world.save()  # 객체 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # 루트/파일명
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})  # 루트/파일명


class AccountCreateView(CreateView):
    model = User  # User: 장고제공 클래스
    form_class = UserCreationForm  # 장고제공 클래스
    success_url = reverse_lazy('accountapp:hello_world')  # 장고제공 함수(클래스형)
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')  # 일반 fuction에 사용할수있는 데코레이터를 class메서드에 사용할수 있게 변환해주는 어노테이션
class AccountUpdateView(UpdateView):
    model = User  # User: 장고제공 클래스
    form_class = AccountUpdateForm  # 장고제공 클래스
    success_url = reverse_lazy('accountapp:hello_world')  # 장고제공 함수(클래스형)
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'

    # 인증구현
