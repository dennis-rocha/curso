# Bem-vindo aluno!

Seja bem-vindo a nossa segunda aula!

## Proposta
Nesta aula vamos aprender sobre:
- Os tipos de variáveis.
- As principais funções de cada tipo.
- Conversão de tipos de variáveis.

## Introdução 
Em Python toda variável é um objeto, ou seja, é a instância de uma classe. Não precise se preocupar sobre Programação Orientada a Objetos (POO) agora, vamos aprender mais adiante. Todavia é importante compreender como essa linguagem funciona e como ela é fácil de aprender!

## Conteúdo
Existem alguns tipos de variáveis. Você viu na aula anterior alguns tipos, como, por exemplo, o nome, idade ou os valores booleanos.

Em Python os tipos são:
1. String,
2. Int,
3. Float,
4. Bool,
5. List,
6. Tuple,
7. Dict,
8. Set,
9. Complex.


### 1. String
O tipo String é uma sequência que pode ser de zero ou mais de caracteres usadas para determinar textos ou bytes.

Esse tipo de dado pode ser preenchido, por exemplo, com o seu nome, frases, textos, etc. <br>
Podemos definir uma variável do tipo `string` com aspas duplas `"` ou aspas simples `'`, Por exemplo:
- `nome = "Meu nome Completo"`
- `frase_favorita = 'Minha frase Favorita'`

As duas maneiras estão corretas!

**Funções**

As principais funções com string é:
- `split()` - Serve para quebrar uma string a partir de um caractere, por exemplo: `variavel.split(",")`.
- `strip()` - Serve para remover espaços em branco no início ou no final de um texto, por exemplo: `variavel.strip()`. Isso não remove espaços em branco no meio do texto!
- `join()` - Serve para unir uma lista de strings, por exemplo: `",".join(["nome","sobrenome"])`.
- `capitalize()` - Deixa a primeira letra maiúscula, por exemplo: `"pedro".capitalize()` -> `'Pedro'`.
- `upper()` - Deixa todas as letras maiúsculas, por exemplo: `"pedro".upper()` -> `'PEDRO'`.
- `title()` - Deixa todas as primeiras letras maiúsculas, por exemplo: `"pedro sampaio".title()` -> `'Pedro Sampaio'`
  

### 2. Int
O tipo Int é um valor numérico sem um componente decimal, podendo ser positivo ou negativo.

Esse tipo de dado pode ser preenchido com números inteiros como: idade, quantidade ou outro valor numérico. <br>
Para preencher uma variável do tipo inteiro não deve ser usado aspas duplas ou simples, por exemplo:
- `idade = 18`
- `quantidade_produto = 2`
- `juros = -10`

**Funções**

Vejamos algumas funções built-ins do Python que retorna um número inteiro:
- `round()` - Essa função arredonda um valor decimal, exemplo: `round(12.3363)` -> `12`. Se esse numero for `12.6` será arredondado para `13`.
- `len()` - Obtém o tamanho de uma lista, exemplo: `len(["Banana", "Maça", "Uva"])` -> `3`. 


### 3. Float
O tipo Float é um valor numérico com casas decimais, podendo ser positivo ou negativo.

Esse tipo de dado pode ser preenchido com números decimais como: Peso, altura ou outro valor decimal. <br>
Para preencher uma variável do tipo Float não deve ser usado aspas duplas ou simples, por exemplo:
- `peso = 76.5`
- `altura = 1.75`
- `minuto = 2.21`

**Funções**

Vejamos algumas funções built-ins do Python que retorna um número float:
- `round()` - Essa função arredonda um valor decimal, exemplo: `round(12.3363,2)` -> `12.34`. Parecido com o tipo inteiro, mas necessário inserir um parâmetro a mais.
- `is_integer()` - Verifica se o número é inteiro, exemplo: `peso.is_integer()` -> `False`. Se o número for `12.0` o retorno é `True`.


### 4. Bool
O tipo Bool é um tipo booleano, podendo ter apenas valores True ou False. 

Esse tipo de dado é usado em variáveis representados como verdadeiro ou falso. Esses valores lógicos podem ser usados para representar uma afirmação ou negação, representar se possui ou não, entre outros. O tipo bool pode ser preenchido com `True` ou `False`, `1` ou `0`, `" "` ou `""`. Esse tipo de dado é muito usado para construir condições lógicas.

**Funções**
Existem algumas funções que usamos esse tipo de dado ou que retorna `True` ou `False`. Vamos aprender mais sobre esse tipo nas próximas aulas.
- `isnumeric()` - Essa função é do tipo de dado Str, mas ao usá-lo o retorno é um Bool. Exemplo: `nome.isnumeric()` -> `False`, isso porque nome é uma string. Mesmo sendo string, mas preenchido com números, por exemplo, `"2000"`, o retorno seria `True`.


