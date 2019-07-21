

from . import views

from django.urls import path

# add name to differentite url in = {% url 'central:index' name %} in template to represent href insted of hardcode
# {% url 'index' name % } have issue that more than one app may have same view.

app_name = 'central'

urlpatterns = [

    path('', views.index, name='index'),
    path('login/',views.user_login, name="user_login"),
    path('detail/<str:username>/',  views.detail , name='detail'),
    path('register/',views.register , name="register"),
    path('adduser/',views.add_user, name="add_user"),
    path('logout/', views.log_out, name="log_out"),
    path('deleteuser/', views.delete_user,name="delete_user"),
    path('update/',views.update,name="update"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('game/',views.game, name="game"),
]