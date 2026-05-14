
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Ex 1
wine = load_wine(as_frame=True)
df = wine.frame
print("Ex 1:")
print("Primele 5 randuri:")
print(df.head())
print("\nCaracteristicile disponibile:")
print(wine.feature_names)

# Ex 2
X_sub = df[['alcohol', 'flavanoids']]
y = wine.target
clf_2 = DecisionTreeClassifier(max_depth=2, random_state=42)
clf_2.fit(X_sub, y)

plt.figure(figsize=(10, 8))
plot_tree(clf_2, feature_names=['alcohol', 'flavanoids'], class_names=wine.target_names, filled=True)
plt.show()

# Ex 3
print("\nEx 3:")
print("Nodul radacina evalueaza o conditie initiala (ex: flavanoids <= prag) si separa prima clasa.")
print("Nodurile de pe nivelul urmator aplica o a doua conditie (ex: pe alcohol) pentru a prezice clasa finala in frunze.")

# Ex 4
X_train, X_test, y_train, y_test = train_test_split(X_sub, y, test_size=0.3, random_state=42)
clf_full = DecisionTreeClassifier(max_depth=None, random_state=42)
clf_full.fit(X_train, y_train)
pred_full = clf_full.predict(X_test)
print("\nEx 4:")
print(f"Acuratete pe setul de testare (arbore complet): {accuracy_score(y_test, pred_full):.4f}")

# Ex 5
X_all = wine.data
X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all, y, test_size=0.3, random_state=42)
clf_all = DecisionTreeClassifier(random_state=42)
clf_all.fit(X_train_all, y_train_all)

print("\nEx 5:")
print("Importanta caracteristicilor:")
for nume, imp in zip(wine.feature_names, clf_all.feature_importances_):
    print(f"{nume}: {imp:.4f}")

# Ex 6
print("\nEx 6:")
print("Analizand lista de la Ex 5, caracteristicile cu cel mai mare scor (ex: proline, flavanoids) sunt cele care influenteaza cel mai mult deciziile arborelui.")