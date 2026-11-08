# Iteradores em Python (Iterators)

## 1. Introdução aos Iteradores

Os **iteradores (Iterators)** são objetos utilizados para percorrer elementos de uma coleção ou sequência de dados, permitindo acessar um elemento por vez.

Em Python, os iteradores são fundamentais para trabalhar com estruturas de repetição, especialmente o laço `for`.

Sempre que utilizamos um `for` para percorrer uma lista, uma tupla ou um dicionário, Python utiliza internamente o mecanismo de iteração.

### 1.1. O que é iteração?

A iteração é o processo de percorrer uma sequência de elementos, acessando cada elemento individualmente.

Por exemplo, imagine uma lista contendo nomes:

```python
nomes = ["Matheus", "João", "Maria", "Pedro"]

for nome in nomes:
    print(nome)
```

**Resultado:**

```text
Matheus
João
Maria
Pedro
```

Nesse exemplo, o Python percorre a lista e apresenta cada elemento individualmente.

Esse processo é chamado de iteração.

### 1.2. Diferença entre Iterável e Iterador

Embora sejam conceitos relacionados, **iterável (Iterable)** e **iterador (Iterator)** não significam a mesma coisa.

**Iterável (Iterable):**

É qualquer objeto capaz de fornecer um iterador, permitindo que seus elementos sejam percorridos.

Exemplos:

- Listas (`list`).
- Tuplas (`tuple`).
- Dicionários (`dict`).
- Conjuntos (`set`).
- Strings (`str`).
- Arquivos.

**Iterador (Iterator):**

É um objeto responsável por fornecer os elementos de um iterável, um de cada vez, mantendo o estado da iteração.

Em Python, um iterador implementa dois métodos fundamentais:

- `__iter__()`: retorna o próprio iterador.
- `__next__()`: retorna o próximo elemento disponível.

**Exemplo conceitual:**

```text
ITERÁVEL
   |
   | iter()
   v
ITERADOR
   |
   | next()
   v
PRÓXIMO ELEMENTO
```

---

## 2. O método iter()

O método `iter()` é utilizado para obter um iterador a partir de um objeto iterável.

Ele solicita ao objeto que forneça um iterador, utilizando internamente o protocolo de iteração do Python.

### 2.1. Exemplo prático

```python
numeros = [10, 20, 30, 40, 50]

# Criando um iterador
iterador = iter(numeros)

print(iterador)
```

**Resultado aproximado:**

```text
<list_iterator object at 0x...>
```

Observe que `iter()` não retorna a lista original. Ele retorna um objeto iterador responsável por percorrer seus elementos.

### 2.2. Verificando os tipos

Podemos utilizar a função `type()` para verificar os tipos dos objetos.

```python
numeros = [10, 20, 30]

iterador = iter(numeros)

print(type(numeros))
print(type(iterador))
```

**Resultado:**

```text
<class 'list'>
<class 'list_iterator'>
```

Isso demonstra que uma lista e seu iterador são objetos diferentes.

---

## 3. O método next()

O método `next()` é utilizado para solicitar o próximo elemento de um iterador.

Cada vez que chamamos `next()`, o iterador avança para o próximo elemento disponível.

### 3.1. Exemplo prático

```python
numeros = [10, 20, 30, 40]

iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
10
20
30
40
```

Observe que cada chamada de `next()` retorna um elemento diferente.

Isso acontece porque o iterador mantém seu estado interno, lembrando qual elemento deverá ser entregue na próxima solicitação.

### 3.2. O que acontece quando os elementos acabam?

Quando todos os elementos disponíveis já foram percorridos, uma nova chamada de `next()` gera uma exceção chamada `StopIteration`.

```python
numeros = [10, 20]

iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
10
20

StopIteration
```

Essa exceção indica que não existem mais elementos disponíveis naquele iterador.

**Importante:** `StopIteration` não representa necessariamente um erro no funcionamento do programa. É o mecanismo utilizado pelo Python para indicar o encerramento de uma iteração.

---

## 4. Como funciona o laço for internamente?

Uma das características mais interessantes do Python é que o laço `for` utiliza automaticamente os métodos `iter()` e `next()`.

Isso significa que não precisamos chamar esses métodos manualmente sempre que desejamos percorrer uma coleção.

### 4.1. Exemplo utilizando for

```python
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)
```

**Resultado:**

```text
10
20
30
```

### 4.2. Reproduzindo o funcionamento do for manualmente

O exemplo anterior pode ser reproduzido utilizando explicitamente `iter()` e `next()`.

```python
numeros = [10, 20, 30]

iterador = iter(numeros)

while True:

    try:
        numero = next(iterador)
        print(numero)

    except StopIteration:
        break
```

