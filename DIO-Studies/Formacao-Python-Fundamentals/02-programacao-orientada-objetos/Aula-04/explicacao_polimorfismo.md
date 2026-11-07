# Polimorfismo em Python

## 1. Introdução ao Polimorfismo

O **polimorfismo** é um dos quatro pilares da Programação Orientada a Objetos (POO). O termo tem origem grega e significa literalmente "muitas formas".

Na programação, o polimorfismo permite que diferentes objetos utilizem métodos com o mesmo nome, mas apresentem comportamentos diferentes de acordo com a classe à qual pertencem.

Em outras palavras, podemos utilizar uma mesma interface para trabalhar com diferentes tipos de objetos, sem precisar conhecer todos os detalhes internos de cada um.

### Exemplo conceitual

Imagine um sistema que trabalha com diferentes tipos de animais.

Todos os animais possuem a capacidade de emitir sons, mas cada um emite um som diferente:

- Cachorro: late.
- Gato: mia.
- Vaca: muge.

Embora todos utilizem um método chamado `emitir_som()`, o comportamento muda de acordo com o objeto.

Essa capacidade de apresentar diferentes comportamentos por meio de uma mesma interface é o que chamamos de polimorfismo.

### Principais vantagens do polimorfismo

- **Flexibilidade:** permite trabalhar com diferentes tipos de objetos utilizando uma interface comum.
- **Reutilização de código:** evita a necessidade de criar estruturas específicas para cada tipo de objeto.
- **Extensibilidade:** facilita a inclusão de novas classes sem modificar necessariamente o código existente.
- **Organização:** reduz a quantidade de condicionais utilizadas para identificar tipos de objetos.
- **Manutenção:** permite modificar comportamentos individualmente sem comprometer a estrutura geral do programa.

---

## 2. Polimorfismo por Sobrescrita de Métodos (Method Overriding)

Uma das formas mais comuns de implementar polimorfismo em Python é por meio da sobrescrita de métodos.

Isso acontece quando uma classe filha redefine um método que já existe na classe pai, oferecendo uma implementação específica.

### 2.1. Exemplo prático

Imagine um sistema que trabalha com diferentes tipos de animais.

```python
# Classe pai
class Animal:

    def emitir_som(self):
        print("O animal está emitindo um som.")


# Classe filha
class Cachorro(Animal):

    def emitir_som(self):
        print("Au au!")


# Classe filha
class Gato(Animal):

    def emitir_som(self):
        print("Miau!")


# Classe filha
class Vaca(Animal):

    def emitir_som(self):
        print("Muuu!")


# Instanciando os objetos
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()


# Executando os métodos
cachorro.emitir_som()
gato.emitir_som()
vaca.emitir_som()
```

**Resultado:**

```text
Au au!
Miau!
Muuu!
```

### 2.2. Entendendo o código

1. Criamos a classe `Animal`, que possui o método `emitir_som()`.
2. Criamos as classes `Cachorro`, `Gato` e `Vaca`, que herdam de `Animal`.
3. Cada classe filha sobrescreve o método `emitir_som()`.
4. Ao chamar o método em cada objeto, Python executa a implementação correspondente à classe do objeto.

Observe que todos os objetos utilizam o mesmo nome de método, mas apresentam resultados diferentes.

**Importante:** o polimorfismo não exige necessariamente que as classes tenham uma relação de herança. Python também permite implementar comportamentos polimórficos entre classes independentes.

---

## 3. Polimorfismo utilizando Funções

Uma característica interessante do Python é permitir que uma mesma função trabalhe com diferentes tipos de objetos, desde que eles ofereçam os métodos ou comportamentos necessários.

Isso permite escrever códigos mais genéricos e flexíveis.

### 3.1. Exemplo prático

Vamos utilizar novamente as classes de animais.

```python
class Cachorro:

    def emitir_som(self):
        print("Au au!")


class Gato:

    def emitir_som(self):
        print("Miau!")


class Vaca:

    def emitir_som(self):
        print("Muuu!")


# Função polimórfica
def fazer_barulho(animal):
    animal.emitir_som()


# Instanciando os objetos
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()


# Executando a função
fazer_barulho(cachorro)
fazer_barulho(gato)
fazer_barulho(vaca)
```

**Resultado:**

```text
Au au!
Miau!
Muuu!
```

### 3.2. Entendendo o código

Observe que a função `fazer_barulho()` recebe um parâmetro chamado `animal`.

Não precisamos verificar se o objeto recebido pertence à classe `Cachorro`, `Gato` ou `Vaca`.

A função simplesmente executa o método `emitir_som()`.

Cada objeto responde à chamada de acordo com sua própria implementação.

Isso demonstra uma característica importante do Python: o comportamento de um objeto pode ser mais relevante do que sua classe específica.