### 5. List
O tipo List é uma coleção ordenada de valores, podendo assumir outros tipos de dados dentro de seus elementos. 

Esse tipo de dado pode ser preenchido com: números Inteiros, Decimais, Booleanos, Dicionários ou até mesmo outras listas. <br>
Para preencher uma variável do tipo lista precisa ser usado os colchetes `[]` e cada item dentro da lista precisa ser separado por vírgula `,`, por exemplo:
- `lista_compras = ["Maça", "Banana", "Melão"]`
- `notas = [10, 5.5, 7.5]`
- `usuarios = [["Fernado","Garcia",1.75],["Maria","Silva",1.63]]`

**Funções**

As principais funções são:
- `sort()` - Essa função ordena os itens (apenas itens do mesmo tipo), exemplo: `[10,7.6,5.5].sort()` -> `[5.5, 7.6, 10]`
- `append()` - Adiciona um novo elemento na lista, exemplo: `lista_compras.append("Uva")` -> `["Maça", "Banana", "Melão", "Uva"]`
- `extend()` - Adiciona itens de uma lista em outras, exemplo: `notas.extend([5, 9, 8])` -> `[10, 5.5, 7.5, 5, 9, 8]` 
- `count()` - Retorna o total de itens dentro da lista, exemplo: `usuarios.count()` -> `2`


### 6. Tuple
O tipo Tuple é uma coleção ordenada de valores, podendo assumir outros tipos de dados dentro de seus elementos. 

Esse tipo de dado pode ser preenchido com: números Inteiros, Decimais, Booleanos, Dicionários ou até mesmo outras listas. <br>
Para preencher uma variável do tipo Tupla precisa ser usado os parêntesis `()` e cada item dentro da tupla precisa ser separado por vírgula `,`. Esse tipo de dado é parecido com a lista, mas a diferença é que não pode ser editado após ser construído e com isso aumenta o desempenho quando é criado esse tipo de dado comparado ao tipo da lista. Por exemplo:
- `lista_compras = ("Maça", "Banana", "Melão")`
- `usuarios = (("Fernado","Garcia",1.75),("Maria","Silva",1.63))`

**Funções**

As funções são:
- `count()` - Retorna o total de itens dentro da tupla, exemplo: `usuarios.count()` -> `2`
- `index()` - Retorna o índice de um item dentro dessa Tupla, exemplo: `lista_compras.index('Banana')` -> 1


### 7. Dict

O tipo Dict é um tipo de dado onde possui chave e valor devendo ficar entre chaves `{}`.

Esse tipo de dado pode ser preenchido com diferentes tipos de dados, só deve observar que se possuir duas chaves iguais à primeira chave será substituída pela segunda. Por exemplo: `{'a':1,'b':2,'a':3}` observe que possui duas chaves `'a'`, mas o resultado se salvar ou usar o `print()` o resultado será `{'a': 3, 'b': 2}`. Outros casos de uso desse tipo de dado é: `{"vendedor":"Luísa","produtos":[{"item":"Calça", "valor":79.90},{"item":"Camisa", "valor":50}]}` <br>
Perceba que possui uma chave com o nome do vendedor e preenchido com um nome e possui uma chave com o nome produtos no qual está preenchido com uma lista de produtos. Observe que cada item dessa lista é um dicionário também.
- `usuario = {"nome":"Joaquim", "email":"joaquim21@email.com"}`

**Funções**

As principais funções são:
- `items()` - Retorna um Objeto, porém podemos transformar em uma lista de tuplas das chaves e valores. Por exemplo: `usuario.items()` -> `dict_items([('nome', 'Joaquim'), ('email', 'joaquim21@email.com')])`, perceba que mesmo sendo um objeto o retorno é uma lista de tuplas.


### 8. Set

O tipo Set é tipo de coleção de itens que não pode conter elementos duplicados.

Esse tipo de dado pode ser preenchido apenas com valores numéricos e string usando as chaves `{}`, por exemplo: `{1,2,4,"a","c"}`. Esse tipo de dado pode parecer o tipo Dict, no entanto, são diferentes. Note que o tipo Dict necessita chave e valor separados por `:` entre si e vírgula `,` para cada "coluna". Esse tipo possui apenas as "chaves" separados por `,` como se fosse uma lista. Por exemplo:
- `a = {1,2,3}`
- `b = {2,4,5}`
- `c = {4,2,1}`

**Funções**

As principais funções são:
- `union()` - Retorna um novo Set unindo os valores de ambos Sets, por exemplo: `a.union(b)` -> `{1, 2, 3, 4, 5}`.
- `intersection()` - Retorna um novo Set contendo apenas os valores que estão nos dois Sets, por exemplo: `a.intersection(b)` -> `{2}`
- `difference()` - Retorna um novo Set que possui apenas a diferença de um dos Sets, por exemplo: `a.difference(b)` -> `{1,3}`, o `2` está em ambos os Sets e por isso não foi retornado.



