import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import BayesianEstimator

# Load dataset
df = pd.read_csv("D:\BE Sem 7\IR_Practicals\IR_Practicals\heart.csv")

# Preprocessing
continuous = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
bins = {}

for col in continuous:
    df[col], bins[col] = pd.cut(
        df[col], bins=3, labels=False,
        retbins=True, include_lowest=True
    )
    bins[col][0], bins[col][-1] = -np.inf, np.inf

df = df.astype(int)

# Split dataset
X, y = df.drop('target', axis=1), df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

train = X_train.copy()
train['target'] = y_train

# Construct Bayesian Network
model = DiscreteBayesianNetwork(
    [('target', col) for col in X.columns]
)

model.add_cpds(*BayesianEstimator(
    model, train
).get_parameters(prior_type='BDeu'))

print("Model Validity:", model.check_model())

# Test model
pred = model.predict(X_test)['target']
print("Model Accuracy:",
      round(accuracy_score(y_test, pred) * 100, 2), "%")

# Input ranges
ranges = {
    'age': (1, 100),
    'sex': (0, 1),
    'cp': (0, 3),
    'trestbps': (90, 200),
    'chol': (100, 600),
    'fbs': (0, 1),
    'restecg': (0, 2),
    'thalach': (60, 220),
    'exang': (0, 1),
    'oldpeak': (0, 7),
    'slope': (0, 2),
    'ca': (0, 4),
    'thal': (0, 3)
}

# Take patient details
print("\nEnter Patient Medical Details:")

patient = {}

for col, (low, high) in ranges.items():
    while True:
        try:
            value = float(input(f"{col} ({low}-{high}): "))

            if low <= value <= high:
                patient[col] = value
                break

            print("Invalid input! Enter value within range.")

        except ValueError:
            print("Please enter a valid number.")

patient = pd.DataFrame([patient])

# Apply preprocessing
for col in continuous:
    patient[col] = pd.cut(
        patient[col], bins=bins[col],
        labels=False, include_lowest=True
    )

patient = patient.astype(int)

# Predict diagnosis
prob = model.predict_probability(patient)

heart = prob['target_1'].iloc[0]

print("\nDiagnosis Probability:")
print("No Heart Disease:",
      round(prob['target_0'].iloc[0] * 100, 2), "%")
print("Heart Disease:",
      round(heart * 100, 2), "%")

print("\nFinal Diagnosis:")
print("Heart Disease Detected" if heart > 0.5
      else "No Heart Disease Detected")


# Another Similar Code for Heart Disease Prediction using Bayesian Network :

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from pgmpy.models import DiscreteBayesianNetwork
# from pgmpy.estimators import BayesianEstimator

# # Load and preprocess dataset
# df = pd.read_csv("heart(1).csv")
# cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
# bins = {}

# for c in cols:
#     df[c], bins[c] = pd.cut(df[c], 3, labels=False,
#                             retbins=True, include_lowest=True)
#     bins[c][[0, -1]] = [-np.inf, np.inf]

# # Train Bayesian Network
# X, y = df.drop('target', axis=1), df['target']
# a, b, ya, yb = train_test_split(X, y, test_size=0.2,
#                                  random_state=42, stratify=y)

# train = a.copy()
# train['target'] = ya

# model = DiscreteBayesianNetwork([('target', c) for c in X.columns])
# model.add_cpds(*BayesianEstimator(model, train).get_parameters(prior_type='BDeu'))

# print("Model Validity:", model.check_model())
# print("Accuracy:", round(accuracy_score(yb, model.predict(b)['target'])*100, 2), "%")

# # User input with ranges
# ranges = {
#     'age': (1, 100), 'sex': (0, 1), 'cp': (0, 3),
#     'trestbps': (90, 200), 'chol': (100, 600),
#     'fbs': (0, 1), 'restecg': (0, 2), 'thalach': (60, 220),
#     'exang': (0, 1), 'oldpeak': (0, 7), 'slope': (0, 2),
#     'ca': (0, 4), 'thal': (0, 3)
# }

# patient = {}
# print("\nEnter Patient Details:")

# for c, (low, high) in ranges.items():
#     while True:
#         try:
#             v = float(input(f"{c} ({low}-{high}): "))
#             if low <= v <= high:
#                 patient[c] = v
#                 break
#             print("Enter value within range!")
#         except ValueError:
#             print("Enter a valid number!")

# patient = pd.DataFrame([patient])

# # Apply same preprocessing
# for c in cols:
#     patient[c] = pd.cut(patient[c], bins[c],
#                         labels=False, include_lowest=True)

# # Diagnosis
# prob = model.predict_probability(patient.astype(int))
# heart = prob['target_1'].iloc[0]

# print("\nHeart Disease:", round(heart*100, 2), "%")
# print("No Heart Disease:", round(prob['target_0'].iloc[0]*100, 2), "%")
# print("Final Diagnosis:", "Heart Disease Detected" if heart > 0.5
#       else "No Heart Disease Detected")