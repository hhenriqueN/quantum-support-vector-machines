# Imports do Qiskit
from qiskit.circuit.library import ZFeatureMap
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.state_fidelities import ComputeUncompute

# Imports clássicos
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

# 1. Define o Feature Map (transformação dos dados)
feature_map = ZFeatureMap(feature_dimension=2, reps=2)

# 2. Cria o Sampler quântico (simula o circuito)
sampler = StatevectorSampler()

# 3. Define a fidelidade via método compute-uncompute
fidelity = ComputeUncompute(sampler=sampler)

# 4. Define o kernel quântico com base em fidelidade
quantum_kernel = FidelityQuantumKernel(
    fidelity=fidelity,
    feature_map=feature_map
)
print("✅ Kernel quântico definido com sucesso!")

# 5. Carrega e prepara os dados
X, y = load_iris(return_X_y=True)
X = X[y != 2][:, :2]  # Apenas duas classes e duas features
y = y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 6. Avalia as matrizes de kernel diretamente com os dados
kernel_matrix_train = quantum_kernel.evaluate(X_train)
kernel_matrix_test = quantum_kernel.evaluate(X_test, X_train)
print("✅ Matrizes de similaridade calculadas!")

# 7. Treina o QSVM com kernel pré-computado
qsvm = SVC(kernel='precomputed')
qsvm.fit(kernel_matrix_train, y_train)

# 8. Predição e avaliação
y_pred = qsvm.predict(kernel_matrix_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"🎯 Acurácia do QSVM: {accuracy:.2f}")
