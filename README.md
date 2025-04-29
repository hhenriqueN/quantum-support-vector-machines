# quantum-support-vector-machines
Mostrar como a Álgebra Linear é usada na construção de matrizes de kernel quânticas para classificar dados com Quantum Support Vector Machine (QSVM) 


```IMPORTANTE! Como a Computação Quântica é uma área em estágio de desenvolvimento e constante adaptação, a biblioteca utilizada neste projeto (Qiskit, da IBM) teve atualizações recentes que não estavam perfeitamente otimizadas durante o desenvolvimento deste trabalho. Por isso, tive que fazer algumas alterações internas dentro do pacote da biblioteca pra que houvesse compatibilidade entre as dependências, é possível e esperado que o código não funcione sem estas alterações e por isso deixei todas as alterações necessárias documentadas em QISKIT.md!```

No projeto há dois arquivos Python `quantum_classification.py` e `classical_classification.py`, cada um deles contendo os códigos necessários para classificar (separar por classes) dados de um banco de dados. Um utiliza a abordagem clássica com SVM (Support Vector Machine) normal, e o outro com QSVM (Quantum Support Vector Machine).

Para rodar o projeto é necessário instalar as dependencias contidas em requirements.txt e rodar os códigos.
