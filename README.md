# 📚 Sistema de Gerenciamento de Biblioteca em Python

Um sistema de terminal desenvolvido em Python focado nos conceitos de **Programação Orientada a Objetos (POO)**. O projeto simula a rotina completa de atendimento de uma biblioteca, gerenciando acervo de livros, cadastro de usuários e o fluxo de empréstimos e devoluções.

---

## 💻 Sobre o Projeto

O objetivo principal do projeto é aplicar uma **arquitetura limpa com separação de responsabilidades**:
- **`Livro`**: Entidade responsável por armazenar as informações do livro e seu estado atual (disponível ou emprestado).
- **`Usuario`**: Entidade responsável pelos dados do usuário e por manter seu histórico de empréstimos ativos.
- **`Biblioteca`**: O sistema central que gerencia o acervo, o cadastro de usuários e orquestra o balcão de empréstimos/devoluções.

---

## 🚀 Funcionalidades

### 📚 Gestão de Livros
- **Cadastrar Livro**: Registra título, autor, ISBN e ano de publicação.
- **Remover Livro**: Remove uma obra do acervo via ISBN.
- **Listar Acervo**: Exibe todos os livros cadastrados e seus status de disponibilidade.
- **Buscar Livro**: Localiza um livro específico através do código ISBN.

### 👤 Gestão de Usuários
- **Cadastrar Usuário**: Registra nome, CPF e ID único.
- **Remover Usuário**: Remove o cadastro de um usuário via ID.
- **Listar Usuários**: Exibe todos os usuários cadastrados na biblioteca.
- **Buscar Usuário**: Busca as informações de um usuário específico via ID.

### 🔄 Balcão de Empréstimos e Devoluções
- **Realizar Empréstimo**: Vincula um livro disponível diretamente ao cadastro de um usuário.
- **Registrar Devolução**: Libera o livro no acervo e o remove do histórico do usuário.
- **Consultar Livros do Usuário**: Exibe todos os livros atualmente emprestados para um determinado usuário.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Paradigma**: Programação Orientada a Objetos (POO)
- **Estruturas de Dados**: Listas e Dicionários para manipulação em memória
- **Controle de Fluxo**: Estrutura `match-case` e tratamento de exceções (`try/except`)

---

## 🎯 Como Executar o Projeto

1. **Pré-requisitos**: Certifique-se de ter o [Python 3.10+](https://www.python.org/) instalado na sua máquina.

2. **Clonar o repositório**:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
