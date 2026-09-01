# Gerenciador de Tarefas - Kanban Dinâmico e Seguro

Bem-vindo ao repositório do projeto **Gerenciador de Tarefas**, uma aplicação robusta de gerenciamento de tarefas baseada em Django, agora refatorada para oferecer maior segurança, usabilidade e controle de acesso.

## 🚀 Novas Features (Refatoração)

### 🔒 Autenticação Segura
O sistema de cadastro de usuários foi aprimorado. Agora, o **e-mail é um campo obrigatório** durante o registro, garantindo uma camada adicional de validação, segurança e possibilidade de comunicação confiável com os usuários.

### 📋 Kanban Dinâmico (Drag-and-Drop e Controle de Acesso)
A interface de gerenciamento de tarefas foi transformada em um Kanban interativo:
* **Drag-and-Drop:** Arraste e solte tarefas facilmente entre as colunas para atualizar seus status de forma fluida.
* **Controle de Ações Restrito:** Botões de ação (como editar, excluir e mover tarefas) estão **bloqueados estritamente para o Usuário Responsável (`atribuido_a`)**. Apenas o usuário designado para a tarefa pode manipulá-la, reforçando as regras de negócio e prevenindo edições acidentais por terceiros.

---

## Passo a Passo de Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente em sua máquina.

### Pré-requisitos
- Ter o **Python 3.x** instalado.
- Ter o **Git** instalado (opcional, caso vá clonar o repositório).

### 1. Clonar o repositório ou extrair os arquivos
Se estiver usando o Git:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
```

### 2. Criar e Ativar o Ambiente Virtual (Recomendado)
É uma boa prática isolar as dependências do projeto.
- No macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
- No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as Dependências
Instale as bibliotecas listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Preparar o Banco de Dados
Execute as migrações para criar as tabelas no banco de dados SQLite:
```bash
python manage.py migrate
```

### 5. Iniciar o Servidor
Execute o comando abaixo para iniciar o servidor de desenvolvimento:
```bash
python manage.py runserver
```

### 6. Acessar a Aplicação
Abra o seu navegador web e acesse o endereço:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Como utilizar o sistema
1. Ao acessar a aplicação pela primeira vez, clique em **Cadastre-se** para criar o seu usuário.
2. Após criar a conta, você será redirecionado para o seu **Quadro Kanban**.
3. Clique no botão **"Nova Tarefa"** no topo direito, preencha os dados (Título, Descrição, a quem será atribuída e o status inicial).
4. No Kanban, você pode **arrastar e soltar** as tarefas entre as colunas para atualizar seus status automaticamente no banco de dados.
5. Acesse a aba **Dashboard** no menu superior para ver as estatísticas gerais do projeto.

## Painel Administrativo (Django Admin)
O projeto conta com uma interface administrativa completa nativa do Django. Nela, é possível gerenciar todos os usuários, tarefas e redefinir senhas (caso algum usuário esqueça).

Para utilizar:
1. Certifique-se de que você criou um "Superusuário" executando o comando no terminal (com o `venv` ativo):
```bash
python manage.py createsuperuser
```
2. Acesse a rota administrativa no seu navegador: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
3. Faça login com as credenciais do superusuário.
4. Para alterar a senha de um colega, clique em **Usuários**, selecione o usuário desejado e clique no link "alterar a senha" no topo do formulário.
