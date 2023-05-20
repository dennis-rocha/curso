# Bem vindo aluno!

Seja bem vindo a nossa primeira aula!

## Proposta
Nesta aula vamos aprender sobre:
- Conceitos básicos em python e sua sintaxe.
- Váriaveis.
- Aprendendo matemática com pyhton.
- Tabela verdade.

## Introdução 
Python é uma das linguagens mais utilizadas no mundo. Ela é favorita devido a sua facilidade de aprendizagem e suas possibilidades de uso. Com Python é possível desenvolver aplicações Webs, Mobile, Desktop, Automações, IA, IoT, entre outras.

No decorrer do curso vamos estudar as mais diversas aplicações, para que todo o conteúdo seja eficaz teremos exercícios durante a aulas e ao final de cada módulo teremos um projeto que vamos exercitar tudo o que for aprendido.

## Conteúdo
Python é uma linguagem de tipagem forte e dinâmica. Isso significa que para criar suas váriaveis não existe a necessidade de atribuir o tipo dela. Essa linguagem interpreta o tipo da linguagem durante a execução e não no tempo de compilação. Porém ao usar um tipo de váriavel, suas funções só pode ser acessada ao tipo dela. A variável pode mudar de tipo durante a execução do programa veremos isso mais na frente do curso, veja a seguir como criar uma variável:

- Para atribuir uma valor numa variável precisamos definir um _nome_ e um _valor_. Por exemplo: `nome = 'Carlos'`. Tudo o que fica a esquerda do `=` é o nome da variável (como vamos acessar) e o que fica a direita é o valor que estamos atribuindo a ela. 
- Podemos definir que **=** é o mesmo que **recebe**.
- O desenvolvimento ocorre da esquerda para direita.
  
Afinal, o que é variável?

Uma variável é um valor armazenado na mémoria do RAM do computador e acessamos esse valor através de um ponteiro, neste caso o _nome_ da variável! Imagine um armário com diversas divisórias, nesse armário você pode guardar alguma coisa dentro dele. Ao guardar, você precisa por um _nome_ ou um número para facilitar a busca disso. É exatamente isso que é a variável. Inserimos um valor e um nome, esse valor é armazenado na mémoria RAM e acessamos esse valor através desse ponteiro.

Que tal um pouco de matemática para exercitar isso? 
Vamos fazer uma soma:
- 2 + 2 = ?
- 2 + 4 = ?

Resultado 2 + 2 = 4, correto?
Vamos armazenar esse valor...
- x = 2 + 2.
- y = 2 + x.

Qual o valor de `y`? Se você pensou em 6 está correto!
Veja que o resultado é armazenado em `x` e depois usamos o resultado para somar outro número!
Usando o mesmo conceito que conhecemos fica mais fácil aprender!

A tabela verdade é usada para criarmos a lógica durante o desenvolvimento de software. Para criar a Tabela Verdade temos os valores `P` e `Q`, também temos os operadores lógicos os quais são: ~ (not) negação, ^ (and) soma, v (or) algum. Veja a seguir a Tabela Verdade:

| P | Q | ~ P | ~ Q | P ^ Q | P v Q |
|--- |--- |--- |--- | --- |--- | 
| v | v | f | f | v | v |
| v | f | f | v | f | v |
| f | v | v | f | f | v |
| f | f | v | v | f | f |

O operador lógico **~** (not) faz a negação do valor, veja a tabela onde `P` é Verdadeiro (primeira coluna) com a negação (terceira coluna) se tornou um Falso e onde era Falso com a negação de tornou-se Verdadeiro. O mesmo ocorre para o valor `Q`.

O operador lógico **^** (and) faz a "soma" desses valores, veja a tabela verdade onde **P ^ Q** (quinta coluna) são verdadeiros o resultado é V, para o resultado do operador **AND** ser Verdadeiro todas as condições precisam ser verdadeiras. Se alguma condição **AND** for Falso o resultado sempre será Falso.

O operador lógico **v** (OR) obtém o resultado onde qualquer uma das condições sejam verdadeiras, veja a tabela verdade onde **P v Q** (sexta coluna) são Falsos, o resultado é um F. S.e qualquer outra condição for V no operador **OR** o resultado será V.

Perceba na tabela verdade que o **NOT** faz a negação (inverte o valor), o **AND** só será Verdadeiro quando TODAS as condições for Verdadeiro e o operador **OR** só será Falso onde TODAS as condições for Falsas.

Vamos exercitar isso, ilustrando o seguinte cenário:
- caso_1 = Verdadeiro
- caso_2 = Falso
- Qual o resultado `caso_1 and caso_2`?
- Qual o resultado `caso_1 or caso_2`?
- Qual o resultado `caso_1 and (not caso_2)`?
- Qual o resultado `(not caso_1) and caso_2`?

Se você pensou nesse resultado `F,V,V,F` você acertou!
Explicação: V and F é Falso, V or F é Verdadeiro, V and V é Verdadeiro, F or F é Falso.

Não deixe de exercitar e vamos para a aula!