from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

#accountapp:hello_world
#"127.0.0.1:8000/account/hello_world"


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), #함수형 베이스는 함수명 바로 넣어주는 형식
    path('create/', AccountCreateView.as_view(), name='create'), #클래스 베이스 뷰 형식
]