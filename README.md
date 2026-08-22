# Todoo! — Gerenciador de Tarefas

Um sistema simples de gerenciamento de tarefas desenvolvido em **Python**, utilizando **SQLite** para armazenamento dos dados. O projeto possui duas formas de utilização: uma interface gráfica desenvolvida com **Tkinter** e uma interface via **terminal**.

## 📌 Sobre o Projeto

O **Todoo!** permite que o usuário crie, visualize e remova tarefas. Todas as tarefas são armazenadas em um banco de dados SQLite, garantindo que os dados permaneçam salvos mesmo após o encerramento do programa.

O projeto foi desenvolvido com o objetivo de praticar conceitos de:

* Python
* Programação orientada a objetos
* Banco de dados
* SQLite
* Interfaces gráficas
* Manipulação de dados
* Funções e estruturas de controle

## ⚙️ Funcionalidades

### 🖥️ Interface Gráfica

A versão gráfica utiliza **Tkinter** e permite:

*  Adicionar tarefas
*  Visualizar tarefas cadastradas
*  Remover tarefas
*  Atualizar a lista de tarefas
*  Armazenar informações no banco SQLite
*  Validar os campos preenchidos

Cada tarefa possui:

| Campo     | Descrição                     |
| --------- | ----------------------------- |
| ID        | Identificador único da tarefa |
| Nome      | Nome da tarefa                |
| Data      | Data e horário de criação     |
| Descrição | Descrição da tarefa           |

### 💻 Interface Terminal

A versão para terminal possui um menu com as seguintes opções:

```text
{1} -> Verificar tarefas
{2} -> Adicionar tarefas
{3} -> Remover tarefa
{0} -> Encerrar
```

## 🗄️ Banco de Dados

O projeto utiliza o **SQLite3**, através do arquivo:

```text
meu_banco.db
```

A tabela utilizada é:

```sql
CREATE TABLE tarefas(
    id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    descricao TEXT
);
```

### Estrutura da tabela

* `id_tarefa`: ID único gerado automaticamente.
* `nome`: nome da tarefa.
* `data`: data e horário em que a tarefa foi criada.
* `descricao`: descrição da tarefa.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **SQLite3**
* **Tkinter**
* **ttk**
* **Git/GitHub**

As bibliotecas `sqlite3` e `tkinter` fazem parte da instalação padrão do Python na maioria dos ambientes.

## 📁 Estrutura do Projeto

```text
Todoo/
│
├── interface_grafica.py
├── terminal.py
├── meu_banco.db
└── README.md
```

> O arquivo `meu_banco.db` pode ser criado automaticamente pelo programa na primeira execução.

## ▶️ Como Executar

### 1. Instale o Python

Verifique se o Python está instalado:

Clone o repositório e entre na pasta:

```bash
cd Todoo
```

### 3. Execute para utilizar o Todoo! com interface gráfica:

```bash
python "Todoo Aplication.py"
```
- Exemplo de execução:
<img width="1600" height="1000" alt="WhatsApp Image 2026-08-22 at 00 48 15" src="https://github.com/user-attachments/assets/d73cb1d4-d913-4913-a592-bdd8c7fddd32" />

---
### 4. Execute para utilizar o Todoo! pelo terminal:

```bash
python "Todoo terminal.py"
```
- Exemplo de execução:
<img width="1600" height="1000" alt="WhatsApp Image 2026-08-22 at 00 53 03" src="https://github.com/user-attachments/assets/ac26dd8d-33d8-469d-91bb-aeb5814b1a12" />

---

## ⚠️ Regras para criação de tarefas

O sistema possui algumas validações:

* Nem o nome e nem a descrição podem ficar vazios.
* O nome pode possuir no máximo **20 caracteres**.
* A descrição pode possuir no máximo **50 caracteres**.

Exemplo:

```text
Nome: Estudar Python
Descrição: Revisar funções e banco de dados
```

## 🔄 Funcionamento

O fluxo básico do sistema é:

```text
Usuário
   │
   ▼
Interface Gráfica / Terminal
   │
   ▼
Funções Python
   │
   ▼
SQLite
   │
   ▼
meu_banco.db
```

Ao adicionar uma tarefa, o programa executa um `INSERT` no banco.

Ao visualizar as tarefas, executa um `SELECT`.

Ao remover uma tarefa, executa um `DELETE`.

## 📍 Objetivo Acadêmico

O projeto foi desenvolvido como forma de aplicar na prática conceitos de programação em python, persistência de dados e desenvolvimento de interfaces, visando colocar os meus conhecimentos em prática.

Além disso, a utilização de duas interfaces demonstra diferentes formas de interação com o mesmo sistema:

* Interface gráfica para facilitar a utilização pelo usuário.
* Interface de terminal para uma utilização mais simples e direta.

## Ideias para possíveis futuras atualizações

Algumas funcionalidades que podem ser adicionadas futuramente caso eu decida mexer novamente nesse projeto:

*  Editar tarefas existentes
*  Adicionar status: pendente/concluída
*  Implementar pesquisa de tarefas
*  Adicionar filtro 
*  Melhorar o design da interface gráfica
*  Criar sistema de login

## 👨‍💻 Autor

**Heitor Alves dos Santos**

Projeto desenvolvido em Python para estudos e prática de desenvolvimento de software de forma autônoma, sem dependência de IA.
