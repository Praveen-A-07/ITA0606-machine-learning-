import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Student dataset
data = {
    'Study_Hours': ['High', 'High', 'Medium', 'Low', 'Low',
                    'Medium', 'High', 'Medium', 'Low', 'High'],
    'Attendance': ['Good', 'Poor', 'Good', 'Good', 'Poor',
                   'Poor', 'Good', 'Good', 'Poor', 'Good'],
    'Assignment': ['Yes', 'Yes', 'No', 'Yes', 'No',
                   'Yes', 'Yes', 'No', 'No', 'Yes'],
    'Pass': ['Yes', 'Yes', 'Yes', 'No', 'No',
             'No', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Encode categorical data
encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features and target
X = df[['Study_Hours', 'Attendance', 'Assignment']]
y = df['Pass']

# Train ID3 model
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# New student data
new_student = pd.DataFrame({
    'Study_Hours': ['High'],
    'Attendance': ['Good'],
    'Assignment': ['Yes']
})

# Encode new data
for col in new_student.columns:
    new_student[col] = encoders[col].transform(new_student[col])

# Predict
prediction = model.predict(new_student)
result = encoders['Pass'].inverse_transform(prediction)

# Simple 3-line output
print("Model Trained Successfully")
print("Prediction:", result[0])
print("Classification Completed")