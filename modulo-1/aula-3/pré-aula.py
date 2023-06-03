# Bem-vindo aluno!

Seja bem-vindo a nossa terceira aula!


## Proposta
Nesta aula vamos aprender sobre:
- Os tipos condicionais.
- Tratamento de erro.

## Introdução 
As estruturas condicionais em Python permitem que você execute diferentes blocos de código com base em determinadas condições. Existem diferentes tipos de estruturas condicionais: simples, composta, aninhada e encadeada.


## Conteúdo
Existem quatro tipos de Estruturas condicionais, são elas:
1. Condicional simples,
2. Condicional composta,
3. Condicional aninhada,
4. Condicional encadeada.


### 1. Condicional simples
A condicional simples verifica uma única condição e executa um bloco de código se essa condição for verdadeira. A sintaxe básica da condicional simples em Python é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira
```

Aqui está um exemplo simples:

```python
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
```

Neste exemplo, o código verifica se a idade é maior ou igual a 18. Se for verdadeiro, ele imprime a mensagem "Você é maior de idade".


### 2. Condicional composta
A condicional composta verifica uma condição e executa um bloco de código se essa condição for verdadeira. Caso contrário, ela executa um segundo bloco de código. A sintaxe básica da condicional composta em Python é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa
```

Aqui está um exemplo simples:

```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Neste exemplo, o código verifica se a idade é maior ou igual a 18. Se for verdadeiro, ele imprime a mensagem "Você é maior de idade". Caso contrário, imprime a mensagem "Você é menor de idade".


### 3. Condicional aninhada
A condicional aninhada contém uma estrutura condicional dentro de outra. Isso permite verificar múltiplas condições em sequência. A sintaxe básica da condicional aninhada em Python é a seguinte:

```python
if condição1:
    # código a ser executado se a condição1 for verdadeira
    if condição2:
        # código a ser executado se a condição2 for verdadeira
    else:
        # código a ser executado se a condição2 for falsa
else:
    # código a ser executado se a condição1 for falsa
```

Aqui está um exemplo simples:

```python
idade = 25
if idade >= 18:
    print("Você é maior de idade.")
    if idade >= 21:
        print("Você também pode beber álcool.")
else:
    print("Você é menor de idade.")
```

Neste exemplo, o código verifica se a idade é maior ou igual a 18. Se for verdadeiro, imprime a mensagem "Você é maior de idade" e, em seguida, verifica se a idade é maior ou igual a 21. Se essa segunda condição for verdadeira, imprime a mensagem "Você também pode beber álcool".


### 4. Condicional encadeada
A condicional encadeada verifica várias condições em sequência, permitindo executar diferentes blocos de código com base em diferentes condições. A sintaxe básica da condicional encadeada em Python é a seguinte:

```python
if condição1:
    # código a ser executado se a condição1 for verdadeira
elif condição2:
    # código a ser executado se a condição2 for verdadeira
elif condição3:
    # código a ser executado se a condição3 for verdadeira
else:
    # código a ser executado se todas as condições anteriores forem falsas
```

Aqui está um exemplo simples:

```python
idade = 20
if idade < 18:
    print("Você é menor de idade.")
elif idade < 21:
    print("Você é maior de idade, mas ainda não pode beber álcool.")
else:
    print("Você é maior de idade e pode beber álcool.")
```

Neste exemplo, o código verifica a idade e imprime uma mensagem diferente com base nas condições. Se a idade for menor que 18, imprime "Você é menor de idade". Se for maior ou igual a 18, mas menor que 21, imprime "Você é maior de idade, mas ainda não pode beber álcool". Caso contrário, imprime "Você é maior de idade e pode beber álcool".

