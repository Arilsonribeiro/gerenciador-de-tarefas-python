# 📝 Gerenciador de Tarefas em Python (CLI)

Um sistema interativo de gerenciamento de tarefas via linha de comando (CLI), desenvolvido em Python puro. Este projeto foi construído para demonstrar o domínio dos conceitos fundamentais da linguagem, incluindo estruturas de controle, manipulação de coleções dinâmicas e tratamento de exceções.

---

## 📌 Sumário
- [Funcionalidades](#-funcionalidades)
- [Conceitos Utilizados](#-conceitos-utilizados)
- [Como Executar](#-como-executar)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Estrutura do Código](#-estrutura-do-código)
- [Próximos Passos (Melhorias Futuras)](#-próximos-passos-melhorias-futuras)
- [Autor](#-autor)

---

## 🚀 Funcionalidades

- **Adicionar Tarefas:** Adiciona novas tarefas com validação contra entradas vazias.
- **Listar Tarefas:** Exibe todas as tarefas cadastradas de forma numerada e organizada.
- **Remover Tarefas:** Permite remover tarefas específicas pelo seu índice numérico com tratamento de erros.
- **Interface Interativa:** Menu interativo no terminal em loop contínuo até o encerramento manual.

---

## 🧠 Conceitos Utilizados

Este projeto engloba os fundamentos essenciais da programação em Python:

| Conceito | Aplicação Prática no Projeto |
| :--- | :--- |
| **Entrada e Saída de Dados** | Leitura de inputs do usuário via `input()` e formatação de mensagens no terminal. |
| **Estruturas Condicionais** | Controle de fluxo do menu e validação de regras de negócio (`if`, `elif`, `else`). |
| **Listas e Métodos** | Armazenamento dinâmico e manipulação de dados com `.append()` e `.pop()`. |
| **Laços de Repetição** | Manutenção do estado da aplicação (`while`) e iteração para exibição (`for`). |
| **Variáveis e Operadores** | Controle numérico de índices, validação lógica e contadores. |
| **Tratamento de Exceções** | Prevenção de travamento com bloco `try-except` para entradas não numéricas. |

---

## 💻 Como Executar

### Pré-requisitos
- **Python 3.x** instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Arilsonribeiro/gerenciador-de-tarefas-python.git](https://github.com/Arilsonribeiro/gerenciador-de-tarefas-python.git)

Acesse o diretório do projeto:
cd gerenciador-de-tarefas-python

Execute o script Python:
python main.py

Exemplo de Uso:

--- GERENCIADOR DE TAREFAS ---
1. Adicionar Tarefa
2. Listar Tarefas
3. Remover Tarefa
4. Sair
Escolha uma opção (1-4): 1

Digite a nova tarefa: Estudar fundamentos de Python
✓ Tarefa 'Estudar fundamentos de Python' adicionada com sucesso!

--- GERENCIADOR DE TAREFAS ---
1. Adicionar Tarefa
2. Listar Tarefas
3. Remover Tarefa
4. Sair
Escolha uma opção (1-4): 2

SUAS TAREFAS:
1. Estudar fundamentos de Python

Estrutura do Repositório:

gerenciador-de-tarefas-python/
│
├── main.py          # Código-fonte principal do projeto
├── README.md        # Documentação completa do projeto
└── .gitignore       # Arquivo de configuração de arquivos ignorados do Git



Próximos Passos (Melhorias Futuras)

[ ] Persistência de dados salva em arquivo JSON ou banco de dados SQLite.

[ ] Adição de status para tarefas (Concluída / Pendente).

[ ] Implementação de prioridades e datas de vencimento.



Autor
Desenvolvido por: Arilson Ribeiro Moreira

Estudante de Análise e Desenvolvimento de Sistemas (ADS)





----------------------------------------------------------------------------------------------------------------------------------------------------------