**Resultado:**

```text
10
20
30
```

### 4.3. Entendendo o código

1. Criamos uma lista chamada `numeros`.
2. Utilizamos `iter()` para obter seu iterador.
3. Criamos um laço `while` para solicitar elementos continuamente.
4. Utilizamos `next()` para obter o próximo elemento.
5. Quando não existem mais elementos, o iterador gera `StopIteration`.
6. O bloco `except` captura a exceção e encerra o laço com `break`.

**Conclusão:** o `for` automatiza esse processo, tornando a iteração mais simples e legível.

---

## 5. Protocolo de Iteração (Iterator Protocol)

O protocolo de iteração define as regras que um objeto precisa seguir para funcionar como iterador em Python.

Para que um objeto seja considerado um iterador, ele precisa implementar dois métodos:

### 5.1. __iter__()

O método `__iter__()` deve retornar o próprio iterador.

Ele é responsável por permitir que o objeto seja utilizado no mecanismo de iteração.

### 5.2. __next__()

O método `__next__()` deve retornar o próximo elemento disponível.

Quando não existem mais elementos, ele deve gerar a exceção `StopIteration`.

### 5.3. Exemplo prático

```python
numeros = [10, 20, 30]

iterador = iter(numeros)

# Utilizando os métodos especiais
print(iterador.__iter__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
```

**Resultado:**

```text
<list_iterator object at 0x...>
10
20
30
```

Observe que `iterador.__iter__()` retorna o próprio iterador.

Já cada chamada de `iterador.__next__()` retorna o próximo elemento disponível.

**Boa prática:** normalmente, utilizamos `iter()` e `next()` em vez de chamar diretamente `__iter__()` e `__next__()`. As funções convencionais representam a interface pública recomendada.

---

## 6. Criando um Iterador Personalizado

Além de utilizar os iteradores disponíveis nas estruturas nativas do Python, também podemos criar nossos próprios iteradores.

Para isso, podemos desenvolver uma classe que implemente os métodos `__iter__()` e `__next__()`.

Essa abordagem é útil quando precisamos controlar como os elementos são produzidos e em qual ordem serão disponibilizados.

### 6.1. Exemplo prático

Vamos criar um iterador que percorre uma sequência de números de 1 até 5.

```python
class Contador:

    def __init__(self, limite):
        self.limite = limite
        self.numero_atual = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.numero_atual <= self.limite:

            numero = self.numero_atual

            self.numero_atual += 1

            return numero

        raise StopIteration


# Criando o iterador
contador = Contador(5)

# Percorrendo os elementos
for numero in contador:
    print(numero)
```

**Resultado:**

```text
1
2
3
4
5
```

### 6.2. Entendendo o código

**1. Criamos a classe `Contador`.**

Ela será responsável por controlar a sequência de números.

**2. Criamos o construtor `__init__()`.**

Ele recebe o limite da contagem e inicializa o atributo `numero_atual` com o valor 1.

**3. Implementamos `__iter__()`.**

O método retorna `self`, ou seja, o próprio objeto será utilizado como iterador.

**4. Implementamos `__next__()`.**

Esse método verifica se o número atual ainda está dentro do limite estabelecido.

**5. Retornamos o número atual.**

Antes de retornar, incrementamos o contador para que a próxima chamada forneça o número seguinte.

**6. Encerramos a iteração.**

Quando o limite é ultrapassado, utilizamos `raise StopIteration` para informar que não existem mais elementos.

### 6.3. Por que utilizar iteradores personalizados?

Eles permitem criar mecanismos próprios de iteração, como:

- Contadores personalizados.
- Sequências matemáticas.
- Percursos de estruturas de dados.
- Leitura controlada de informações.
- Processamento de dados em etapas.

---

## 7. Iteradores e Estruturas de Dados

Diversas estruturas nativas do Python são iteráveis.

Isso significa que podemos obter seus iteradores utilizando `iter()`.

### 7.1. Listas

```python
lista = [10, 20, 30]

iterador = iter(lista)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
10
20
30
```

### 7.2. Tuplas

```python
tupla = ("Python", "Java", "JavaScript")

iterador = iter(tupla)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
Python
Java
JavaScript
```

### 7.3. Strings

Uma string também é iterável. Nesse caso, cada elemento retornado pelo iterador é um caractere.

```python
linguagem = "Python"

iterador = iter(linguagem)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
P
y
t
```

### 7.4. Dicionários

Por padrão, iterar sobre um dicionário significa percorrer suas chaves.

```python
pessoa = {
    "nome": "Matheus",
    "idade": 25,
    "profissao": "Analista"
}

iterador = iter(pessoa)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
nome
idade
profissao
```

