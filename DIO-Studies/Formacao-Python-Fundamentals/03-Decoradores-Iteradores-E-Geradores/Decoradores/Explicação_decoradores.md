# Decoradores em Python (Decorators)

## 1. Introdução aos Decoradores

Os **decoradores (Decorators)** são um recurso do Python que permite modificar ou ampliar o comportamento de funções e métodos sem precisar alterar diretamente o código original.

Em termos simples, um decorador recebe uma função como argumento, adiciona alguma funcionalidade e retorna uma nova função com esse comportamento.

Esse mecanismo permite adicionar funcionalidades como:

- Registro de operações (Logging).
- Controle de tempo de execução.
- Autenticação e autorização.
- Validação de dados.
- Controle de acesso.
- Monitoramento de funções.
- Cache de resultados.

Os decoradores são muito utilizados em projetos profissionais, especialmente em frameworks como Flask, Django e FastAPI.

### 1.1. Como funcionam os decoradores?

Para compreender os decoradores, primeiro precisamos entender três características importantes do Python:

1. **Funções são objetos:** podemos armazenar funções em variáveis, passá-las como argumentos e retorná-las de outras funções.
2. **Funções podem ser definidas dentro de outras funções:** isso permite criar funções internas.
3. **Closures:** uma função interna pode acessar variáveis definidas no escopo da função externa, mesmo depois que a função externa termina sua execução.

Esses três conceitos formam a base para compreender o funcionamento dos decoradores.

---

## 2. Funções como Objetos (First-Class Functions)

Em Python, as funções são consideradas objetos de primeira classe (*First-Class Functions*).

Isso significa que uma função pode ser tratada como qualquer outro objeto da linguagem.

Podemos, por exemplo:

- Armazenar uma função em uma variável.
- Passar uma função como argumento para outra função.
- Retornar uma função como resultado de outra função.

### 2.1. Armazenando funções em variáveis

```python
def saudacao():
    print("Olá! Seja bem-vindo.")


# Armazenando a função em uma variável
mensagem = saudacao

# Executando a função através da variável
mensagem()
```

**Resultado:**

```text
Olá! Seja bem-vindo.
```

Observe que utilizamos `saudacao`, sem os parênteses, para armazenar a referência da função.

Se utilizássemos `saudacao()`, estaríamos executando a função imediatamente.

### 2.2. Passando funções como argumentos

Também podemos enviar uma função como argumento para outra função.

```python
def saudacao():
    print("Olá! Seja bem-vindo.")


def executar_funcao(funcao):
    funcao()


# Passando a função como argumento
executar_funcao(saudacao)
```

**Resultado:**

```text
Olá! Seja bem-vindo.
```

Nesse exemplo, a função `executar_funcao()` recebe outra função como parâmetro e executa seu conteúdo.

Esse comportamento é fundamental para entender os decoradores.

---

## 3. Funções Internas (Nested Functions)

As funções internas são funções declaradas dentro de outras funções.

Elas permitem organizar funcionalidades auxiliares e criar comportamentos que dependem de uma função externa.

### 3.1. Exemplo prático

```python
def funcao_externa():

    print("Executando a função externa.")

    def funcao_interna():
        print("Executando a função interna.")

    funcao_interna()


funcao_externa()
```

**Resultado:**

```text
Executando a função externa.
Executando a função interna.
```

### 3.2. Entendendo o código

1. Criamos a função `funcao_externa()`.
2. Dentro dela, definimos a função `funcao_interna()`.
3. A função interna possui uma mensagem própria.
4. Ao executar a função externa, ela também executa a função interna.

**Importante:** funções internas podem acessar variáveis definidas no escopo da função externa.

Esse comportamento está relacionado ao conceito de Closure.

---

## 4. Closures em Python

Uma **Closure** acontece quando uma função interna mantém acesso a variáveis do escopo de uma função externa, mesmo depois que a função externa já terminou sua execução.

Esse recurso permite que uma função preserve informações do ambiente em que foi criada.

### 4.1. Exemplo prático

```python
def criar_saudacao(nome):

    def saudacao():
        print(f"Olá, {nome}! Seja bem-vindo.")

    return saudacao


# Criando uma função personalizada
mensagem = criar_saudacao("Matheus")

# Executando a função retornada
mensagem()
```

