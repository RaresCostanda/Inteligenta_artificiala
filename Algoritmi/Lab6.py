#regresie liniara

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print("Primele 5 randuri")
print(df.head())
print("\n")

print("Caracteristici disponibile")
print(diabetes.feature_names)
print("\n")

print("Informatii statistice")
print(df.describe())
print("\n")

plt.figure(figsize=(8, 5))
plt.hist(df['bmi'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma pentru BMI')
plt.xlabel('BMI (valori standardizate)')
plt.ylabel('Frecventa')
plt.show()

plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['age'], df['bmi'], c=df['target'], cmap='viridis', alpha=0.8)
plt.colorbar(scatter, label='Scorul Diabetului (Target)')
plt.title('Relatia dintre varsta si BMI colorata dupa Target')
plt.xlabel('Varsta (standardizata)')
plt.ylabel('BMI (standardizat)')
plt.show()

X_simple = df[['bmi']]
y = df['target']
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_simple, y, test_size=0.2, random_state=42)

model_simplu = LinearRegression()
model_simplu.fit(X_train_s, y_train_s)

y_pred_s = model_simplu.predict(X_test_s)
mse_simple = mean_squared_error(y_test_s, y_pred_s)

print("Regresie Liniara Simpla (BMI)")
print(f"Eroarea patratica medie (MSE): {mse_simple:.2f}\n")

plt.figure(figsize=(8, 5))
plt.scatter(X_test_s, y_test_s, color='blue', label='Date reale (Test)', alpha=0.6)
plt.plot(X_test_s, y_pred_s, color='red', linewidth=2, label='Linia de regresie')
plt.title('Regresie Liniara Simpla: BMI vs Diabet')
plt.xlabel('BMI')
plt.ylabel('Scor Diabet (Target)')
plt.legend()
plt.show()

X_multi = df[['bmi', 'bp']]
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

y_pred_m = model_multi.predict(X_test_m)
r2_multi = r2_score(y_test_m, y_pred_m)

print("Regresie Multipla (BMI, BP)")
print(f"Coeficient BMI: {model_multi.coef_[0]:.2f}")
print(f"Coeficient BP: {model_multi.coef_[1]:.2f}")
print(f"Scorul R2 pe setul de testare: {r2_multi:.4f}")