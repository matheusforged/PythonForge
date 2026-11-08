# Geradores em Python (Generators)

## 1. Introdução aos Geradores

Os **geradores (Generators)** são recursos do Python que permitem criar iteradores de maneira simples e eficiente, produzindo valores sob demanda, ou seja, um valor de cada vez.

Diferentemente de uma função convencional, que normalmente executa todas as suas instruções e retorna um resultado, uma função geradora pode pausar sua execução, entregar um valor e continuar exatamente de onde parou quando solicitada novamente.

Para criar um gerador, utilizamos a palavra-chave `yield`.

### Por que utilizar geradores?

Imagine que precisamos trabalhar com uma lista contendo 1 milhão de registros.

Uma abordagem convencional seria carregar todos esses registros na memória:

```python
def gerar_numeros():
    numeros = []

    for numero in range(1000000):
        numeros.append(numero)

    return numeros
```

Nesse exemplo, a função cria uma lista contendo todos os números antes de retornar o resultado.

Uma alternativa seria utilizar um gerador:

```python
def gerar_numeros():
    for numero in range(1000000):
        yield numero
```

Agora, os números são produzidos individualmente, conforme forem solicitados.

Isso pode reduzir significativamente o consumo de memória, principalmente quando trabalhamos com grandes volumes de dados.

**Principais vantagens:**

- Economia de memória.
- Processamento sob demanda.
- Código mais simples para criar iteradores.
- Facilidade para trabalhar com grandes conjuntos de dados.
- Possibilidade de criar sequências infinitas.
- Processamento eficiente de arquivos e fluxos de informações.

---

## 2. A palavra-chave `yield`

A palavra-chave `yield` é o principal elemento dos geradores.

Ela funciona de maneira semelhante ao `return`, pois entrega um valor ao código que chamou a função. Entretanto, existe uma diferença fundamental:

- `return`: encerra a execução da função.
- `yield`: entrega um valor e suspende temporariamente a execução da função.

Observe:

```python
def exemplo():
    print("Primeira execução")

    yield 10

    print("Segunda execução")

    yield 20

    print("Terceira execução")

    yield 30
```

Quando chamamos a função:

```python
resultado = exemplo()

print(resultado)
```

O Python não executa imediatamente o conteúdo da função. Ele retorna um objeto gerador.

Para começar a execução, precisamos solicitar um valor:

```python
print(next(resultado))
```

Saída:

```text
Primeira execução
10
```

Ao solicitar novamente:

```python
print(next(resultado))
```

Saída:

```text
Segunda execução
20
```

E mais uma vez:

```python
print(next(resultado))
```

Saída:

```text
Terceira execução
30
```

A execução fica suspensa em cada `yield`, preservando o estado da função.

### 2.1. Diferença entre `yield` e `return`

Observe a comparação:

**Utilizando `return`:**

```python
def numeros():
    return 10
    return 20
    return 30
```

A função encerra sua execução no primeiro `return`. Os demais comandos nunca serão alcançados.

**Utilizando `yield`:**

```python
def numeros():
    yield 10
    yield 20
    yield 30
```

A função entrega os três valores individualmente, conforme forem solicitados.

| Característica | `return` | `yield` |
|---|---|---|
| Entrega um valor | Sim | Sim |
| Encerra a função | Sim | Não imediatamente |
| Suspende a execução | Não | Sim |
| Preserva o estado | Não | Sim |
| Permite produzir vários valores | Não, em uma única execução | Sim |

---

## 3. Como funciona a execução de um gerador?

Uma função geradora não executa seu conteúdo no momento em que é chamada.

Ela retorna um objeto gerador, que começa a executar quando algum valor é solicitado.

Vamos acompanhar:

```python
def contar():
    print("Iniciando...")

    yield 1

    print("Continuando...")

    yield 2

    print("Finalizando...")
```

Criando o gerador:

```python
contador = contar()

print("Gerador criado")
```

Saída:

```text
Gerador criado
```

Observe que a mensagem `"Iniciando..."` ainda não apareceu.

Isso acontece porque a função ainda não começou a executar.

Agora:

```python
print(next(contador))
```

Saída:

```text
Iniciando...
1
```

Na próxima solicitação:

```python
print(next(contador))
```

Saída:

```text
Continuando...
2
```

Na terceira solicitação:

```python
next(contador)
```

Saída:

```text
Finalizando...
```

A função termina sem produzir outro valor.

Se tentarmos solicitar mais um valor:

