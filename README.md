# Interceptação de Asteroide: Simulação de Sistema Solar 2D

![Python](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-2.2.6-blue?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5.1-blue?logo=matplotlib&logoColor=white)

Projeto desenvolvido para a disciplina de Matemática Computacional (2025.1) na UFRJ, que consiste na simulação de um sistema solar 2D com o objetivo de interceptar um asteroide com um projétil.

O núcleo do projeto reside na implementação de métodos numéricos fundamentais do zero, sem o uso de bibliotecas de otimização prontas para essas tarefas, demonstrando um profundo entendimento dos algoritmos.

## Conceitos e Métodos Implementados

As seguintes técnicas foram criadas de forma customizada para este trabalho:

* **Spline Cúbica:** Utilizada para interpolar a trajetória do asteroide.
* **Método de Newton:** Empregado para resolver o sistema de equações não-lineares e encontrar o ponto exato de interceptação entre o projétil e o asteroide.
* **Método de Runge-Kutta (4ª Ordem):** Usado para resolver as equações diferenciais ordinárias (EDOs) que governam o movimento dos corpos celestes sob a influência da gravidade.


## Gerenciamento de Dependências

Este projeto utiliza `pip-tools` para um gerenciamento de dependências robusto e explícito.

* As dependências diretas estão declaradas em `requirements.in`.
* O arquivo `requirements.txt` é gerado a partir do `requirements.in` com o comando `pip-compile` e contém a lista completa de pacotes com suas versões exatas, garantindo que o ambiente seja sempre o mesmo.

## Autor

* **João Marcos Correa** - [JMarcosGomes](https://github.com/JMarcosGomes)
* **João Pedro Leyssieux** - [joao27lex](https://github.com/joao27lex)
* **Lucas Ferreira** - [Luc6s](https://github.com/Luc6s)
---

## English Version

# Asteroid Interceptor: A 2D Solar System Simulation

This project was developed for the Computational Mathematics course (2025.1 semester). It features a 2D solar system simulation with the goal of intercepting an asteroid with a projectile.

The core of this project lies in the from-scratch implementation of fundamental numerical methods, demonstrating a deep understanding of the underlying algorithms without relying on pre-existing optimization libraries.

## Key Concepts and Implemented Methods

* **Cubic Spline:** Used to interpolate the asteroid's trajectory.
* **Newton's Method:** Employed to solve the system of non-linear equations to find the precise interception point.
* **4th Order Runge-Kutta Method:** Used to solve the ordinary differential equations (ODEs) that govern the motion of celestial bodies under gravitational influence.
