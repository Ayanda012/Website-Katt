import json
from sklearn.ensemble import RandomForestClassifier

# load model from JSON file
with open('model_params.json', 'r') as json_file:
    model_params = json.load(json_file)

# create a new model with the loaded parameters
loaded_model = RandomForestClassifier(**model_params)
# load test data
X_test, y_test = ...

# evaluate model 
y_predict = loaded_model.predict(X_test)

# check results
print(classification_report(y_test, y_predict))