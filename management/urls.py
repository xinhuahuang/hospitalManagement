from django.conf.urls import url
from . import views
from handler import *

urlpatterns = [
    url(r'^$', backend, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^set_password/$', views.set_password, name='set_password'),
    # url(r'^add_book00/$', views.add_book00, name='add_book00'),
    url(r'^new_page', views.new_page),
    url(r'^add_book/$', views.add_book),
    # url(r'^add_book2/$', views.add_book2, name='add_book2'),
    # url(r'^add_book3/$', views.add_book3, name='add_book3'),
    # url(r'^add_book4/$', views.add_book4, name='add_book4'),
    # url(r'^add_book5/$', views.add_book5, name='add_book5'),
    # url(r'^add_book6/$', views.add_book6, name='add_book6'),
    # url(r'^add_book7/$', views.add_book7, name='add_book7'),
    # url(r'^add_book8/$', views.add_book8, name='add_book8'),
    # url(r'^add_book9/$', views.add_book9, name='add_book9'),
    # url(r'^add_img/$', views.add_img, name='add_img'),
    # url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    # url(r'^view_book/detail/$', views.detail, name='detail'),
    url(r'^backend/$',backend),
    url(r'^show_ssd',show_ssd),
    url(r'^edit_ssd',get_ssd_by_id),
    url(r'^delete_ssd/$',delete_ssd),
    url(r'^save_ssd/$',save_ssd)
]