**Resultado:**

```text
Olá, Matheus! Seja bem-vindo.
```

### 4.2. Entendendo o código

1. Criamos a função externa `criar_saudacao()`, que recebe um nome.
2. Dentro dela, criamos a função interna `saudacao()`.
3. A função interna utiliza a variável `nome`, que pertence ao escopo externo.
4. A função externa retorna a função interna, sem executá-la.
5. Armazenamos a função retornada na variável `mensagem`.
6. Mesmo depois que `criar_saudacao()` termina, a função `mensagem()` ainda consegue acessar o nome armazenado.

Isso acontece porque a função retornada mantém uma referência ao ambiente necessário para sua execução.

**Relação com os decoradores:** essa característica permite que um decorador mantenha acesso à função original e a outras informações necessárias para modificar seu comportamento.

---

## 5. O que são Decoradores?

Agora que conhecemos os conceitos fundamentais, podemos entender melhor os decoradores.

Um decorador é uma função que recebe outra função, adiciona um comportamento e retorna uma função modificada ou envolvida por uma nova implementação.

A estrutura mais comum de um decorador utiliza:

- Uma função decoradora.
- Uma função interna responsável por envolver a função original.
- Uma chamada à função original.
- O retorno da função interna.

### 5.1. Estrutura básica

```python
def meu_decorador(funcao):

    def wrapper():
        # Código executado antes da função original
        print("Antes da execução.")

        # Executa a função original
        funcao()

        # Código executado depois da função original
        print("Depois da execução.")

    return wrapper
```

Observe que:

- `meu_decorador()` recebe uma função.
- `wrapper()` envolve a execução da função original.
- `funcao()` executa a função recebida.
- `return wrapper` retorna a nova função, sem executá-la.

A função `wrapper` é frequentemente utilizada nos decoradores para representar a função que envolve o comportamento original.

### 5.2. Aplicando o decorador manualmente

```python
def meu_decorador(funcao):

    def wrapper():
        print("Antes da execução.")

        funcao()

        print("Depois da execução.")

    return wrapper


def minha_funcao():
    print("Executando minha função original.")


# Aplicando o decorador manualmente
minha_funcao = meu_decorador(minha_funcao)

# Executando a função decorada
minha_funcao()
```

**Resultado:**

```text
Antes da execução.
Executando minha função original.
Depois da execução.
```

### 5.3. Entendendo o funcionamento

1. Criamos a função `minha_funcao()`.
2. Passamos essa função como argumento para `meu_decorador()`.
3. O decorador recebe a função original e cria a função interna `wrapper()`.
4. O decorador retorna `wrapper`.
5. A variável `minha_funcao` passa a referenciar a função retornada.
6. Quando executamos `minha_funcao()`, estamos executando `wrapper()`, que também executa a função original.

Observe que não modificamos o código interno de `minha_funcao()`. Apenas ampliamos seu comportamento.

---

## 6. Sintaxe @ (Açúcar Sintático)

Python oferece uma sintaxe especial para aplicar decoradores: o símbolo `@`.

Essa sintaxe é conhecida como *Decorator Syntax* e facilita a utilização dos decoradores.

### 6.1. Exemplo utilizando @

```python
def meu_decorador(funcao):

    def wrapper():
        print("Antes da execução.")

        funcao()

        print("Depois da execução.")

    return wrapper


@meu_decorador
def minha_funcao():
    print("Executando minha função original.")


minha_funcao()
```

**Resultado:**

```text
Antes da execução.
Executando minha função original.
Depois da execução.
```

### 6.2. Entendendo o símbolo @

Quando utilizamos:

```python
@meu_decorador
def minha_funcao():
    print("Olá!")
```

É equivalente a escrever:

```python
def minha_funcao():
    print("Olá!")


minha_funcao = meu_decorador(minha_funcao)
```

Ou seja, o símbolo `@` é apenas uma maneira mais simples e organizada de aplicar um decorador.

**Importante:** o decorador é aplicado durante a definição da função, e não a cada chamada dela.

---

