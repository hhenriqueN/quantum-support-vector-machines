Primeiramente, as versões utilizadas que ficam compativeis após estas alterações são:

qiskit                  2.0.0
qiskit-aer              0.17.0
qiskit-machine-learning 0.8.2


### 1) utils.py

Em `qiskit/primitives/utils.py` é necessário incluir a seguinte função:

```python
def _circuit_key(circuit: QuantumCircuit) -> str:
    return str(hash(circuit.draw('text')))
```
    

### 2) compute_uncompute.py

Em `qiskit_machine_learning/state_fidelities/compute_uncompute.py` é necessário:

1. Ajustar as importações

Troque:
```python
from qiskit.primitives import BaseSampler, BaseSamplerV1, SamplerResult
```

Por:
```python
from qiskit.primitives import BaseSamplerV1, SamplerResult
from qiskit.primitives.base import BaseSamplerV2
```

2. Ajustar o tipo esperado no __init__ da classe ComputeUncompute

Dentro da função __init__, altere isto:

```python
sampler: BaseSampler | BaseSamplerV2,
```

Por isto:

```python
sampler: BaseSamplerV2,
```


3. Ajustar validações de tipo

Troque isto:

```python
if (not isinstance(sampler, BaseSampler)) and (not isinstance(sampler, BaseSamplerV2)):
```

Por isto:

```python
if not isinstance(sampler, (BaseSamplerV1, BaseSamplerV2)):
```

4. Ajustar atribuições internas

Troque isto:

```python
self._sampler: BaseSampler = sampler
```

Por isto:

```python
self._sampler: BaseSamplerV2 = sampler

```


