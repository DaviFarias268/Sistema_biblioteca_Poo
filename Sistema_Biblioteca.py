# --------------------------------------------------
# CLASSES DO SISTEMA
# --------------------------------------------------

class Livro:
    def __init__(self, titulo, autor, isbn, ano):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Status: {status}"


class Usuario:
    def __init__(self, nome, cpf, id_usuario):
        self.nome = nome
        self.cpf = cpf
        self.id_usuario = id_usuario
        self.lista_livro_emprestado = []

    def adicionar_livro(self, livro):
        self.lista_livro_emprestado.append(livro)

    def remover_livro(self, livro):
        if livro in self.lista_livro_emprestado:
            self.lista_livro_emprestado.remove(livro)

    def consultar_livros(self):
        if not self.lista_livro_emprestado:
            print("Este usuário não possui livros emprestados no momento.")
            return
        print(f"\n--- Livros com {self.nome} ---")
        for livro in self.lista_livro_emprestado:
            print(f"- {livro.titulo} (ISBN: {livro.isbn})")

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.lista_usuario = []
        self.lista_livro = []

    # --- GERENCIAMENTO DE LIVROS ---
    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ").strip()
        autor = input("Digite o autor do livro: ").strip()
        isbn = input("Digite o ISBN do livro: ").strip()
        ano = input("Digite o ano do livro: ").strip()
        
        livro = Livro(titulo, autor, isbn, ano)
        self.lista_livro.append(livro)
        print("\033[32mLivro cadastrado com sucesso!\033[m")

    def remover_livro(self):
        isbn = input("Digite o ISBN do livro a ser removido: ").strip()
        for livro in self.lista_livro:
            if livro.isbn == isbn:
                self.lista_livro.remove(livro)
                print("\033[32mLivro removido com sucesso!\033[m")
                return
        print("\033[31mErro: Livro não encontrado.\033[m")

    def listar_livros(self):
        if not self.lista_livro:
            print("Nenhum livro cadastrado no acervo.")
            return
        print("\n--- ACERVO DE LIVROS ---")
        for livro in self.lista_livro:
            print(livro)

    def buscar_livro(self):
        isbn = input("Digite o ISBN do livro: ").strip()
        for livro in self.lista_livro:
            if livro.isbn == isbn:
                print("\nLivro encontrado:")
                print(livro)
                return
        print("\033[31mLivro não encontrado!\033[m")

    # --- GERENCIAMENTO DE USUÁRIOS ---
    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ").strip()
        cpf = input("Digite o CPF do usuário: ").strip()
        id_usuario = input("Digite o ID do usuário: ").strip()
        
        usuario = Usuario(nome, cpf, id_usuario)
        self.lista_usuario.append(usuario)
        print("\033[32mUsuário cadastrado com sucesso!\033[m")

    def remover_usuario(self):
        id_usuario = input("Digite o ID do usuário a ser removido: ").strip()
        for usuario in self.lista_usuario:
            if usuario.id_usuario == id_usuario:
                self.lista_usuario.remove(usuario)
                print("\033[32mUsuário removido com sucesso!\033[m")
                return
        print("\033[31mErro: Usuário não encontrado.\033[m")

    def listar_usuarios(self):
        if not self.lista_usuario:
            print("Nenhum usuário cadastrado.")
            return
        print("\n--- LISTA DE USUÁRIOS ---")
        for usuario in self.lista_usuario:
            print(usuario)

    def buscar_usuario(self):
        id_usuario = input("Digite o ID do usuário: ").strip()
        for usuario in self.lista_usuario:
            if usuario.id_usuario == id_usuario:
                print("\nUsuário encontrado:")
                print(usuario)
                return
        print("\033[31mUsuário não encontrado!\033[m")

    # --- BALCÃO DE EMPRÉSTIMOS ---
    def emprestar_livro(self):
        id_usuario = input("Digite o ID do usuário: ").strip()
        usuario_encontrado = None
        for u in self.lista_usuario:
            if u.id_usuario == id_usuario:
                usuario_encontrado = u
                break

        if not usuario_encontrado:
            print("\033[31mUsuário não encontrado!\033[m")
            return

        isbn = input("Digite o ISBN do livro a ser emprestado: ").strip()
        for livro in self.lista_livro:
            if livro.isbn == isbn:
                if not livro.disponivel:
                    print("\033[31mEste livro já está emprestado!\033[m")
                    return
                
                livro.disponivel = False
                usuario_encontrado.adicionar_livro(livro)
                print(f"\033[32mLivro '{livro.titulo}' emprestado com sucesso para {usuario_encontrado.nome}!\033[m")
                return

        print("\033[31mLivro não encontrado!\033[m")

    def registrar_devolucao(self):
        id_usuario = input("Digite o ID do usuário que vai devolver: ").strip()
        usuario_encontrado = None
        for u in self.lista_usuario:
            if u.id_usuario == id_usuario:
                usuario_encontrado = u
                break

        if not usuario_encontrado:
            print("\033[31mUsuário não encontrado!\033[m")
            return

        isbn = input("Digite o ISBN do livro a ser devolvido: ").strip()
        for livro in self.lista_livro:
            if livro.isbn == isbn:
                if livro in usuario_encontrado.lista_livro_emprestado:
                    livro.disponivel = True
                    usuario_encontrado.remover_livro(livro)
                    print(f"\033[32mLivro '{livro.titulo}' devolvido por {usuario_encontrado.nome}!\033[m")
                    return
                else:
                    print("\033[31mEste livro não consta na lista deste usuário!\033[m")
                    return

        print("\033[31mLivro não encontrado no acervo!\033[m")

    def consultar_emprestimos_usuario(self):
        id_usuario = input("Digite o ID do usuário: ").strip()
        for usuario in self.lista_usuario:
            if usuario.id_usuario == id_usuario:
                usuario.consultar_livros()
                return
        print("\033[31mUsuário não encontrado!\033[m")