## 7. Decoradores com Argumentos (*args e **kwargs)

Até agora, nossos decoradores funcionaram apenas com funções que não recebem parâmetros.

Mas e se quisermos decorar uma função que recebe argumentos?

Para isso, utilizamos `*args` e `**kwargs` na função interna `wrapper()`.

- `*args`: recebe uma quantidade variável de argumentos posicionais.
- `**kwargs`: recebe uma quantidade variável de argumentos nomeados.

Dessa maneira, o decorador consegue trabalhar com funções que possuem diferentes assinaturas.

### 7.1. Exemplo prático

```python
def meu_decorador(funcao):

    def wrapper(*args, **kwargs):

        print("Iniciando a execução...")

        resultado = funcao(*args, **kwargs)

        print("Finalizando a execução.")

        return resultado

    return wrapper


@meu_decorador
def somar(a, b):
    return a + b


resultado = somar(10, 20)

print(f"Resultado: {resultado}")
```

**Resultado:**

```text
Iniciando a execução...
Finalizando a execução.
Resultado: 30
```

### 7.2. Entendendo o código

1. O decorador recebe a função `somar()`.
2. A função `wrapper()` recebe os argumentos enviados para `somar()`.
3. `*args` e `**kwargs` permitem encaminhar os argumentos corretamente.
4. A função original é executada por meio de `funcao(*args, **kwargs)`.
5. O resultado é armazenado na variável `resultado`.
6. O decorador retorna o resultado original, preservando o funcionamento da função.

**Atenção:** não se esqueça de utilizar `return resultado` quando a função original precisar devolver algum valor. Sem isso, o resultado da função decorada será `None`.

---

## 8. Preservando os Metadados com functools.wraps

Quando decoramos uma função, ela passa a referenciar a função `wrapper()` retornada pelo decorador.

Isso pode causar um problema: os metadados da função original podem ser substituídos pelos metadados da função interna.

Entre os metadados afetados estão:

- Nome da função (`__name__`).
- Documentação (`__doc__`).
- Informações de identificação da função.

Para evitar esse problema, utilizamos `functools.wraps`.

### 8.1. Exemplo sem functools.wraps

```python
def meu_decorador(funcao):

    def wrapper():
        print("Executando função...")

        funcao()

    return wrapper


@meu_decorador
def minha_funcao():
    """Esta é a documentação da minha função."""
    print("Olá!")


print(minha_funcao.__name__)
print(minha_funcao.__doc__)
```

**Resultado:**

```text
wrapper
None
```

Observe que os metadados apresentados pertencem à função `wrapper`, e não à função original.

### 8.2. Exemplo utilizando functools.wraps

```python
from functools import wraps


def meu_decorador(funcao):

    @wraps(funcao)
    def wrapper():
        print("Executando função...")

        funcao()

    return wrapper


@meu_decorador
def minha_funcao():
    """Esta é a documentação da minha função."""
    print("Olá!")


print(minha_funcao.__name__)
print(minha_funcao.__doc__)
```

**Resultado:**

```text
minha_funcao
Esta é a documentação da minha função.
```

### 8.3. Por que utilizar wraps?

O decorador `@wraps(funcao)` preserva informações importantes da função original na função envolvente.

Isso facilita a depuração, a documentação e a utilização de ferramentas que dependem dos metadados das funções.

**Boa prática:** utilize `@wraps(funcao)` em decoradores que criam uma função interna `wrapper()`.

---

## 9. Aplicações Práticas dos Decoradores

Agora vamos conhecer algumas situações em que os decoradores podem ser utilizados em aplicações reais.

### 9.1. Logging (Registro de Operações)

O logging permite registrar informações sobre a execução de funções.

Podemos utilizar decoradores para registrar quando determinada função é executada.

```python
from functools import wraps
from datetime import datetime


def log_transacao(funcao):

    @wraps(funcao)
    def wrapper(*args, **kwargs):

        print(f"Executando: {funcao.__name__}")

        resultado = funcao(*args, **kwargs)

        print(f"Data e hora: {datetime.now()}")

        return resultado

    return wrapper


@log_transacao
def realizar_transferencia(valor):
    print(f"Transferência de R$ {valor:.2f} realizada.")


realizar_transferencia(1500)
```