```python
next(contador)
```

O Python lançará uma exceção:

```text
StopIteration
```

Isso acontece porque o gerador já foi totalmente consumido.

### 3.1. O que é `StopIteration`?

`StopIteration` é a exceção utilizada pelo protocolo de iteração do Python para indicar que não existem mais valores disponíveis.

Quando um gerador termina naturalmente, essa exceção sinaliza o encerramento da sequência.

Normalmente, não precisamos tratá-la manualmente, pois o próprio `for` sabe identificar quando a iteração terminou.

---

## 4. Utilizando geradores com `for`

Uma das maneiras mais práticas de consumir um gerador é utilizando um laço `for`.

Observe:

```python
def gerar_numeros():
    yield 10
    yield 20
    yield 30
    yield 40
```

Agora:

```python
for numero in gerar_numeros():
    print(numero)
```

Saída:

```text
10
20
30
40
```

O `for` solicita automaticamente os próximos valores até que o gerador termine.

Isso significa que não precisamos utilizar `next()` manualmente em todas as situações.

### 4.1. Criando uma sequência numérica

Podemos utilizar um gerador para produzir números dentro de um intervalo.

```python
def contar_ate(limite):
    numero = 1

    while numero <= limite:
        yield numero
        numero += 1
```

Utilização:

```python
for numero in contar_ate(5):
    print(numero)
```

Saída:

```text
1
2
3
4
5
```

Perceba que o gerador mantém o valor da variável `numero` entre uma suspensão e outra.

---

## 5. Geradores e Iteradores

Os geradores estão diretamente relacionados ao conteúdo estudado anteriormente sobre iteradores.

Todo gerador é um iterador, mas nem todo iterador é um gerador.

Um gerador já implementa automaticamente o protocolo de iteração, incluindo os métodos `__iter__()` e `__next__()`.

Compare:

**Criando um iterador manualmente:**

```python
class Contador:
    def __init__(self, limite):
        self.numero = 1
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero > self.limite:
            raise StopIteration

        valor = self.numero
        self.numero += 1

        return valor
```

**Criando um gerador:**

```python
def contador(limite):
    numero = 1

    while numero <= limite:
        yield numero
        numero += 1
```

Os dois exemplos podem produzir a mesma sequência.

Entretanto, o gerador permite realizar a mesma tarefa com menos código, pois o Python administra automaticamente o estado da execução.

### Comparação

| Característica | Iterador personalizado | Gerador |
|---|---|---|
| Implementação manual | Geralmente necessária | Não |
| Utiliza `yield` | Não necessariamente | Sim |
| Implementa o protocolo de iteração | Sim | Automaticamente |
| Preserva o estado | Sim, conforme a implementação | Sim, automaticamente |
| Complexidade | Pode ser maior | Geralmente menor |

---

## 6. Expressões Geradoras (Generator Expressions)

Além das funções geradoras, Python permite criar geradores utilizando expressões geradoras.

Elas possuem uma sintaxe semelhante às *list comprehensions*, mas utilizam parênteses em vez de colchetes.

**List comprehension:**

```python
numeros = [numero * 2 for numero in range(5)]

print(numeros)
```

Resultado:

```text
[0, 2, 4, 6, 8]
```

Nesse caso, todos os valores são calculados e armazenados em uma lista.

**Generator expression:**

```python
numeros = (numero * 2 for numero in range(5))

print(numeros)
```

O resultado será um objeto gerador, e não uma lista.

Para consumir os valores:

```python
for numero in numeros:
    print(numero)
```

Saída:

```text
0
2
4
6
8
```

### 6.1. Diferença entre List Comprehension e Generator Expression

| Característica | List Comprehension | Generator Expression |
|---|---|---|
| Sintaxe | `[]` | `()` |
| Cria uma lista | Sim | Não |
| Produz valores sob demanda | Não | Sim |
| Armazena todos os resultados | Sim | Não |
| Consumo de memória | Geralmente maior | Geralmente menor |

### 6.2. Exemplo prático

Imagine que precisamos calcular o quadrado de 1 milhão de números.

Com uma lista:

```python
quadrados = [numero ** 2 for numero in range(1000000)]
```

Com um gerador:

```python
quadrados = (numero ** 2 for numero in range(1000000))
```

A segunda abordagem não precisa armazenar todos os resultados simultaneamente.

**Atenção:** se utilizarmos `list()` para transformar o gerador em uma lista, todos os valores serão materializados na memória:

