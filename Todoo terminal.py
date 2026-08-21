import time
import sqlite3

def menu():
    while True:
        escolha_execucao = ()
        print("-" * 50)
        print(" " * 10 + "Bem vindo ao Todoo Terminal" + " "*12 + "|")
        print("-" * 50)
        print(" " * 49 + "|")
        print("{1} -> Verificar tarefas " + " "*24 + "|")
        print("{2} -> Adicionar tarefas"+ " "*25 + "|")
        print("{3} -> Remover tarefa"+ " "*28 + "|")
        print("{0} -> Encerrar "+ " "*33 + "|")
        print("-" * 50)
        print(" " * 50)
        while True:
            try:
                escolha_execucao = int(input("Digite a sua escolha: "))
            except ValueError:
                print("Valor inválido, digite um valor numérico! \n")
                time.sleep(2)
                break
            if escolha_execucao not in [1,2,3,0]:
                print("Valor numérico inválido, digite outro valor! \n")
                time.sleep(2)
                break
            else:
                break
        if escolha_execucao == 1:
            print("Opção 1 -- Verificando tarefas \n")
            time.sleep(1)
            verificar_tarefas()
            time.sleep(2)
        if escolha_execucao == 2:
            print("Opção 2 -- Adicionando tarefas \n")
            time.sleep(1)
            while True:
                nome = input("Nome da tarefa (Máx 20): ").strip()
                descricao = input("Descrição da tarefa (Máx 50): ").strip()
                if (nome and descricao) and  len(nome) <=20 and len(descricao) <=50:
                    adicionar_tarefas(nome,descricao)
                    break
                elif len(descricao) > 50 and len(nome) > 20:
                    print("Ambos nome e descrição ultrapassam o limite de caracteres!\n")
                elif len(nome) > 20:
                    print("O nome precisa ter menos de 20 caracteres!\n")
                elif len(descricao) > 50:
                    print("A descrição precisa ter menos de 50 caracteres!\n")
                else:
                    print("Nome e Descrição não podem ficar vazios!\n")

        if escolha_execucao == 3:
            print("Opção 3 -- Removendo tarefa" )
            time.sleep(1)
            try:
                id_tarefa = int(input("Digite o id da tarefa que deseja excluir: "))
                remover_tarefa(id_tarefa)
            except ValueError:
                print("Digite uma opção válida!\n")
                time.sleep(2)
                continue

        if escolha_execucao == 0:
            print("Opção  3 -- saindo...")
            time.sleep(2)
            break

def inicializar_banco():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas(
            id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            descricao TEXT
        )
    """
    )
    conexao.commit()
    return conexao

def conectar_banco():
    return sqlite3.connect("meu_banco.db")

def verificar_tarefas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    registros = cursor.fetchall()
    conexao.close()
    print("\n" + "=" * 100)
    print("       TAREFAS LISTADAS: ")
    print("=" * 100)
    if not registros:
        print("Nenhuma tarefa adicionada ainda")
    else:
        print(f"{'ID':<5} | {'Nome':<20} | {'Data':<19} | {'Descricao'}")
        print("-"*100)
        for i in registros:
            id_tarefa, nome, data, descricao = i
            print(f"{id_tarefa:<5} | {nome:<20} | {data:<7} | {descricao}")
    print("="*100 + "\n")

def adicionar_tarefas(nome, descricao):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO tarefas (nome, descricao) VALUES (?, ?)",
        (nome, descricao),
    )
    conexao.commit()
    conexao.close()
    print(f"\n '{nome}' adicionado com sucesso e salvo no arquivo!s")
    time.sleep(2)

def remover_tarefa(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id_tarefa = ?",
        (id_tarefa,)
    )
    if cursor.rowcount > 0:
        conexao.commit()
        conexao.close()
        print(f"\n '{id_tarefa}' removido com sucesso e atualizado nos arquivos!")
    else:
        conexao.close()
        print("Id não localizado, tarefa inexistente!")
    time.sleep(2)
if __name__ == "__main__":
    inicializar_banco()
    menu()