**Resultado ilustrativo:**

```text
Executando: realizar_transferencia
Transferência de R$ 1500.00 realizada.
Data e hora: 2026-11-07 19:30:00
```

A data e a hora apresentadas são apenas ilustrativas.

Observe que o decorador registra informações sem precisar inserir o código de logging dentro da função original.

**Aplicação:** esse padrão pode ser utilizado para monitorar operações, registrar atividades e acompanhar a execução de funções.

Para aplicações reais, prefira utilizar o módulo `logging` da biblioteca padrão em vez de depender exclusivamente de `print()`.

### 9.2. Medindo o Tempo de Execução

Outra aplicação interessante é medir quanto tempo uma função demora para ser executada.

```python
from functools import wraps
from time import perf_counter


def medir_tempo(funcao):

    @wraps(funcao)
    def wrapper(*args, **kwargs):

        inicio = perf_counter()

        resultado = funcao(*args, **kwargs)

        fim = perf_counter()

        tempo_total = fim - inicio

        print(f"Tempo de execução: {tempo_total:.6f} segundos")

        return resultado

    return wrapper


@medir_tempo
def calcular():
    soma = sum(range(1_000_001))
    return soma


resultado = calcular()

print(f"Resultado: {resultado}")
```

**Resultado:**

```text
Tempo de execução: 0.035000 segundos
Resultado: 500000500000
```

O tempo apresentado é apenas ilustrativo, pois depende do computador e do ambiente de execução.

Nesse exemplo, utilizamos `perf_counter()`, que é apropriado para medir intervalos de tempo.

### 9.3. Validação de Dados

Os decoradores também podem ser utilizados para verificar condições antes de permitir a execução de determinada função.

```python
from functools import wraps


def validar_valor(funcao):

    @wraps(funcao)
    def wrapper(valor):

        if valor <= 0:
            print("Erro: o valor precisa ser positivo.")
            return None

        return funcao(valor)

    return wrapper


@validar_valor
def realizar_deposito(valor):
    print(f"Depósito de R$ {valor:.2f} realizado.")


realizar_deposito(500)
realizar_deposito(-100)
```

**Resultado:**

```text
Depósito de R$ 500.00 realizado.
Erro: o valor precisa ser positivo.
```

Nesse exemplo, o decorador verifica se o valor informado é positivo antes de executar a função original.

**Aplicação:** esse tipo de estrutura pode ajudar a centralizar validações comuns em sistemas financeiros e administrativos.

---

## 10. Decoradores que Recebem Argumentos

Até agora, nossos decoradores receberam diretamente uma função como argumento.

Entretanto, Python também permite criar decoradores que recebem parâmetros próprios.

Nesse caso, precisamos adicionar mais um nível de função.

A estrutura passa a ter três níveis:

1. **Função externa:** recebe os argumentos do decorador.
2. **Função decoradora:** recebe a função que será decorada.
3. **Função wrapper:** envolve a execução da função original.

### 10.1. Sintaxe

```python
def meu_decorador(parametro):

    def decorador(funcao):

        def wrapper(*args, **kwargs):

            # Código adicional

            return funcao(*args, **kwargs)

        return wrapper

    return decorador
```

### 10.2. Exemplo prático

Imagine que queremos criar um decorador que permita personalizar uma mensagem exibida antes da execução de uma função.

```python
from functools import wraps


def exibir_mensagem(mensagem):

    def decorador(funcao):

        @wraps(funcao)
        def wrapper(*args, **kwargs):

            print(mensagem)

            return funcao(*args, **kwargs)

        return wrapper

    return decorador


@exibir_mensagem("Iniciando processamento...")
def processar_dados():
    print("Dados processados com sucesso!")


processar_dados()
```

**Resultado:**

```text
Iniciando processamento...
Dados processados com sucesso!
```

Observe que agora podemos personalizar o comportamento do decorador por meio do argumento `mensagem`.

### 10.3. Entendendo o funcionamento

1. Chamamos `exibir_mensagem()` com o texto desejado.
2. Ela retorna a função `decorador()`.
3. A função `decorador()` recebe a função original.
4. O `wrapper()` adiciona a mensagem antes da execução.
5. A função original é executada normalmente.