---

## 4. Duck Typing

O **Duck Typing** é um conceito muito importante para compreender o polimorfismo em Python.

O nome vem de uma expressão popular:

> If it walks like a duck and it quacks like a duck, then it must be a duck.

Em português:

> Se anda como um pato e grasna como um pato, então provavelmente é um pato.

Na programação, isso significa que não precisamos verificar necessariamente a classe de um objeto. Podemos simplesmente verificar se ele possui os métodos e comportamentos necessários para realizar determinada operação.

Python utiliza amplamente essa abordagem.

### 4.1. Exemplo prático

Imagine que temos diferentes objetos capazes de reproduzir algum tipo de conteúdo.

```python
class Musica:

    def reproduzir(self):
        print("Reproduzindo música...")


class Video:

    def reproduzir(self):
        print("Reproduzindo vídeo...")


class Podcast:

    def reproduzir(self):
        print("Reproduzindo podcast...")


# Função que aceita diferentes objetos
def iniciar_reproducao(conteudo):
    conteudo.reproduzir()


# Instanciando os objetos
musica = Musica()
video = Video()
podcast = Podcast()


# Executando a função
iniciar_reproducao(musica)
iniciar_reproducao(video)
iniciar_reproducao(podcast)
```

**Resultado:**

```text
Reproduzindo música...
Reproduzindo vídeo...
Reproduzindo podcast...
```

### 4.2. O que torna esse exemplo interessante?

Observe que as classes `Musica`, `Video` e `Podcast` não possuem nenhuma relação de herança.

Mesmo assim, conseguimos utilizar os três objetos na mesma função.

Isso acontece porque todos implementam o método `reproduzir()`.

O Python não exige que os objetos pertençam à mesma classe ou compartilhem uma classe pai.

**Atenção:** Duck Typing não significa que Python ignora erros de tipos. Se um objeto não possuir o método esperado, a execução poderá gerar um `AttributeError`.

---

## 5. Polimorfismo utilizando Classes Abstratas (ABC)

Outra maneira de implementar polimorfismo em Python é utilizando classes abstratas.

Uma classe abstrata funciona como um modelo que estabelece quais métodos suas subclasses devem implementar.

Para trabalhar com esse recurso, utilizamos o módulo `abc`, disponível na biblioteca padrão do Python.

### 5.1. Principais conceitos

- **Classe abstrata:** classe que estabelece uma estrutura para outras classes.
- **Método abstrato:** método declarado na classe abstrata que precisa ser implementado pelas subclasses concretas.
- **ABC:** classe base utilizada para criar classes abstratas.
- **@abstractmethod:** decorador que indica que determinado método é abstrato.

### 5.2. Exemplo prático

Imagine um sistema financeiro que trabalha com diferentes tipos de contas bancárias.

Todas as contas precisam oferecer uma operação de saque, mas cada tipo de conta pode possuir regras específicas.

```python
from abc import ABC, abstractmethod


# Classe abstrata
class ContaBancaria(ABC):

    @abstractmethod
    def sacar(self, valor):
        pass


# Classe filha
class ContaCorrente(ContaBancaria):

    def sacar(self, valor):
        print(f"Saque de R$ {valor:.2f} realizado na conta corrente.")


# Classe filha
class ContaPoupanca(ContaBancaria):

    def sacar(self, valor):
        print(f"Saque de R$ {valor:.2f} realizado na poupança.")


# Instanciando os objetos
corrente = ContaCorrente()
poupanca = ContaPoupanca()


# Executando os métodos
corrente.sacar(500)
poupanca.sacar(300)
```

**Resultado:**

```text
Saque de R$ 500.00 realizado na conta corrente.
Saque de R$ 300.00 realizado na poupança.
```

### 5.3. Por que utilizar classes abstratas?

As classes abstratas ajudam a estabelecer um contrato entre a classe base e suas subclasses.

No exemplo, qualquer classe concreta que herdar de `ContaBancaria` deverá implementar o método `sacar()`.

Caso contrário, não será possível instanciar essa classe.

Por exemplo:

```python
class ContaDigital(ContaBancaria):
    pass


conta = ContaDigital()
```

**Resultado:**

```text
TypeError: Can't instantiate abstract class ContaDigital
with abstract method sacar
```

Isso acontece porque a classe `ContaDigital` não implementou o método abstrato obrigatório.

**Importante:** classes abstratas não servem apenas para implementar polimorfismo. Elas também ajudam a definir contratos e padronizar a estrutura de sistemas maiores.

---

## 6. Polimorfismo utilizando Protocol (Structural Typing)

Além do Duck Typing tradicional, Python oferece um recurso chamado `Protocol`, disponível no módulo `typing`.

