from django.urls import path
from .views import accueil, custom_login,liste_dechets, ajouter_dechet, details_dechet, modifier_dechet,index, supprimer_dechet
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    
    path('login', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('', accueil, name='accueil'),
    path('',index, name='index'),

    path('dechets/', liste_dechets, name='liste_dechets'),
    path('dechets/ajouter/', ajouter_dechet, name='ajouter_dechet'),
    path('dechets/<int:dechet_id>/', details_dechet, name='details_dechet'),
    path('dechets/<int:dechet_id>/modifier/', modifier_dechet, name='modifier_dechet'),
    path('dechets/<int:dechet_id>/supprimer/', supprimer_dechet, name='supprimer_dechet'),
    # path('index', views.application, name='application'),  # La vue 'application' sera associée à la racine de votre site

]