Essa estrutura permite criar decoradores reutilizáveis e configuráveis.

---

## 11. Decoradores Aplicados a Métodos de Classes

Os decoradores também podem ser utilizados em métodos de classes.

Inclusive, Python possui alguns decoradores próprios para trabalhar com orientação a objetos.

Os mais conhecidos são:

- `@staticmethod`
- `@classmethod`
- `@property`

### 11.1. @staticmethod

O decorador `@staticmethod` permite criar métodos que pertencem à classe, mas não recebem automaticamente o parâmetro `self` nem `cls`.

São utilizados quando determinado comportamento está relacionado à classe, mas não precisa acessar os atributos de uma instância ou da própria classe.

```python
class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b


resultado = Calculadora.somar(10, 20)

print(resultado)
```

**Resultado:**

```text
30
```

### 11.2. @classmethod

O decorador `@classmethod` permite criar métodos que recebem automaticamente a própria classe como primeiro argumento, representado convencionalmente por `cls`.

São utilizados quando precisamos acessar ou modificar atributos da classe ou criar construtores alternativos.

```python
class Funcionario:

    empresa = "Empresa ABC"

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def alterar_empresa(cls, nova_empresa):
        cls.empresa = nova_empresa


Funcionario.alterar_empresa("Empresa XYZ")

print(Funcionario.empresa)
```

**Resultado:**

```text
Empresa XYZ
```

### 11.3. @property

O decorador `@property` permite acessar um método como se fosse um atributo.

É muito utilizado para implementar propriedades calculadas e controlar o acesso a determinados dados.

```python
class Produto:

    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade

    @property
    def valor_total(self):
        return self.preco * self.quantidade


produto = Produto(50, 3)

print(produto.valor_total)
```

**Resultado:**

```text
150
```

Observe que acessamos `valor_total` sem utilizar parênteses, mesmo sendo um método.

---

## 12. Diferenças entre os Decoradores

| Decorador | Finalidade |
|---|---|
| `@wraps` | Preservar os metadados da função original |
| `@staticmethod` | Criar métodos sem acesso automático à instância ou à classe |
| `@classmethod` | Criar métodos que recebem a classe como primeiro argumento |
| `@property` | Permitir acessar métodos como atributos |
| Decoradores personalizados | Adicionar ou modificar comportamentos de funções e métodos |

---

## 13. Boas Práticas ao Trabalhar com Decoradores

Para utilizar decoradores de maneira eficiente, considere as seguintes recomendações:

1. **Utilize `functools.wraps`:** preserve os metadados da função original.
2. **Utilize `*args` e `**kwargs`:** permita que o decorador trabalhe com funções que recebem diferentes argumentos.
3. **Preserve o retorno original:** retorne o resultado da função decorada quando necessário.
4. **Evite decoradores excessivamente complexos:** prefira separar responsabilidades.
5. **Utilize nomes descritivos:** facilite a compreensão do propósito de cada decorador.
6. **Evite modificar comportamentos inesperadamente:** o decorador deve adicionar funcionalidades de maneira previsível.
7. **Considere a ordem de aplicação:** quando existem vários decoradores, a ordem influencia o comportamento final.

### 13.1. Ordem de execução de múltiplos decoradores

É possível aplicar mais de um decorador à mesma função.

```python
def decorador_a(funcao):

    def wrapper():
        print("Executando decorador A.")
        return funcao()

    return wrapper


def decorador_b(funcao):

    def wrapper():
        print("Executando decorador B.")
        return funcao()

    return wrapper


@decorador_a
@decorador_b
def minha_funcao():
    print("Executando função original.")


minha_funcao()
```

**Resultado:**

```text
Executando decorador A.
Executando decorador B.
Executando função original.
```

Isso acontece porque:

```python
@decorador_a
@decorador_b
def minha_funcao():
    pass
```

É equivalente a:

```python
minha_funcao = decorador_a(decorador_b(minha_funcao))
```

O decorador mais próximo da função é aplicado primeiro, mas a execução dos wrappers começa pelo decorador mais externo.

---