# --------------------------------------------------
# EXECUÇÃO DO SISTEMA
# --------------------------------------------------

print("=" * 45)
print("     BEM-VINDO AO SISTEMA DE BIBLIOTECA     ")
print("=" * 45)

minha_biblioteca = Biblioteca()

while True:
    print("\n┌" + "─" * 43 + "┐")
    print("│                 MENU PRINCIPAL            │")
    print("├" + "─" * 43 + "┤")
    print("│  --- LIVROS ---                           │")
    print("│   1. Cadastrar Livro                      │")
    print("│   2. Remover Livro                        │")
    print("│   3. Listar Todos os Livros               │")
    print("│   4. Buscar Livro por ISBN                │")
    print("│                                           │")
    print("│  --- USUÁRIOS ---                         │")
    print("│   5. Cadastrar Usuário                    │")
    print("│   6. Remover Usuário                      │")
    print("│   7. Listar Todos os Usuários             │")
    print("│   8. Buscar Usuário por ID                │")
    print("│                                           │")
    print("│  --- EMPRÉSTIMOS ---                      │")
    print("│   9. Realizar Empréstimo                  │")
    print("│  10. Registrar Devolução                  │")
    print("│  11. Consultar Livros do Usuário          │")
    print("│                                           │")
    print("│  12. Sair do Sistema                      │")
    print("└" + "─" * 43 + "┘")
    
    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("\033[31mErro: Digite apenas números inteiros!\033[m")
        continue

    print("\n" + "=" * 45 + "\n")

    match opcao:
        case 1:
            minha_biblioteca.cadastrar_livro()
        case 2:
            minha_biblioteca.remover_livro()
        case 3:
            minha_biblioteca.listar_livros()
        case 4:
            minha_biblioteca.buscar_livro()
        case 5:
            minha_biblioteca.cadastrar_usuario()
        case 6:
            minha_biblioteca.remover_usuario()
        case 7:
            minha_biblioteca.listar_usuarios()
        case 8:
            minha_biblioteca.buscar_usuario()
        case 9:
            minha_biblioteca.emprestar_livro()
        case 10:
            minha_biblioteca.registrar_devolucao()
        case 11:
            minha_biblioteca.consultar_emprestimos_usuario()
        case 12:
            print("Saindo do sistema... Até logo!")
            print("=" * 45)
            break
        case _:
            print("\033[31mOpção inválida! Escolha um número de 1 a 12.\033[m")