Para percorrer os valores:

```python
iterador = iter(pessoa.values())

for valor in iterador:
    print(valor)
```

**Resultado:**

```text
Matheus
25
Analista
```

Para percorrer as chaves e os valores:

```python
iterador = iter(pessoa.items())

for chave, valor in iterador:
    print(f"{chave}: {valor}")
```

**Resultado:**

```text
nome: Matheus
idade: 25
profissao: Analista
```

### 7.5. Conjuntos (Sets)

Os conjuntos também são iteráveis.

```python
numeros = {10, 20, 30, 40}

iterador = iter(numeros)

for numero in iterador:
    print(numero)
```

**Observação:** conjuntos não garantem uma ordem de iteração específica. Não devemos depender de uma sequência determinada de elementos.

---

## 8. Iteradores são Consumíveis (Exhaustion)

Uma característica importante dos iteradores é que eles são consumidos à medida que seus elementos são percorridos.

Isso significa que, depois que todos os elementos são utilizados, o iterador não retorna automaticamente ao início.

### 8.1. Exemplo prático

```python
numeros = [10, 20, 30]

iterador = iter(numeros)

for numero in iterador:
    print(numero)

print("Segunda tentativa:")

for numero in iterador:
    print(numero)
```

**Resultado:**

```text
10
20
30

Segunda tentativa:
```

Observe que a segunda tentativa não apresenta nenhum elemento.

Isso acontece porque o iterador já foi completamente consumido.

### 8.2. Como reiniciar a iteração?

Para percorrer novamente a lista, podemos criar um novo iterador.

```python
numeros = [10, 20, 30]

iterador = iter(numeros)

for numero in iterador:
    print(numero)

# Criando um novo iterador
iterador = iter(numeros)

print("Percorrendo novamente:")

for numero in iterador:
    print(numero)
```

**Resultado:**

```text
10
20
30

Percorrendo novamente:
10
20
30
```

**Importante:** o iterador é consumido, mas o objeto original, nesse caso a lista, continua disponível para criar novos iteradores.

---

## 9. Iteradores e Economia de Memória

Os iteradores são especialmente úteis quando trabalhamos com grandes volumes de dados.

Isso acontece porque eles permitem processar elementos individualmente, sem necessariamente precisar armazenar uma nova coleção completa na memória.

### 9.1. Exemplo utilizando uma lista

```python
numeros = [numero for numero in range(1_000_001)]

for numero in numeros:
    print(numero)
```

Nesse exemplo, todos os números são armazenados na lista antes de começarmos a percorrê-los.

### 9.2. Exemplo utilizando um iterador

```python
numeros = iter(range(1_000_001))

for numero in numeros:
    print(numero)
```

Nesse caso, o objeto `range` fornece os números conforme são solicitados pelo iterador.

Não precisamos criar uma lista contendo todos os números.

**Importante:** o iterador não garante, por si só, que qualquer operação utilizará pouca memória. O consumo depende de como os dados são produzidos e armazenados. Entretanto, a iteração sob demanda pode reduzir significativamente a necessidade de memória.

---

## 10. Iteradores versus Iteráveis

É importante compreender as diferenças entre esses dois conceitos.

| Característica | Iterável | Iterador |
|---|---|---|
| Finalidade | Fornecer um iterador | Fornecer elementos |
| Método principal | `__iter__()` | `__iter__()` e `__next__()` |
| Mantém estado de consumo | Geralmente não | Sim |
| Pode ser percorrido novamente | Geralmente sim | Não sem reinicialização |
| Exemplo | Lista, tupla e string | `list_iterator` |

### Exemplo comparativo

```python
numeros = [10, 20, 30]

# Iterável
lista = numeros

# Iterador
iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
```

**Resultado:**

```text
10
20
```

A lista continua armazenando todos os elementos, enquanto o iterador mantém o estado de qual elemento deverá ser retornado em seguida.

---

## 11. Boas Práticas ao Trabalhar com Iteradores

Para trabalhar com iteradores de maneira eficiente, considere as seguintes recomendações:

1. **Utilize `for` sempre que possível:** ele simplifica a iteração e trata automaticamente o encerramento.
2. **Conheça `iter()` e `next()`:** entender esses métodos ajuda a compreender o funcionamento interno dos laços.
3. **Trate `StopIteration` corretamente:** especialmente quando estiver utilizando `next()` manualmente.
4. **Evite consumir iteradores desnecessariamente:** lembre-se de que eles não retornam automaticamente ao início.
5. **Prefira processar dados sob demanda:** isso pode reduzir o consumo de memória em operações com grandes volumes de informações.
6. **Implemente corretamente o protocolo de iteração:** iteradores personalizados precisam respeitar os métodos `__iter__()` e `__next__()`.
7. **Evite compartilhar iteradores consumíveis sem controle:** diferentes partes do programa podem acabar avançando o mesmo estado de iteração.

