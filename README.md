# Queue Implementation in Python

This is a basic implementation of a Queue data structure using linked nodes in Python.

## Features

- `enqueue(value)`: Adds a new value to the end of the queue.
- `dequeue()`: Removes and returns the value at the front of the queue.
- `print_queue()`: Prints all the values in the queue from front to back.

## Example

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()  # Output: 1 2 3
my_queue.dequeue()      # Removes 1
my_queue.print_queue()  # Output: 2 3

-----------------------

# Implementação de Fila em Python

Esta é uma implementação básica de uma estrutura de dados Fila (Queue) usando nós encadeados em Python.

## Funcionalidades

- `enqueue(value)`: Adiciona um novo valor ao final da fila.
- `dequeue()`: Remove e retorna o valor no início da fila.
- `print_queue()`: Imprime todos os valores da fila do início ao fim.

## Exemplo

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()  # Saída: 1 2 3
my_queue.dequeue()      # Remove 1
my_queue.print_queue()  # Saída: 2 3