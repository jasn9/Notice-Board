

from . import views

from django.urls import path

# add name to differentite url in = {% url 'central:index' name %} in template to represent href insted of hardcode
# {% url 'index' name % } have issue that more than one app may have same view.

app_name = 'central'

urlpatterns = [

    path('', views.index, name='index'),
    path('login/',views.user_login, name='user_login'),
    path('detail/<str:username>/',  views.detail , name='detail'),
    path('register/',views.register , name='register'),
    path('adduser/',views.add_user, name='add_user'),
    path('logout/', views.log_out, name='log_out'),
    path('deleteuser/', views.delete_user,name='delete_user'),
    path('update/',views.update,name='update'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create_board/', views.create_board, name='create_board'),
    path('register_board/', views.register_board, name='register_board'),
    path('get_board/<str:board_id>/', views.get_board, name='get_board'),
    path('my_boards/', views.my_boards, name='my_boards'),
    path('game/',views.game, name="game"),
]