from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from articleapp.views import ArticleListView

app_name = "accountapp"

#accountapp:hello_world
#"127.0.0.1:8000/account/hello_world"


urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),   #클래스 베이스 뷰 형식
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), #로그인은 템플릿 지정
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]