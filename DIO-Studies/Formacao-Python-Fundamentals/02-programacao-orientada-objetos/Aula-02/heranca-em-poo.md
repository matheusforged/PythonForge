# Herança em Python

## 1. Introdução à Herança

A **herança** é um dos quatro pilares da Programação Orientada a Objetos (POO). Ela permite que uma classe herde atributos e métodos de outra classe, possibilitando o reaproveitamento de código e facilitando a organização e manutenção dos programas.

Em Python, uma classe pode herdar características de uma ou mais classes existentes.

A classe que fornece os atributos e métodos é chamada de **classe pai**, **superclasse** ou **classe base**.

Já a classe que recebe essas características é chamada de **classe filha**, **subclasse** ou **classe derivada**.

### Principais vantagens da herança

- **Reutilização de código:** evita a necessidade de escrever os mesmos métodos e atributos várias vezes.
- **Organização:** permite estruturar classes de maneira hierárquica.
- **Manutenção:** alterações na classe base podem beneficiar suas subclasses.
- **Extensibilidade:** permite adicionar novas funcionalidades sem modificar diretamente a classe original.
- **Polimorfismo:** permite que diferentes classes implementem comportamentos específicos para métodos com o mesmo nome.

---

## 2. Herança Simples (Single Inheritance)

A **herança simples** acontece quando uma classe filha herda características de apenas uma classe pai.

É o modelo mais básico de herança e permite que uma classe especializada aproveite os atributos e métodos de uma classe mais genérica.

### 2.1. Sintaxe

```python
class ClassePai:
    # Atributos e métodos da classe pai
    pass


class ClasseFilha(ClassePai):
    # Atributos e métodos específicos da classe filha
    pass
```

Observe que o nome da classe pai é informado entre parênteses na declaração da classe filha.

### 2.2. Exemplo prático

Imagine um sistema que trabalha com diferentes tipos de funcionários.

Todos os funcionários possuem nome, salário e um método para apresentar suas informações. Entretanto, alguns funcionários possuem características específicas.

Podemos criar uma classe base chamada `Funcionario` e uma classe derivada chamada `Gerente`.

```python
# Classe pai
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


# Classe filha
class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def apresentar_departamento(self):
        print(f"Departamento: {self.departamento}")


# Instanciando a classe filha
gerente = Gerente("Matheus", 8500, "Financeiro")

gerente.apresentar()
gerente.apresentar_departamento()
```

**Resultado:**

```text
Nome: Matheus
Salário: R$ 8500.00
Departamento: Financeiro
```

### 2.3. Entendendo o código

1. Criamos a classe `Funcionario`, que contém os atributos `nome` e `salario`.
2. Criamos o método `apresentar()`, responsável por exibir as informações do funcionário.
3. Criamos a classe `Gerente`, que herda da classe `Funcionario`.
4. Utilizamos `super().__init__(nome, salario)` para executar o construtor da classe pai.
5. Adicionamos o atributo `departamento`, que pertence especificamente à classe `Gerente`.
6. Criamos um objeto da classe `Gerente` e utilizamos tanto os métodos herdados quanto o método próprio da classe filha.

**Importante:** a classe filha não precisa reescrever os métodos da classe pai para utilizá-los. Ela pode simplesmente herdá-los.

---

## 3. A função super() na Herança

A função `super()` permite acessar métodos definidos na próxima classe da cadeia de herança, seguindo a ordem de resolução de métodos (MRO).

Ela é frequentemente utilizada para chamar o construtor da classe pai, evitando a repetição de código.

### 3.1. Exemplo sem super()

```python
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):

    def __init__(self, nome, idade, curso):
        Pessoa.__init__(self, nome, idade)
        self.curso = curso
```

Nesse exemplo, chamamos diretamente o construtor da classe `Pessoa`.

### 3.2. Exemplo utilizando super()

```python
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):

    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
```

A segunda abordagem é geralmente preferível, pois funciona melhor com hierarquias de herança mais complexas, especialmente na herança múltipla.

---

## 4. Sobrescrita de Métodos (Method Overriding)