```python
quadrados = list(numero ** 2 for numero in range(1000000))
```

Portanto, perdemos boa parte da vantagem de economia de memória.

---

## 7. Geradores e Economia de Memória

Uma das aplicações mais importantes dos geradores é o processamento de grandes volumes de dados.

Imagine que temos uma base contendo milhões de transações financeiras.

Carregar todos os registros na memória pode ser desnecessário, principalmente quando precisamos analisar cada registro individualmente.

Podemos utilizar um gerador para processar os dados gradualmente.

### 7.1. Exemplo com transações financeiras

```python
def gerar_transacoes():
    transacoes = [
        {"id": 1, "valor": 1500},
        {"id": 2, "valor": 2500},
        {"id": 3, "valor": 800},
        {"id": 4, "valor": 3200}
    ]

    for transacao in transacoes:
        yield transacao
```

Agora podemos percorrer as transações:

```python
for transacao in gerar_transacoes():
    print(transacao)
```

Saída:

```text
{'id': 1, 'valor': 1500}
{'id': 2, 'valor': 2500}
{'id': 3, 'valor': 800}
{'id': 4, 'valor': 3200}
```

### 7.2. Filtrando transações

Podemos adicionar condições dentro do gerador.

```python
def filtrar_transacoes():
    transacoes = [
        {"id": 1, "valor": 1500},
        {"id": 2, "valor": 2500},
        {"id": 3, "valor": 800},
        {"id": 4, "valor": 3200}
    ]

    for transacao in transacoes:
        if transacao["valor"] > 2000:
            yield transacao
```

Utilização:

```python
for transacao in filtrar_transacoes():
    print(transacao)
```

Resultado:

```text
{'id': 2, 'valor': 2500}
{'id': 4, 'valor': 3200}
```

O gerador entrega somente os registros que atendem à condição.

**Observação:** nesse exemplo, a lista original ainda é criada dentro da função. Em uma aplicação real, para aproveitar melhor a economia de memória, os registros poderiam ser lidos diretamente de um arquivo, banco de dados ou fluxo de dados.

---

## 8. Geradores para leitura de arquivos

Geradores também são úteis quando precisamos trabalhar com arquivos grandes.

Imagine um arquivo de texto com milhões de linhas.

Uma alternativa é utilizar um gerador para entregar uma linha de cada vez.

```python
def ler_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            yield linha.strip()
```

Utilização:

```python
for linha in ler_arquivo("transacoes.txt"):
    print(linha)
```

Nesse exemplo:

1. O arquivo é aberto.
2. O Python percorre suas linhas.
3. Cada linha é entregue por meio de `yield`.
4. A execução fica suspensa até a próxima solicitação.
5. Quando o arquivo termina, o gerador é encerrado.
6. O bloco `with` fecha o arquivo.

Essa abordagem evita carregar todo o conteúdo do arquivo na memória de uma só vez.

**Boa prática:** utilize `with` para abrir arquivos. Assim, o recurso é fechado corretamente quando a execução sai do bloco, inclusive quando ocorre uma exceção.

---

## 9. Geradores Infinitos

Outra aplicação interessante é a criação de sequências infinitas.

Como os geradores produzem valores sob demanda, podemos criar uma sequência que não possui um limite definido.

Observe:

```python
def numeros_infinitos():
    numero = 0

    while True:
        yield numero
        numero += 1
```

Esse gerador continuará produzindo números enquanto receber solicitações.

Utilização:

```python
gerador = numeros_infinitos()

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
```

Resultado:

```text
0
1
2
3
```

**Atenção:** não utilize diretamente um `for` sem limite em um gerador infinito, pois a execução nunca terminará naturalmente.

Podemos limitar a quantidade de valores utilizando `itertools.islice`:

```python
from itertools import islice

for numero in islice(numeros_infinitos(), 10):
    print(numero)
```

Nesse exemplo, serão produzidos somente os dez primeiros números.

---

## 10. Utilizando `yield from`

A palavra-chave `yield from` permite que um gerador delegue a produção de valores para outro iterável.

Isso é especialmente útil quando precisamos combinar diferentes sequências.

Observe:

```python
def gerar_numeros():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
```

Utilização:

```python
for numero in gerar_numeros():
    print(numero)
```

Saída:

```text
1
2
3
4
5
6
```

O `yield from` percorre o iterável informado e entrega seus valores individualmente.

### 10.1. Comparação com `yield`

Sem `yield from`:

