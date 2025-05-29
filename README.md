# Escalonador de Matrizes em Python (Python Matrix Scaler)

## Descrição

Este projeto é um script simples em Python que permite ao usuário escalar uma matriz numericamente. O usuário pode definir as dimensões da matriz, inserir seus elementos e especificar um fator de escala. O script então calcula e exibe a matriz resultante, onde cada elemento da matriz original foi multiplicado pelo fator de escala.

Este projeto foi desenvolvido como um exercício prático para manipulação de matrizes com Python e a biblioteca NumPy, focando também na interação com o usuário e validação de entradas.

## Funcionalidades

* Permite a entrada interativa das dimensões da matriz (número de linhas e colunas).
* Coleta os elementos da matriz linha por linha, diretamente do usuário.
* Solicita ao usuário o fator de escala desejado.
* Valida as entradas do usuário para garantir que:
    * As dimensões sejam números inteiros positivos.
    * Os elementos da matriz sejam numéricos.
    * O número correto de elementos seja fornecido para cada linha.
    * O fator de escala seja um valor numérico.
* Utiliza a biblioteca NumPy para realizar a operação de escalonamento de forma eficiente.
* Exibe a matriz original fornecida e a matriz escalonada resultante.

## Pré-requisitos

Para rodar este script, você precisará ter instalado:

* **Python 3.x** (você pode baixar em [python.org](https://www.python.org/))
* **Biblioteca NumPy**

## Instalação da Biblioteca NumPy

Se você ainda não tem a biblioteca NumPy instalada, abra seu terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install numpy