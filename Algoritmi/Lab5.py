#knn


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()

print("1. Explorarea setului de date")
print(f"Numar de exemple si caracteristici: {iris.data.shape}")
print(f"Denumirile caracteristicilor (coloanelor): {iris.feature_names}")
print(f"Numele claselor: {iris.target_names}\n")

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

print("2. Impartirea setului")
print(f"Forma setului de antrenament: {X_train.shape}")
print(f"Forma setului de testare: {X_test.shape}\n")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("3. Preprocesarea datelor")
print("Primele 3 exemple INAINTE de scalare:")
print(X_train[:3])
print("\nPrimele 3 exemple DUPA scalare:")
print(X_train_scaled[:3], "\n")

knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(X_train_scaled, y_train)
acc_3 = knn3.score(X_test_scaled, y_test)

print("4. Modelul KNN (k=3)")
print(f"Acuratetea pe setul de testare (k=3): {acc_3 * 100:.2f}%\n")

k_values = range(1, 16)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acc = knn.score(X_test_scaled, y_test)
    accuracies.append(acc)

print("5. Impactul lui k")
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='dashed', color='b')
plt.title('Acuratetea modelului knn in functie de k')
plt.xlabel('Valoarea lui k')
plt.ylabel('Acuratete pe setul de testare')
plt.xticks(k_values)
plt.grid(True)
plt.show()

y_pred = knn3.predict(X_test_scaled)

print("6. Evaluarea modelului (pentru k=3)")
print("Matricea de confuzie:")
print(confusion_matrix(y_test, y_pred))

print("\nRaport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("7. Vizualizare si Predictie")
plt.figure(figsize=(8, 5))
scatter = plt.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title('Distributia claselor dupa Petal Length si Petal Width')
plt.legend(handles=scatter.legend_elements()[0], labels=list(iris.target_names))
plt.show()

print("Introduceti valorile pentru o floare noua:")
try:
    sl = float(input("Sepal length (cm): "))
    sw = float(input("Sepal width (cm): "))
    pl = float(input("Petal length (cm): "))
    pw = float(input("Petal width (cm): "))

    new_flower = np.array([[sl, sw, pl, pw]])
    new_flower_scaled = scaler.transform(new_flower)

    pred = knn3.predict(new_flower_scaled)
    predicted_class = iris.target_names[pred[0]]
    print(f"\nFloarea introdusa a fost clasificata ca fiind: {predicted_class.upper()}")

except ValueError:
    print("Va rugam sa introduceti doar numere valide!")