```python
def gerar_numeros():
    for numero in [1, 2, 3]:
        yield numero

    for numero in [4, 5, 6]:
        yield numero
```

Com `yield from`:

```python
def gerar_numeros():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
```

As duas versões produzem a mesma sequência.

### 10.2. Utilizando subgeradores

Também podemos delegar a execução para outras funções geradoras.

```python
def gerar_nomes():
    yield "Ana"
    yield "Carlos"

def gerar_idades():
    yield 25
    yield 30

def gerar_dados():
    yield from gerar_nomes()
    yield from gerar_idades()
```

Utilização:

```python
for dado in gerar_dados():
    print(dado)
```

Resultado:

```text
Ana
Carlos
25
30
```

---

## 11. Recursos avançados: `send()`, `throw()` e `close()`

Geradores possuem métodos adicionais que permitem controlar sua execução.

Esses recursos são mais avançados, mas ajudam a compreender como os geradores funcionam internamente.

### 11.1. Método `send()`

O método `send()` permite enviar um valor para um gerador suspenso.

Esse valor é recebido pela expressão `yield` na qual o gerador está pausado.

Exemplo:

```python
def receber_dados():
    while True:
        valor = yield
        print(f"Valor recebido: {valor}")
```

Utilização:

```python
gerador = receber_dados()

next(gerador)

gerador.send(100)
gerador.send(200)
gerador.send(300)
```

Resultado:

```text
Valor recebido: 100
Valor recebido: 200
Valor recebido: 300
```

Observe que utilizamos `next()` antes do primeiro `send()`.

Isso acontece porque o gerador precisa começar a executar e alcançar a expressão `yield` antes de receber um valor.

O primeiro envio precisa ser `None`, caso seja utilizado `send()` diretamente para iniciar o gerador.

### 11.2. Método `throw()`

O método `throw()` permite lançar uma exceção na posição em que o gerador está suspenso.

Exemplo:

```python
def exemplo():
    try:
        yield 1
        yield 2

    except ValueError:
        print("Uma exceção foi recebida!")
```

Utilização:

```python
gerador = exemplo()

print(next(gerador))

gerador.throw(ValueError)
```

Resultado:

```text
1
Uma exceção foi recebida!
```

O gerador recebe a exceção e pode tratá-la internamente.

### 11.3. Método `close()`

O método `close()` encerra um gerador.

Ele injeta uma exceção especial chamada `GeneratorExit` na execução suspensa.

Isso permite que blocos `finally` sejam executados para liberar recursos.

Exemplo:

```python
def exemplo():
    try:
        yield 1
        yield 2

    finally:
        print("Gerador encerrado!")
```

Utilização:

```python
gerador = exemplo()

print(next(gerador))

gerador.close()
```

Resultado:

```text
1
Gerador encerrado!
```

Esses métodos são especialmente úteis em aplicações mais avançadas, como processamento de fluxos e gerenciamento de recursos.

---

## 12. Geradores e processamento de dados

Geradores podem ser combinados com funções e bibliotecas do Python para criar pipelines de processamento.

Um pipeline é uma sequência de etapas em que os dados passam por diferentes operações.

Imagine o seguinte fluxo:

1. Receber transações.
2. Filtrar transações aprovadas.
3. Calcular valores.
4. Entregar os resultados.

Podemos implementar isso utilizando geradores.

```python
def gerar_transacoes():
    transacoes = [
        {"id": 1, "valor": 1000, "status": "aprovada"},
        {"id": 2, "valor": 500, "status": "cancelada"},
        {"id": 3, "valor": 2000, "status": "aprovada"},
        {"id": 4, "valor": 800, "status": "aprovada"}
    ]

    for transacao in transacoes:
        yield transacao


def filtrar_aprovadas(transacoes):
    for transacao in transacoes:
        if transacao["status"] == "aprovada":
            yield transacao


def calcular_taxa(transacoes):
    for transacao in transacoes:
        taxa = transacao["valor"] * 0.02

        yield {
            "id": transacao["id"],
            "valor": transacao["valor"],
            "taxa": taxa
        }
```

Agora podemos conectar as etapas:

```python
transacoes = gerar_transacoes()

aprovadas = filtrar_aprovadas(transacoes)

resultado = calcular_taxa(aprovadas)

for transacao in resultado:
    print(transacao)
```

Resultado:

```text
{'id': 1, 'valor': 1000, 'taxa': 20.0}
{'id': 3, 'valor': 2000, 'taxa': 40.0}
{'id': 4, 'valor': 800, 'taxa': 16.0}
```

