# views.py
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def my_login_view(request):
    # Logique pour gérer la vue de connexion
    return auth_views.LoginView.as_view()(request)

def my_logout_view(request):
    # Logique pour gérer la vue de déconnexion
    return auth_views.LogoutView.as_view()(request)

def my_password_change_view(request):
    # Logique pour gérer la vue de changement de mot de passe
    return auth_views.PasswordChangeView.as_view()(request)

def my_password_change_done_view(request):
    # Logique pour gérer la vue de confirmation de changement de mot de passe
    return auth_views.PasswordChangeDoneView.as_view()(request)

def my_password_reset_view(request):
    # Logique pour gérer la vue de réinitialisation de mot de passe
    return auth_views.PasswordResetView.as_view()(request)

def my_password_reset_done_view(request):
    # Logique pour gérer la vue de confirmation d'envoi de lien de réinitialisation de mot de passe
    return auth_views.PasswordResetDoneView.as_view()(request)

def my_password_reset_confirm_view(request, uidb64, token):
    # Logique pour gérer la vue de confirmation de réinitialisation de mot de passe
    return auth_views.PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)

def my_password_reset_complete_view(request):
    # Logique pour gérer la vue de confirmation de réinitialisation de mot de passe complétée
    return auth_views.PasswordResetCompleteView.as_view()(request)

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authentification réussie, redirigez l'utilisateur vers une page spécifique
            return redirect('accueil')  # Remplacez 'accueil' par le nom de l'URL de votre choix
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def accueil(request):
    return render(request, 'acceuil.html')
from django.shortcuts import render, redirect
from .models import Dechets

def liste_dechets(request):
    dechets = Dechets.objects.all()
    return render(request, 'liste_dechets.html', {'dechets': dechets})


from .forms import DechetForm

def ajouter_dechet(request):
    if request.method == 'POST':
        form = DechetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_dechets')
    else:
        form = DechetForm()
    return render(request, 'ajouter_dechet.html', {'form': form})
from django.shortcuts import render
from .models import Dechets

def liste_dechets(request):
    dechets = Dechets.objects.all()
    return render(request, 'liste_dechets.html', {'dechets': dechets})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import DechetForm
from .models import Dechets

def modifier_dechet(request, dechet_id):
    dechet = get_object_or_404(Dechets, pk=dechet_id)
    if request.method == 'POST':
        form = DechetForm(request.POST, instance=dechet)
        if form.is_valid():
            form.save()
            return redirect('details_dechet', dechet_id=dechet_id)
    else:
        form = DechetForm(instance=dechet)
    return render(request, 'modifier_dechet.html', {'form': form})

from django.shortcuts import redirect, get_object_or_404
from .models import Dechets

def supprimer_dechet(request, dechet_id):
    dechet = get_object_or_404(Dechets, pk=dechet_id)
    dechet.delete()
    return redirect('liste_dechets')


from django.shortcuts import render, get_object_or_404
from .models import Dechets

def details_dechet(request, dechet_id):
    dechet = get_object_or_404(Dechets, pk=dechet_id)
    return render(request, 'details_dechet.html', {'dechet': dechet})



# Import necessary Django modules
from django.shortcuts import render
from django.conf import settings
import os
# from .prediction import *

# Define your Django view function
def application(request):
    file = ""
    answer = None
    error = ""
    
    if request.method == "POST":
        try:
            file = request.FILES["image"]
            if file:
                # Save the uploaded file
                file_path = os.path.join(settings.MEDIA_ROOT, file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # Get prediction
                result = predict(file.name)
                
                if result == "":
                    error = "Sorry!"
                else:
                    answer = result
                    
        except SyntaxError as e:
            error = "Could not understand"
            print("Error:" + str(e))

    return render(request, 'index.html', {'file': file,
                                          'answer': answer,
                                          'error': error})
# trash_classification/views.py
from django.shortcuts import render
from .forms import ImageUploadForm
import os
import cv2
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def predict(img_path):
    labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic'}
    img = image.load_img(img_path, target_size=(300, 300))
    img = image.img_to_array(img, dtype=np.uint8)
    img = np.array(img) / 255.0
     
    model = tf.keras.models.load_model("trained_model.h5")
    p = model.predict(img[np.newaxis, ...])
    pro = np.max(p[0], axis=-1)
    predicted_class = labels[np.argmax(p[0], axis=-1)]
    os.remove(img_path)
    return str(predicted_class) + " \n Probability:" + str(pro)

import os

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            filename = image_file.name
            file_path = os.path.join('uploads', filename)
            
            # Créer le répertoire "uploads" s'il n'existe pas
            os.makedirs('uploads', exist_ok=True)
            
            with open(file_path, 'wb') as f:
                f.write(image_file.read())
            result = predict(file_path)
            return render(request, 'index.html', {'answer': result})
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form})