Ele permite definir estruturas de comportamento que diferentes classes podem implementar sem precisar herdar de uma classe específica.

Esse recurso é particularmente útil quando trabalhamos com tipagem estática e ferramentas de análise de código.

### 6.1. Exemplo prático

```python
from typing import Protocol


# Definindo um protocolo
class Reproduzivel(Protocol):

    def reproduzir(self) -> None:
        ...


# Primeira classe
class Musica:

    def reproduzir(self) -> None:
        print("Reproduzindo música...")


# Segunda classe
class Video:

    def reproduzir(self) -> None:
        print("Reproduzindo vídeo...")


# Função que recebe qualquer objeto compatível
def iniciar_reproducao(conteudo: Reproduzivel) -> None:
    conteudo.reproduzir()


musica = Musica()
video = Video()


iniciar_reproducao(musica)
iniciar_reproducao(video)
```

**Resultado:**

```text
Reproduzindo música...
Reproduzindo vídeo...
```

### 6.2. Entendendo o Protocol

O protocolo `Reproduzivel` estabelece que um objeto precisa oferecer um método chamado `reproduzir()`.

As classes `Musica` e `Video` não precisam herdar de `Reproduzivel`.

Elas apenas precisam implementar a estrutura definida pelo protocolo.

Diferentemente das classes abstratas, os protocolos normalmente são utilizados para verificação estrutural de tipos, especialmente por ferramentas como Pyright e Mypy.

---

## 7. Diferenças entre as Abordagens de Polimorfismo

Python oferece diferentes mecanismos para trabalhar com polimorfismo.

| Abordagem | Característica principal |
|---|---|
| Sobrescrita de métodos | Subclasses redefinem métodos herdados |
| Duck Typing | Objetos são utilizados conforme seus comportamentos |
| Classes abstratas (ABC) | Estabelecem contratos para subclasses |
| Protocol | Define estruturas compatíveis sem exigir herança explícita |

### Quando utilizar cada abordagem?

**Sobrescrita de métodos:**

Utilize quando existir uma relação de herança e uma classe filha precisar especializar um comportamento herdado.

**Duck Typing:**

Utilize quando diferentes objetos possuírem os métodos necessários para realizar uma operação, sem necessidade de compartilhar uma hierarquia.

**Classes abstratas:**

Utilize quando precisar estabelecer regras obrigatórias para classes que compartilham uma estrutura.

**Protocol:**

Utilize quando desejar definir contratos estruturais, especialmente em projetos que utilizam tipagem estática.

---

## 8. Sobrecarga de Métodos (Method Overloading) em Python

É importante conhecer uma particularidade da linguagem Python: diferentemente de linguagens como Java e C++, Python não oferece sobrecarga tradicional de métodos baseada exclusivamente na quantidade ou nos tipos dos parâmetros.

Por exemplo, não podemos definir dois métodos com o mesmo nome esperando que Python escolha automaticamente um deles de acordo com os argumentos.

### 8.1. Exemplo de comportamento incorreto

```python
class Calculadora:

    def somar(self, a, b):
        return a + b

    def somar(self, a, b, c):
        return a + b + c


calculadora = Calculadora()

print(calculadora.somar(10, 20))
```

O código gera um `TypeError`, porque a segunda definição substituiu a primeira.

### 8.2. Alternativa utilizando parâmetros padrão

Uma maneira de obter comportamento semelhante é utilizar parâmetros opcionais.

```python
class Calculadora:

    def somar(self, a, b, c=0):
        return a + b + c


calculadora = Calculadora()

print(calculadora.somar(10, 20))
print(calculadora.somar(10, 20, 30))
```

**Resultado:**

```text
30
60
```

### 8.3. Alternativa utilizando *args

Também podemos utilizar `*args` para receber uma quantidade variável de argumentos.

```python
class Calculadora:

    def somar(self, *args):
        return sum(args)


calculadora = Calculadora()

print(calculadora.somar(10, 20))
print(calculadora.somar(10, 20, 30))
print(calculadora.somar(10, 20, 30, 40))
```

**Resultado:**

```text
30
60
100
```

**Observação:** o módulo `typing` também disponibiliza o decorador `@overload`, que permite declarar diferentes assinaturas para análise estática de tipos. Ele não cria, por si só, múltiplas implementações em tempo de execução.

---

## 9. Boas Práticas ao Trabalhar com Polimorfismo

Para utilizar o polimorfismo de maneira eficiente, algumas boas práticas devem ser consideradas:

1. **Prefira interfaces consistentes:** utilize nomes de métodos que representem o mesmo comportamento entre diferentes classes.
2. **Evite condicionais desnecessárias:** não crie vários `if` e `elif` para identificar a classe de cada objeto quando o polimorfismo puder resolver o problema.
3. **Utilize classes abstratas quando necessário:** estabeleça contratos para classes que precisam implementar determinados comportamentos.
4. **Conheça o Duck Typing:** aproveite a flexibilidade da linguagem Python para trabalhar com diferentes objetos.
5. **Respeite o princípio da substituição de Liskov:** subclasses devem preservar as expectativas estabelecidas pela classe base.
6. **Utilize Protocol em projetos tipados:** ele ajuda a documentar e verificar estruturas de comportamento.
7. **Evite abstrações desnecessárias:** nem todo conjunto de classes precisa de uma classe abstrata ou protocolo.

---

## 10. Exercícios para Praticar

A melhor maneira de consolidar o aprendizado é implementar diferentes situações utilizando polimorfismo.

### Exercício 1 — Animais

Crie três classes:

- `Cachorro`
- `Gato`
- `Passaro`

Cada classe deverá possuir um método chamado `emitir_som()`.

Depois, crie uma função chamada `fazer_barulho()` que receba um objeto e execute seu método `emitir_som()`.

**Objetivo:** praticar polimorfismo e Duck Typing.

### Exercício 2 — Formas Geométricas

Crie uma classe chamada `FormaGeometrica` com um método `calcular_area()`.

Depois, crie as classes:

- `Quadrado`: deverá calcular a área de um quadrado.
- `Retangulo`: deverá calcular a área de um retângulo.
- `Circulo`: deverá calcular a área de um círculo.

Utilize sobrescrita de métodos para implementar os cálculos.

**Objetivo:** praticar polimorfismo por sobrescrita.

### Exercício 3 — Sistema de Pagamentos

Crie uma classe abstrata chamada `Pagamento`, contendo um método abstrato `processar_pagamento()`.

Depois, crie três classes:

- `CartaoCredito`
- `Pix`
- `Boleto`

Cada classe deverá implementar seu próprio método `processar_pagamento()`.

**Objetivo:** praticar classes abstratas e métodos abstratos.

### Exercício 4 — Sistema de Reprodução

Crie três classes independentes:

- `Musica`
- `Video`
- `Podcast`

Todas deverão possuir um método chamado `reproduzir()`.

Depois, crie uma função chamada `iniciar_reproducao()` que receba qualquer um desses objetos e execute o método correspondente.

**Objetivo:** compreender como o Duck Typing permite trabalhar com objetos de classes diferentes.

### Exercício 5 — Sistema de Funcionários

Crie uma classe abstrata chamada `Funcionario`, contendo um método abstrato `calcular_salario()`.

Depois, crie as seguintes subclasses:

- `FuncionarioCLT`: salário fixo mais benefícios.
- `FuncionarioFreelancer`: remuneração baseada nas horas trabalhadas.
- `FuncionarioComissionado`: salário baseado em comissão sobre vendas.

Crie uma função que receba uma lista de funcionários e apresente o salário calculado de cada um.

**Objetivo:** integrar abstração, herança e polimorfismo em um cenário mais próximo de aplicações reais.

---

## 11. Resumo Geral

O polimorfismo permite que diferentes objetos respondam a uma mesma chamada de método, apresentando comportamentos específicos.

É um recurso fundamental para construir sistemas flexíveis, extensíveis e organizados.

Os principais conceitos estudados foram:

- **Polimorfismo:** capacidade de diferentes objetos apresentarem comportamentos distintos por meio de uma interface comum.
- **Method Overriding:** sobrescrita de métodos herdados.
- **Duck Typing:** utilização de objetos conforme seus comportamentos, independentemente de sua classe.
- **ABC:** mecanismo para criar classes abstratas e estabelecer contratos.
- **Protocol:** definição de estruturas de comportamento sem exigir herança explícita.
- **Method Overloading:** sobrecarga tradicional não é suportada nativamente em Python por quantidade ou tipo de parâmetros.

### Conceito fundamental para memorizar

> Polimorfismo permite que diferentes objetos utilizem uma mesma interface, mas executem comportamentos específicos de acordo com suas implementações.

---

## 12. Documentação Oficial

Para aprofundar os conhecimentos, consulte a documentação oficial do Python:

- [Python — Classes](https://docs.python.org/3/tutorial/classes.html): conceitos de classes, herança e sobrescrita.
- [Python — abc](https://docs.python.org/3/library/abc.html): documentação sobre classes e métodos abstratos.
- [Python — typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol): documentação sobre protocolos e tipagem estrutural.
- [Python — Typing Overload](https://docs.python.org/3/library/typing.html#typing.overload): documentação sobre assinaturas sobrecarregadas.
- [Python — MRO](https://docs.python.org/3/howto/mro.html): documentação sobre a ordem de resolução de métodos.