---

## 12. Exercícios para Praticar

A melhor maneira de consolidar o aprendizado é desenvolver pequenos programas utilizando iteradores.

### Exercício 1 — Iterando uma Lista

Crie uma lista contendo cinco nomes.

Depois:

- Utilize `iter()` para criar um iterador.
- Utilize `next()` para apresentar cada nome.
- Observe o que acontece quando todos os elementos forem consumidos.

**Objetivo:** compreender os métodos `iter()` e `next()`.

### Exercício 2 — Iterando um Dicionário

Crie um dicionário contendo informações de um funcionário:

- Nome.
- Idade.
- Cargo.
- Salário.

Depois, utilize um iterador para percorrer as chaves e outro para percorrer os valores.

**Objetivo:** praticar iteração em dicionários.

### Exercício 3 — Contador Personalizado

Crie uma classe chamada `Contador` que receba um número inicial e um número final.

O iterador deverá apresentar todos os números entre esses dois valores.

Exemplo:

```python
contador = Contador(1, 10)

for numero in contador:
    print(numero)
```

**Resultado esperado:**

```text
1
2
3
4
5
6
7
8
9
10
```

**Objetivo:** implementar `__iter__()` e `__next__()`.

### Exercício 4 — Sequência de Números Pares

Crie um iterador personalizado que apresente apenas números pares até determinado limite.

Exemplo:

```python
pares = NumerosPares(10)

for numero in pares:
    print(numero)
```

**Resultado esperado:**

```text
2
4
6
8
10
```

**Objetivo:** trabalhar com condições e controle de estado dentro de um iterador.

### Exercício 5 — Iterador de Transações Financeiras

Crie uma classe chamada `Transacoes` que receba uma lista de transações financeiras.

Cada transação deverá conter:

- Descrição.
- Valor.
- Tipo da operação.

O iterador deverá percorrer uma transação por vez e apresentar suas informações.

**Objetivo:** aplicar iteradores em um cenário relacionado ao mercado financeiro e à gestão de dados.

### Exercício 6 — Controle de Consumo

Crie um iterador que receba uma lista de produtos e apresente apenas os produtos cujo estoque seja maior que zero.

Exemplo:

```python
produtos = [
    {"nome": "Notebook", "estoque": 5},
    {"nome": "Mouse", "estoque": 0},
    {"nome": "Teclado", "estoque": 10}
]
```

**Resultado esperado:**

```text
Notebook
Teclado
```

**Objetivo:** praticar filtragem de dados durante a iteração.

---

## 13. Resumo Geral

Os iteradores são objetos responsáveis por fornecer elementos individualmente durante um processo de iteração.

Eles são fundamentais para o funcionamento de estruturas de repetição e permitem percorrer coleções e processar dados de maneira controlada.

Os principais conceitos estudados foram:

- **Iteração:** processo de percorrer elementos.
- **Iterable:** objeto capaz de fornecer um iterador.
- **Iterator:** objeto que fornece elementos um por vez.
- **iter():** função utilizada para obter um iterador.
- **next():** função utilizada para solicitar o próximo elemento.
- **StopIteration:** exceção que indica o encerramento da iteração.
- **__iter__():** método especial responsável por retornar um iterador.
- **__next__():** método especial responsável por fornecer o próximo elemento.
- **Iterator Protocol:** conjunto de regras que define o funcionamento dos iteradores.
- **Iterador personalizado:** objeto desenvolvido pelo programador para controlar a própria sequência de iteração.

### Conceito fundamental para memorizar

> Um iterável é um objeto capaz de fornecer um iterador. Já o iterador é responsável por entregar os elementos um de cada vez, mantendo o controle do estado da iteração até que todos os elementos sejam consumidos.

---

## 14. Documentação Oficial

Para aprofundar os conhecimentos, consulte a documentação oficial do Python:

- [Python — Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types): documentação sobre os tipos iteradores.
- [Python — Iterator Protocol](https://docs.python.org/3/library/stdtypes.html#typeiter): explicação sobre o protocolo de iteração.
- [Python — iter()](https://docs.python.org/3/library/functions.html#iter): documentação da função `iter()`.
- [Python — next()](https://docs.python.org/3/library/functions.html#next): documentação da função `next()`.
- [Python — for Statements](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement): funcionamento das estruturas de repetição.
- [Python — itertools](https://docs.python.org/3/library/itertools.html): biblioteca padrão com ferramentas para trabalhar com iteradores.