## 14. Exercícios para Praticar

A melhor maneira de consolidar o aprendizado é desenvolver pequenos programas utilizando decoradores.

### Exercício 1 — Decorador de Mensagem

Crie um decorador chamado `mensagem_inicio` que exiba uma mensagem antes da execução de uma função.

Depois, crie uma função chamada `executar_tarefa()` e aplique o decorador.

**Objetivo:** compreender a estrutura básica de um decorador.

### Exercício 2 — Decorador de Logging

Crie um decorador chamado `registrar_log` que:

- Receba uma função.
- Exiba o nome da função executada.
- Registre a data e a hora da execução.
- Execute a função original.
- Preserve o retorno da função.

Utilize `datetime` e `functools.wraps`.

**Objetivo:** praticar logging, argumentos e preservação de metadados.

### Exercício 3 — Medidor de Tempo

Crie um decorador chamado `calcular_tempo` que meça quanto tempo uma função demora para executar.

Utilize `perf_counter()`.

Depois, aplique o decorador em uma função que realize uma operação matemática.

**Objetivo:** praticar medição de desempenho.

### Exercício 4 — Validação de Transações

Crie um decorador chamado `validar_transacao` que verifique se o valor informado em uma operação financeira é positivo.

Caso o valor seja negativo ou igual a zero, a função original não deverá ser executada.

Caso contrário, a operação deverá ser realizada normalmente.

**Objetivo:** aplicar decoradores em um cenário financeiro.

### Exercício 5 — Decorador com Argumentos

Crie um decorador chamado `repetir` que receba um número inteiro indicando quantas vezes uma função deverá ser executada.

Exemplo:

```python
@repetir(3)
def apresentar():
    print("Olá, mundo!")
```

**Resultado esperado:**

```text
Olá, mundo!
Olá, mundo!
Olá, mundo!
```

**Objetivo:** compreender decoradores parametrizados.

### Exercício 6 — Múltiplos Decoradores

Crie dois decoradores:

- `autenticacao`: deverá verificar se o usuário está autenticado.
- `registrar_acesso`: deverá registrar quando uma função for executada.

Depois, aplique os dois decoradores em uma função chamada `acessar_sistema()`.

**Objetivo:** compreender a ordem de aplicação e execução dos decoradores.

---

## 15. Resumo Geral

Os decoradores são recursos poderosos do Python que permitem ampliar ou modificar o comportamento de funções e métodos sem alterar diretamente sua implementação original.

Os principais conceitos estudados foram:

- **First-Class Functions:** funções podem ser tratadas como objetos.
- **Nested Functions:** funções podem ser definidas dentro de outras funções.
- **Closures:** funções internas podem preservar acesso a variáveis do escopo externo.
- **Decorators:** funções que recebem outras funções e retornam comportamentos modificados ou envolvidos.
- **Wrapper:** função interna responsável por envolver a execução da função original.
- **@:** sintaxe simplificada para aplicar decoradores.
- **\*args e \*\*kwargs:** permitem receber e encaminhar argumentos variáveis.
- **functools.wraps:** preserva os metadados da função original.
- **Decoradores parametrizados:** permitem configurar o comportamento do decorador.
- **Decoradores de métodos:** permitem adicionar comportamentos específicos em classes.

### Conceito fundamental para memorizar

> Um decorador é uma função que recebe outra função, adiciona funcionalidades ao seu comportamento e retorna uma nova função, permitindo ampliar o código sem modificar diretamente sua implementação original.

---

## 16. Documentação Oficial

Para aprofundar os conhecimentos, consulte a documentação oficial do Python:

- [Python — Decorators](https://docs.python.org/3/glossary.html#term-decorator): definição oficial de decoradores.
- [Python — Function Definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions): documentação sobre definições de funções e aplicação de decoradores.
- [Python — functools](https://docs.python.org/3/library/functools.html): documentação sobre ferramentas para funções, incluindo `wraps`.
- [Python — First-Class Objects](https://docs.python.org/3/glossary.html#term-first-class-object): conceito de objetos de primeira classe.
- [Python — Logging](https://docs.python.org/3/library/logging.html): documentação sobre registro de eventos e operações.