A sobrescrita acontece quando uma classe filha redefine um método que já existe na classe pai.

Isso permite modificar ou especializar o comportamento herdado.

### Exemplo prático

```python
class Animal:

    def emitir_som(self):
        print("O animal emite um som.")


class Cachorro(Animal):

    def emitir_som(self):
        print("O cachorro está latindo!")


class Gato(Animal):

    def emitir_som(self):
        print("O gato está miando!")


cachorro = Cachorro()
gato = Gato()

cachorro.emitir_som()
gato.emitir_som()
```

**Resultado:**

```text
O cachorro está latindo!
O gato está miando!
```

Observe que as classes `Cachorro` e `Gato` herdaram de `Animal`, mas cada uma implementou seu próprio comportamento para o método `emitir_som()`.

### 4.1. Utilizando super() na sobrescrita

Também podemos executar o método original da classe pai e depois adicionar um comportamento específico.

```python
class Animal:

    def emitir_som(self):
        print("O animal está emitindo um som.")


class Cachorro(Animal):

    def emitir_som(self):
        super().emitir_som()
        print("Au au!")


cachorro = Cachorro()
cachorro.emitir_som()
```

**Resultado:**

```text
O animal está emitindo um som.
Au au!
```

---

## 5. Herança Múltipla (Multiple Inheritance)

A **herança múltipla** acontece quando uma classe filha herda características de duas ou mais classes pai.

Diferentemente da herança simples, na qual existe apenas uma classe base direta, a herança múltipla permite combinar funcionalidades de diferentes classes.

Esse recurso é útil quando uma classe precisa reunir responsabilidades ou comportamentos que estão distribuídos em diferentes classes.

### 5.1. Sintaxe

```python
class ClassePai1:
    pass


class ClassePai2:
    pass


class ClasseFilha(ClassePai1, ClassePai2):
    pass
```

Observe que as classes pai são informadas entre parênteses, separadas por vírgulas.

### 5.2. Exemplo prático

Imagine um sistema que trabalha com diferentes características de um dispositivo eletrônico.

Um dispositivo pode possuir funcionalidades de processamento e conectividade.

Podemos representar essas características em classes separadas e depois combiná-las por meio da herança múltipla.

```python
# Primeira classe pai
class Processador:

    def processar(self):
        print("Processando informações...")


# Segunda classe pai
class Conectividade:

    def conectar_internet(self):
        print("Conectado à internet!")


# Classe filha com herança múltipla
class Smartphone(Processador, Conectividade):

    def realizar_chamada(self):
        print("Realizando chamada telefônica...")


# Instanciando a classe filha
celular = Smartphone()

celular.processar()
celular.conectar_internet()
celular.realizar_chamada()
```

**Resultado:**

```text
Processando informações...
Conectado à internet!
Realizando chamada telefônica...
```

### 5.3. Entendendo o código

1. Criamos a classe `Processador`, responsável pelo processamento de informações.
2. Criamos a classe `Conectividade`, responsável pela conexão com a internet.
3. Criamos a classe `Smartphone`, que herda de ambas as classes.
4. Adicionamos o método `realizar_chamada()`, exclusivo da classe `Smartphone`.
5. Instanciamos um objeto e acessamos os métodos das duas classes pai e da própria classe filha.

**Resultado:** a classe `Smartphone` reúne funcionalidades de diferentes classes sem precisar reescrever seus métodos.

---

## 6. Ordem de Resolução de Métodos (MRO)

Na herança múltipla, pode acontecer de duas ou mais classes pai possuírem métodos com o mesmo nome.

Quando isso acontece, como Python decide qual método executar?

Para resolver esse problema, Python utiliza um mecanismo chamado **Method Resolution Order (MRO)**, ou Ordem de Resolução de Métodos.

O MRO determina a sequência em que Python procura os métodos e atributos nas classes de uma hierarquia de herança.

### 6.1. Exemplo prático

```python
class Pai1:

    def apresentar(self):
        print("Método da classe Pai1")


class Pai2:

    def apresentar(self):
        print("Método da classe Pai2")


class Filho(Pai1, Pai2):
    pass


objeto = Filho()

objeto.apresentar()
```

