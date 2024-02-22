import joblib
import json

# load model with joblib
loaded_model = joblib.load('IDH Power Consuption.sav.sav')

# define a function to save the model as JSON
def save_model_as_json(model, filepath):
    model_json = model.get_params()
    with open(filepath, 'w') as json_file:
        json.dump(model_json, json_file)

# save model as JSON
save_model_as_json(loaded_model, 'model_params.json')