Observe que os dados passam pelas etapas conforme são solicitados.

Não precisamos criar uma lista intermediária para armazenar cada resultado.

Esse padrão é muito útil em processamento de dados, automações e aplicações financeiras.

**Importante:** o exemplo utiliza uma lista pequena apenas para simular a origem dos dados. Em uma aplicação real, poderíamos substituir essa origem por um arquivo, consulta ao banco de dados ou fluxo externo.

---

## 13. Limitações dos Geradores

Apesar das vantagens, geradores possuem algumas limitações.

### 13.1. São consumíveis

Um gerador normalmente pode ser percorrido uma única vez.

```python
def gerar_numeros():
    yield 1
    yield 2
    yield 3

numeros = gerar_numeros()

for numero in numeros:
    print(numero)

print("Segundo percurso:")

for numero in numeros:
    print(numero)
```

O segundo percurso não apresentará valores, porque o gerador já foi consumido.

Se precisarmos percorrer novamente, devemos criar um novo gerador:

```python
numeros = gerar_numeros()

for numero in numeros:
    print(numero)
```

### 13.2. Não permitem acesso por índice

Uma lista permite acessar elementos diretamente:

```python
numeros = [10, 20, 30]

print(numeros[1])
```

Resultado:

```text
20
```

Um gerador não permite esse tipo de acesso:

```python
numeros = (numero for numero in [10, 20, 30])

print(numeros[1])
```

Isso gera um `TypeError`, pois geradores não implementam acesso por índice.

Se realmente precisarmos de acesso aleatório, podemos transformar o gerador em uma lista:

```python
numeros = list(numeros)
```

Entretanto, isso consome o gerador e armazena todos os valores na memória.

### 13.3. Não possuem tamanho diretamente disponível

Não podemos utilizar diretamente `len()` em um gerador:

```python
numeros = (numero for numero in range(10))

print(len(numeros))
```

O código gera um `TypeError`.

Isso acontece porque o gerador não precisa conhecer antecipadamente a quantidade total de elementos que produzirá.

---

## 14. Boas práticas ao utilizar Geradores

Para trabalhar corretamente com geradores, considere as seguintes recomendações:

1. **Utilize geradores para grandes volumes de dados:** principalmente quando não precisamos armazenar todos os resultados simultaneamente.

2. **Prefira expressões geradoras quando forem simples:** elas deixam o código mais compacto.

3. **Utilize funções geradoras para lógicas mais complexas:** quando existem várias condições, cálculos ou etapas de processamento.

4. **Evite converter geradores em listas sem necessidade:** isso pode eliminar a vantagem de economia de memória.

5. **Tenha atenção ao consumo:** lembre-se de que um gerador não reinicia automaticamente.

6. **Utilize `yield from` para delegar sequências:** isso pode simplificar a composição de geradores.

7. **Utilize `with` para trabalhar com arquivos:** assim, os recursos são fechados corretamente.

8. **Evite geradores infinitos sem controle:** utilize limites quando precisar consumir apenas uma quantidade específica de valores.

9. **Escolha a estrutura adequada:** listas são melhores quando precisamos acessar elementos repetidamente ou por índice; geradores são úteis quando queremos produzir valores sob demanda.

---

## 15. Exercícios Práticos

Os exercícios abaixo foram organizados em ordem crescente de dificuldade.

Tente resolver cada problema antes de consultar uma solução.

### Exercício 1 — Gerador de números

Crie uma função geradora chamada `gerar_numeros()` que produza os números de 1 até 10.

Requisitos:

- Utilize `yield`.
- Utilize um laço `for`.
- Imprima os valores gerados.

### Exercício 2 — Números pares

Crie uma função geradora chamada `gerar_pares(limite)`.

Requisitos:

- Receba um limite como argumento.
- Gere somente os números pares.
- Utilize `yield`.
- Teste com o limite 20.

Resultado esperado:

```text
2
4
6
8
10
12
14
16
18
20
```

### Exercício 3 — Quadrados de números

Crie uma expressão geradora que produza o quadrado dos números de 1 até 10.

Requisitos:

- Utilize uma expressão geradora.
- Não utilize list comprehension.
- Percorra os resultados com `for`.

### Exercício 4 — Gerador de transações financeiras

Crie uma função geradora chamada `gerar_transacoes()`.

Utilize os seguintes registros:

```python
transacoes = [
    {"id": 1, "valor": 1500},
    {"id": 2, "valor": 2500},
    {"id": 3, "valor": 800},
    {"id": 4, "valor": 3200},
    {"id": 5, "valor": 1200}
]
```

Requisitos:

- Produza cada transação individualmente.
- Utilize `yield`.
- Percorra as transações utilizando `for`.

### Exercício 5 — Filtrando transações

Aproveite o exercício anterior e crie outro gerador chamado `filtrar_transacoes()`.

Requisitos:

- Receba um iterável de transações.
- Retorne somente as transações com valores superiores a R$ 1.500.
- Utilize `yield`.
- Não crie uma lista para armazenar os resultados filtrados.

### Exercício 6 — Processamento de arquivos

Crie uma função geradora chamada `ler_linhas()`.

Requisitos:

- Receba o caminho de um arquivo.
- Abra o arquivo utilizando `with`.
- Produza uma linha por vez.
- Remova espaços e quebras de linha utilizando `strip()`.

### Exercício 7 — Gerador infinito

Crie um gerador chamado `contador_infinito()`.

Requisitos:

- Comece a contagem em 1.
- Utilize `while True`.
- Produza números utilizando `yield`.
- Utilize `itertools.islice()` para apresentar somente os primeiros 15 valores.

### Exercício 8 — Pipeline de processamento

Crie um pequeno pipeline utilizando três geradores:

1. `gerar_vendas()`: produz registros de vendas.
2. `filtrar_vendas()`: mantém somente vendas aprovadas.
3. `calcular_comissao()`: calcula uma comissão de 5% sobre cada venda aprovada.

Requisitos:

- Utilize `yield` nas três funções.
- Conecte os geradores sem criar listas intermediárias.
- Apresente o resultado final utilizando `for`.

---

## 16. Resumo Geral

| Conceito | Descrição |
|---|---|
| Generator | Objeto que produz valores sob demanda e funciona como um iterador |
| `yield` | Entrega um valor e suspende a execução |
| `return` | Encerra a função |
| `next()` | Solicita o próximo valor |
| `StopIteration` | Indica que não existem mais valores |
| Generator Expression | Cria um gerador utilizando uma expressão com parênteses |
| `yield from` | Delega a produção de valores para outro iterável |
| `send()` | Envia um valor para um gerador suspenso |
| `throw()` | Injeta uma exceção na execução suspensa |
| `close()` | Encerra o gerador |
| Lazy Evaluation | Avaliação sob demanda, quando os valores são solicitados |

### Diferença entre os três conteúdos estudados

| Conceito | Principal finalidade |
|---|---|
| Iteradores | Percorrer elementos de uma sequência |
| Geradores | Criar iteradores de maneira simples e produzir valores sob demanda |
| Decoradores | Modificar ou estender o comportamento de funções e métodos |

Os três recursos fazem parte de um conjunto importante de ferramentas da linguagem Python e aparecem frequentemente em projetos profissionais.

---

## 17. Documentação Oficial e Recursos Complementares

Para aprofundar seus conhecimentos, consulte a documentação oficial do Python:

- [Generator Expressions — Python Documentation](https://docs.python.org/3/reference/expressions.html#generator-expressions)
- [Yield Expressions — Python Documentation](https://docs.python.org/3/reference/expressions.html#yield-expressions)
- [Generator Types — Python Documentation](https://docs.python.org/3/library/stdtypes.html#generator-types)
- [Iterator Types — Python Documentation](https://docs.python.org/3/library/stdtypes.html#typeiter)
- [itertools — Functions creating iterators](https://docs.python.org/3/library/itertools.html)

---

## 18. Conclusão

Os geradores são especialmente importantes quando precisamos trabalhar com dados de maneira eficiente, evitando carregar grandes quantidades de informações na memória.

Ao dominar `yield`, expressões geradoras e a composição de diferentes geradores, você passa a ter mais recursos para desenvolver programas que processam informações gradualmente.

Esse conhecimento é particularmente útil em:

- Automação de processos.
- Análise de dados.
- Leitura e processamento de arquivos.
- Integração com bancos de dados.
- Processamento de transações financeiras.
- Desenvolvimento de aplicações que trabalham com grandes volumes de informações.

**Recomendação de estudo:** pratique primeiro os exercícios de 1 a 5. Depois, avance para leitura de arquivos, geradores infinitos e pipelines de processamento. Assim, você consolida os fundamentos antes de trabalhar com aplicações mais complexas.