**Resultado:**

```text
Método da classe Pai1
```

Por quê?

Porque a classe `Filho` foi declarada herdando primeiro de `Pai1` e depois de `Pai2`.

Como ambas possuem o método `apresentar()`, Python encontra primeiro o método em `Pai1` e o executa.

### 6.2. Consultando o MRO

Podemos consultar a ordem de resolução utilizando o método `mro()` ou o atributo `__mro__`.

```python
print(Filho.mro())
```

Ou:

```python
print(Filho.__mro__)
```

**Resultado simplificado:**

```text
[
    Filho,
    Pai1,
    Pai2,
    object
]
```

A classe `object` aparece porque, em Python 3, todas as classes herdam direta ou indiretamente dela.

**Atenção:** o MRO não é simplesmente uma busca linear pela ordem dos parênteses em todos os cenários. Python utiliza o algoritmo C3 Linearization para construir uma ordem consistente, respeitando a hierarquia e a precedência das classes.

---

## 7. Herança Múltipla e super()

Na herança múltipla, `super()` possui um comportamento especialmente importante.

Ele não significa necessariamente "chamar a classe pai". Na verdade, ele chama o próximo método disponível de acordo com o MRO.

Isso permite que diferentes classes cooperem na execução de métodos.

### Exemplo prático

```python
class A:

    def apresentar(self):
        print("Classe A")
        super().apresentar()


class B:

    def apresentar(self):
        print("Classe B")
        super().apresentar()


class C:

    def apresentar(self):
        print("Classe C")


class Filho(A, B, C):
    pass


objeto = Filho()

objeto.apresentar()
```

**Resultado:**

```text
Classe A
Classe B
Classe C
```

Nesse exemplo, o fluxo de execução segue a ordem definida pelo MRO:

```text
Filho → A → B → C → object
```

Observe que cada chamada de `super()` direciona a execução para a próxima classe da sequência.

Esse padrão é conhecido como herança cooperativa.

**Importante:** para que a herança cooperativa funcione corretamente, os métodos precisam seguir uma estrutura compatível de chamadas e argumentos. Não basta adicionar `super()` indiscriminadamente.

---

## 8. Diferenças entre Herança Simples e Herança Múltipla

| Característica | Herança Simples | Herança Múltipla |
|---|---|---|
| Classes pai | Uma | Duas ou mais |
| Complexidade | Menor | Maior |
| Reutilização | De uma classe | De várias classes |
| Organização | Hierárquica | Pode envolver diferentes hierarquias |
| Resolução de métodos | Mais direta | Depende do MRO |
| Manutenção | Geralmente mais simples | Pode exigir mais atenção |

### Representação visual

**Herança simples:**

```text
       Animal
          |
          v
       Cachorro
```

**Herança múltipla:**

```text
    Processador    Conectividade
          \           /
           \         /
            \       /
             v     v
            Smartphone
```

---

## 9. Boas Práticas ao Trabalhar com Herança

A herança é um recurso poderoso, mas deve ser utilizada com planejamento.

Algumas boas práticas:

1. **Evite hierarquias desnecessariamente complexas:** muitas camadas de herança podem dificultar a compreensão do código.
2. **Utilize herança quando existir uma relação de especialização:** uma classe filha deve representar um tipo específico da classe pai.
3. **Prefira composição quando fizer mais sentido:** nem todo relacionamento entre objetos precisa ser resolvido por herança.
4. **Utilize super() corretamente:** principalmente em hierarquias com herança múltipla.
5. **Evite duplicação de código:** centralize comportamentos comuns nas classes apropriadas.
6. **Respeite o princípio da substituição de Liskov:** uma classe filha deve poder substituir sua classe pai sem comprometer o funcionamento esperado do programa.
7. **Conheça o MRO:** entender a ordem de resolução evita comportamentos inesperados na herança múltipla.

### 9.1. Herança ou Composição?

Nem sempre a melhor solução é utilizar herança.

Na herança, uma classe representa um tipo de outra classe (relação *é um*).

