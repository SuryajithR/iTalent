from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup1', views.signup1, name='signup1'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^up_files', views.up_files, name='up_files'),
    url(r'^file_save', views.file_save, name='file_save'),
    url(r'^view_talents', views.view_talents, name='view_talents'),
    url(r'^comment_save', views.comment_save, name='comment_save'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^rating_save', views.rating_save, name='rating_save'),
    path('contact/<id>', views.contact, name='contact'),
    path('edit/<id>', views.edit, name='edit'),
    path('updateProf/<id>', views.updateProfile, name='updateProf'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^admin', views.admin, name='admin'),
    url(r'^approve', views.approve, name='approve'),
    url(r'^talentview', views.talentview, name='talentview'),
    path('accept/<id>', views.accept, name="accept"),
    path('block/<id>', views.block, name='block'),
    path('delete/<id>', views.deletetalent, name='delete'),
    path('deletet/<id>', views.delete, name='deletet'),
    path('delcom/<id>', views.delcom, name='delcom'),
    path('delcomm/<id>', views.delcomm, name='delcomm'),
    path('tedit', views.tedit, name='tedit'),
    path('editp/<id>', views.editp, name='editp'),
    path('updatep/<id>', views.updatep, name='updatep'),
    path('deletep/<id>', views.deletep, name='deletep'),

]
