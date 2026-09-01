from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 16)
        self.cell(0, 10, 'Manual de Instrucoes - Gerenciador de Tarefas', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('helvetica', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('helvetica', '', 12)
        self.multi_cell(0, 8, body)
        self.ln(8)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Título 1
pdf.chapter_title('1. Introducao')
texto1 = ("Bem-vindo ao Gerenciador de Tarefas. Este manual prático tem como objetivo orientar "
          "sobre a usabilidade e as funcionalidades da plataforma, com foco nas recentes "
          "atualizações de segurança e na interface do Kanban Dinâmico.")
pdf.chapter_body(texto1)

# Título 2
pdf.chapter_title('2. Cadastro e Autenticacao Segura')
texto2 = ("A plataforma agora exige maior rigor no registro de novos usuários. "
          "Ao se cadastrar:\n"
          "- Acesse a tela de Registro.\n"
          "- Preencha seu Nome de Usuário, Senha e confirme a Senha.\n"
          "- O preenchimento do campo de E-mail é OBRIGATÓRIO. "
          "Esta medida adiciona uma camada de segurança e permite melhor comunicação e "
          "recuperação de conta no futuro.")
pdf.chapter_body(texto2)

# Título 3
pdf.chapter_title('3. Usabilidade do Kanban Dinâmico')
texto3 = ("O Kanban é a interface central para organizar as demandas.\n\n"
          "a) Arrastar Tarefas (Drag-and-Drop)\n"
          "Você pode mover tarefas entre as colunas ('Pendente', 'Em Andamento', 'Concluído') "
          "clicando e arrastando-as. O status é atualizado automaticamente ao soltar a tarefa na nova coluna.\n\n"
          "b) Designar Tarefas e Bloqueio de Ações\n"
          "Na hora de criar ou editar, uma tarefa deve ser atribuída a um usuário responsável. "
          "Atenção: Apenas o usuário designado para a tarefa possui permissão para movê-la no Kanban, "
          "editá-la ou excluí-la. Se você não for o responsável ('atribuido_a'), os botões "
          "estarão desabilitados ou bloqueados.")
pdf.chapter_body(texto3)

# Título 4
pdf.chapter_title('4. Comprovacoes de Seguranca (Anti-IDOR)')
texto4 = ("A plataforma conta com uma forte proteção de backend (Anti-IDOR). "
          "Se um usuário mal intencionado tentar forçar uma alteração (via manipulação de URL, "
          "scripts ou requisições API diretas) em uma tarefa da qual ele NÃO é o responsável:\n"
          "- O backend intercepta e bloqueia a ação.\n"
          "- Uma mensagem de erro limpa é retornada no formato JSON (ex: {'erro': 'Acesso negado'}).\n"
          "- Nenhum dado sensível ou stack trace da aplicação será exposto. "
          "Isso protege toda a infraestrutura e os dados dos outros usuários de forma efetiva.")
pdf.chapter_body(texto4)

# Gerar arquivo
pdf.output('Manual_Instrucoes.pdf')
print("PDF gerado com sucesso!")
