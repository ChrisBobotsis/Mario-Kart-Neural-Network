import shap
import numpy as np
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
X = X[0:10]

sample = X[0].reshape(1,32,100,1)

explainer = shap.DeepExplainer(model,sample)

shap_values,indexes = explainer.shap_values(sample)

shap.image_plot(shap_values, sample, indexes)