Na composição, uma classe utiliza ou possui objetos de outras classes (relação *tem um*).

Exemplo:

```python
# Composição

class Motor:

    def ligar(self):
        print("Motor ligado!")


class Carro:

    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.ligar()


carro = Carro()
carro.ligar_carro()
```

Nesse caso, `Carro` possui um `Motor`, mas não é um `Motor`.

A composição permite construir objetos combinando diferentes componentes, sem necessariamente criar uma hierarquia de herança.

---

## 10. Exercícios para Praticar

A melhor maneira de consolidar o aprendizado é implementar diferentes cenários utilizando herança.

### Exercício 1 — Herança Simples

Crie uma classe chamada `Pessoa`, contendo:

- Atributo `nome`.
- Atributo `idade`.
- Método `apresentar()`.

Depois, crie uma classe chamada `Estudante`, que herde de `Pessoa` e adicione:

- Atributo `curso`.
- Método `estudar()`.

**Objetivo:** praticar herança simples, construtores e utilização de `super()`.

### Exercício 2 — Sobrescrita de Métodos

Crie uma classe chamada `Veiculo`, contendo um método `movimentar()`.

Depois, crie duas classes filhas:

- `Carro`: sobrescreva o método para informar que o veículo está andando.
- `Aviao`: sobrescreva o método para informar que o veículo está voando.

**Objetivo:** compreender a sobrescrita de métodos e o polimorfismo.

### Exercício 3 — Herança Múltipla

Crie três classes:

- `Camera`: contendo o método `fotografar()`.
- `Telefone`: contendo o método `ligar()`.
- `ReprodutorMusical`: contendo o método `reproduzir_musica()`.

Depois, crie uma classe `Smartphone` que herde das três classes.

**Objetivo:** praticar herança múltipla e reutilização de métodos.

### Exercício 4 — MRO

Crie três classes chamadas `A`, `B` e `C`.

Todas devem possuir um método chamado `executar()`.

Depois, crie uma classe `D` que herde de `A`, `B` e `C`.

Faça o seguinte:

- Instancie a classe `D`.
- Execute o método `executar()`.
- Consulte o MRO utilizando `D.mro()`.
- Inverta a ordem das classes herdadas e observe o resultado.

**Objetivo:** compreender como Python resolve conflitos de métodos.

---

## 11. Resumo Geral

A herança permite reutilizar e especializar funcionalidades entre classes, tornando o desenvolvimento orientado a objetos mais organizado e eficiente.

Os principais conceitos estudados foram:

- **Herança:** mecanismo que permite compartilhar atributos e métodos entre classes.
- **Classe pai:** classe que fornece características para outras classes.
- **Classe filha:** classe que herda características de outra classe.
- **Herança simples:** quando uma classe herda de apenas uma classe base direta.
- **Herança múltipla:** quando uma classe herda de duas ou mais classes base diretas.
- **super():** permite acessar o próximo método na cadeia de resolução de métodos.
- **Sobrescrita:** permite redefinir métodos herdados.
- **MRO:** determina a ordem em que Python procura métodos e atributos.
- **Composição:** alternativa à herança que permite combinar objetos e funcionalidades.

### Conceito fundamental para memorizar

> Herança simples permite que uma classe herde de uma única classe base direta. Herança múltipla permite que uma classe herde de várias classes base diretas. Ambas possibilitam reutilizar código e construir sistemas orientados a objetos mais organizados.

---

## 12. Documentação Oficial

Para aprofundar os conhecimentos, consulte a documentação oficial do Python:

- [Python — Classes](https://docs.python.org/3/tutorial/classes.html): documentação sobre classes, herança e orientação a objetos.
- [Python — super()](https://docs.python.org/3/library/functions.html#super): documentação da função `super()`.
- [Python — Method Resolution Order](https://docs.python.org/3/howto/mro.html): explicação detalhada sobre o MRO e o algoritmo C3.
- [Python — Built-in Types](https://docs.python.org/3/library/stdtypes.html): referência dos tipos e estruturas fundamentais da linguagem.