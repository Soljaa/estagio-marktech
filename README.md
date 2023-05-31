# Projeto de gerenciamento de alunos
 
O usuário pode armazenar, listar, atualizar e deletar informações de 
alunos em um banco de dados.

Um aluno possui as seguintes informações:
matrícula (inteiro)
nome (string)
sobrenome (string)
email (string)
telefone (string)
curso (string)
data de nascimento (data)

## Funcionalidades:

1. Criação:
- Entrada: dados de um aluno como exposto acima;
- Saída: json com as informações do aluno salvo.

2. Listagem:
- Entrada: nenhuma;
- Saída: json contendo as informações de todos os alunos.

3. Atualização:
- Entrada: dados de um aluno como exposto acima;
- Saída: json com as informações atualizados do aluno.

4. Remoção:
- Entrada: matrícula de um aluno;
- Saída: json contendo as informações do aluno removido.

Tecnologias utilizadas:
* flask para a criação dos endpoints de CRUD;
* sqlite para o banco de dados;
* SQLAlchemy como ORM.

## Pré-requisitos

- Python 3.x instalado
- Banco de dados SQLite

## Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate # Para sistemas Linux/Mac
venv\Scripts\activate # Para Windows

3. Instale as dependências:
```
pip install -r requirements.txt
```
## Configuração

1. Crie o banco de dados SQLite:
```
python database/database.py
```
## Execução

1. Inicie o servidor da API:
```
python app.py 
```
## Endpoints

Aqui estão os endpoints disponíveis na API:

- `GET /students/list`: Obter todos os alunos.-
- `POST /students/add`: Criar um novo aluno.
- `PATCH /students/update`: Atualizar um aluno existente.
- `DELETE /students/delete/<int:id>`: Excluir um aluno existente.

Consulte a documentação completa para mais detalhes sobre os endpoints, seus parâmetros e formatos de dados esperados.

## Exemplos de Uso

Execute de outro terminal:
```
python tests/tests.py
```
