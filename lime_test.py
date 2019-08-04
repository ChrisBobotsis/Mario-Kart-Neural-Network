from lime import lime_image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

filepath_dir = 'data/models/'
file_name = 'conv_net_custom-07-28-2019_11-33-29'

filepath = filepath_dir+file_name

model = load_model(
    filepath,
    custom_objects=None,
    compile=True
)

X = np.load('data/training_data/6-ready_for_model/X_Full-DataSet-07-21-2019_22-30-46.npy')

image = X[0].reshape(32,100)

#image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)

explainer = lime_image.LimeImageExplainer()
explanation = explainer.explain_instance(image, model.predict, top_labels=1, hide_color=0, num_samples=1000)

temp, mask = explanation.get_image_and_mask(240, positive_only=True, num_features=5, hide_rest=False)
plt.imshow(temp / 2 + 0.5, mask)