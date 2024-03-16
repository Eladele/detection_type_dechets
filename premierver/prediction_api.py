import os
import numpy as np
from keras.preprocessing import image
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from PIL import Image
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

UPLOAD_FOLDER = os.path.basename('.')
# Assurez-vous que le chemin vers votre modèle est correct
MODEL_PATH = "trained_model.h5"
# import tensorflow.compat.v1 as tf

# # Utilisez cette fonction pour calculer la perte
# loss = tf.compat.v1.losses.sparse_softmax_cross_entropy(labels, logits)

# Définissez votre modèle une seule fois pour économiser des ressources
model = tf.keras.models.load_model(MODEL_PATH)

# Fonction de prédiction
def predict(img_path):
    labels = {0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic'}
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img, dtype=np.uint8)
    img = np.array(img) / 255.0
    predicted = model.predict(img[np.newaxis, ...])
    prob = np.max(predicted[0], axis=-1)
    prob = prob * 100
    prob = round(prob, 2)
    prob = str(prob) + '%'
    predicted_class = labels[np.argmax(predicted[0], axis=-1)]
    category = ""
    if predicted_class in ['Cardboard', 'Paper']:
        category = "Biodegradable"
    elif predicted_class in ['Metal', 'Glass', 'Plastic']:
        category = "Non-Biodegradable"
    else:
        category = "Categorizing Difficult"
    return category, str(predicted_class), prob

# Vue pour gérer la requête POST
@csrf_exempt
def application(request):
    if request.method == "POST":
        try:
            file = request.FILES["file"]
            if file:
                f = os.path.join(settings.MEDIA_ROOT, file.name)
                with open(f, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                result = predict(f)
                if result:
                    response_data = {"success": "True", "result": result}
                    return JsonResponse(response_data)
                else:
                    return HttpResponseBadRequest()
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
