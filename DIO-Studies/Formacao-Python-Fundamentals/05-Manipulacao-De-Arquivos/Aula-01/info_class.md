# Por que precisamos manipular arquivos?
Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função 'open()' para isso. Quando terminamos de trabalhar com o arquivo, usamos a função 'close()' para liberar recusos.

## Para ler um arquivo
file = open('example.txt', 'r')

## Para escrever em um arquivo
file = open('example.txt', 'w')

## Para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')