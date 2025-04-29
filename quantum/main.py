# Imports corretos
from qiskit.circuit.library import ZFeatureMap
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.state_fidelities import ComputeUncompute



# 1. Define o Feature Map
feature_map = ZFeatureMap(feature_dimension=2, reps=2)

# 2. Cria o Sampler
sampler = StatevectorSampler()

# 3. Cria o objeto de Fidelity via ComputeUncompute
fidelity = ComputeUncompute(sampler=sampler)

# 4. Cria o Kernel Quântico
quantum_kernel = FidelityQuantumKernel(
    feature_map=feature_map,
    fidelity=fidelity
)

print("✅ Kernel quântico definido com sucesso!")
