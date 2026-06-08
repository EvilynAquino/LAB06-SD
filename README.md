<div align="center">

# Quine-McCluskey Logic Minimizer

**Lab 06 — Sistemas Digitais | DCOMP/UFS**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-lightgrey)](LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-LAB06--SD-181717?logo=github)](https://github.com/EvilynAquino/LAB06-SD)

Implementação do algoritmo de Quine-McCluskey para minimização de funções booleanas a partir de arquivos `.pla`, com suporte a don't-cares, saída SOP e benchmark de desempenho.

</div>

---

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Configuração e Uso](#configuração-e-uso)
- [Formato de Entrada (.pla)](#formato-de-entrada-pla)
- [Saída Esperada](#saída-esperada)
- [Atividades Implementadas](#atividades-implementadas)

---

## Visão Geral

Este projeto implementa o **algoritmo de Quine-McCluskey**, método tabular para minimização de funções booleanas, como alternativa sistemática ao Mapa de Karnaugh. A solução lê funções no formato PLA (Programmable Logic Array), realiza a minimização e retorna a expressão mínima na forma de **Soma de Produtos (SOP)**.

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Leitura de `.pla` | Parser completo com suporte a comentários e entradas com `-` |
| Expansão de don't-cares | Expansão recursiva de entradas com traço nas variáveis de entrada |
| Algoritmo QM | Combinação iterativa de implicantes até obter os implicantes primos |
| Saída SOP | Expressão booleana minimizada em notação algébrica (`A'B + BC`) |
| Benchmark | Medição de tempo de execução (ms) para múltiplos arquivos `.pla` |

---

## Estrutura do Projeto

```
LAB06-SD/
├── lab06_completo.py       # Script principal
├── README.md
└── benchmark/
    ├── tests/              # Casos de teste para as atividades
    │   ├── ex_and.pla
    │   ├── ex00_f_da_folha.pla
    │   ├── ex01_funcao3var.pla
    │   ├── ex02_funcao4var.pla
    │   ├── ex03_funcao5var.pla
    │   └── ex04_funcao6var.pla
    ├── benchmark/          # Arquivos para benchmark de desempenho
    │   └── ex*.train.pla
    └── validacao/          # Arquivos de validação
        └── ex*.valid.pla
```

---

## Pré-requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa — apenas biblioteca padrão (`os`, `time`)

---

## Configuração e Uso

**1. Clone o repositório:**

```bash
git clone https://github.com/EvilynAquino/LAB06-SD.git
cd LAB06-SD
```

**2. Ajuste o caminho base no final de `lab06_completo.py`:**

```python
BASE = r"caminho/para/pasta/benchmark"
```

**3. Execute:**

```bash
python lab06_completo.py
```

---

## Formato de Entrada (`.pla`)

Os arquivos de entrada seguem o padrão PLA simplificado:

```
.i 3        # Número de variáveis de entrada
.o 1        # Número de saídas (opcional)
011 1       # Mintermo (saída = 1)
1-0 1       # Entrada com don't-care na variável de entrada
100 -       # Don't-care de saída (não importa)
.e          # Fim do arquivo
```

> Linhas iniciadas com `#` são tratadas como comentários e ignoradas.

---

## Saída Esperada

```
ATIVIDADE 02 - LETRA B
--------------------------------------------------
Arquivo: ex01_funcao3var.pla
Mintermos: [0, 1, 2, 3, 5, 7]
Expressao minimizada:
A'C' + A'B + BC

ATIVIDADE 02 - LETRA C
--------------------------------------------------
Arquivo: ex_and.pla
Karnaugh : AB
QM       : AB

Arquivo: ex01_funcao3var.pla
Karnaugh : A'C' + A'B + BC
QM       : A'C' + A'B + BC

Arquivo: ex02_funcao4var.pla
Karnaugh : A + B
QM       : A + B

BENCHMARK
--------------------------------------------------
bench01.pla - 0.42 ms
bench02.pla - 1.87 ms
```

---

## Atividades Implementadas

| Atividade | Descrição |
|---|---|
| **Atividade 02-B** | Minimização de função de 3 variáveis via QM e exibição dos implicantes primos |
| **Atividade 02-C** | Comparação entre resultado do Mapa de Karnaugh (manual) e saída do algoritmo QM |
| **Benchmark** | Execução cronometrada do algoritmo em todos os arquivos `.pla` da pasta benchmark |

---

<div align="center">
Departamento de Computação — Universidade Federal de Sergipe (DCOMP/UFS)
</div>
