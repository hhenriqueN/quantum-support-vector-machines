# Importações

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Carrega o Iris dataset
X, y = load_iris(return_X_y=True)

# Filtra apenas duas classes para problema binário
mask = y < 2
X = X[mask]
y = y[mask]

# Seleciona apenas duas features (colunas)
X = X[:, :2]

# Divide em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Plota os dados
plt.figure(figsize=(8, 6))
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolors='k', label='Train')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm', marker='x', label='Test')
plt.title('Dataset Iris - Duas Classes e Duas Features')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

