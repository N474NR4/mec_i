from pathlib import Path
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(r'C:\Vs Code\Mec intelligence')
OUTPUT = Path(r'C:\Users\Positivo\Downloads\MEC_INTELLIGENCE_Projeto_ABNT.docx')
ASSETS = ROOT / 'document-assets'


def set_cell_shading(cell, fill):
    properties = cell._tc.get_or_add_tcPr()
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), fill)
    properties.append(shading)


def set_cell_text(cell, text, bold=False):
    cell.text = ''
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run(text)
    run.bold = bold
    run.font.name = 'Arial'
    run.font.size = Pt(10)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    for index, header in enumerate(headers):
        set_cell_text(table.rows[0].cells[index], header, True)
        set_cell_shading(table.rows[0].cells[index], 'D9EAF7')
    for row in rows:
        cells = table.add_row().cells
        for index, value in enumerate(row):
            set_cell_text(cells[index], value)
    doc.add_paragraph()
    return table


def add_image(doc, filename, caption):
    path = ASSETS / filename
    if not path.exists():
        return
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run().add_picture(str(path), width=Cm(15.5))
    caption_paragraph = doc.add_paragraph(caption)
    caption_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption_paragraph.runs[0].italic = True
    caption_paragraph.runs[0].font.size = Pt(10)


def add_heading(doc, text, level=1):
    paragraph = doc.add_heading(text, level=level)
    paragraph.paragraph_format.keep_with_next = True
    return paragraph


def add_body(doc, text):
    paragraph = doc.add_paragraph(text)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph.paragraph_format.first_line_indent = Cm(1.25)
    paragraph.paragraph_format.space_after = Pt(6)
    return paragraph


def add_bullet(doc, text):
    paragraph = doc.add_paragraph(text, style='List Bullet')
    paragraph.paragraph_format.space_after = Pt(3)
    return paragraph


def page_number(paragraph):
    run = paragraph.add_run()
    field_begin = OxmlElement('w:fldChar')
    field_begin.set(qn('w:fldCharType'), 'begin')
    instruction = OxmlElement('w:instrText')
    instruction.set(qn('xml:space'), 'preserve')
    instruction.text = 'PAGE'
    field_end = OxmlElement('w:fldChar')
    field_end.set(qn('w:fldCharType'), 'end')
    run._r.append(field_begin)
    run._r.append(instruction)
    run._r.append(field_end)


doc = Document()
section = doc.sections[0]
section.top_margin = Cm(3)
section.bottom_margin = Cm(2)
section.left_margin = Cm(3)
section.right_margin = Cm(2)

styles = doc.styles
styles['Normal'].font.name = 'Arial'
styles['Normal'].font.size = Pt(12)
styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
for style_name, size in [('Title', 16), ('Heading 1', 14), ('Heading 2', 12)]:
    styles[style_name].font.name = 'Arial'
    styles[style_name].font.size = Pt(size)
    styles[style_name].font.bold = True

footer = section.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
page_number(footer)

# Capa
for text in ['COLÉGIO ESTADUAL CÍVICO-MILITAR DOM PEDRO I – EFMP', '', 'NATAN RAFAEL RYZY DO NASCIMENTO', '']:
    paragraph = doc.add_paragraph(text)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if paragraph.runs:
        paragraph.runs[0].bold = bool(text)
doc.add_paragraph('\n\n\n')
paragraph = doc.add_paragraph('MEC INTELLIGENCE')
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
paragraph.runs[0].bold = True
paragraph.runs[0].font.size = Pt(18)
doc.add_paragraph('\n\n\n')
for text in ['Projeto de desenvolvimento de software', 'PITANGA – PR', '2026']:
    paragraph = doc.add_paragraph(text)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.runs[0].bold = True
doc.add_page_break()

# Folha de rosto
paragraph = doc.add_paragraph('NATAN RAFAEL RYZY DO NASCIMENTO')
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
paragraph.runs[0].bold = True
doc.add_paragraph('\n\n')
paragraph = doc.add_paragraph('MEC INTELLIGENCE')
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
paragraph.runs[0].bold = True
paragraph.runs[0].font.size = Pt(16)
doc.add_paragraph('\n')
paragraph = doc.add_paragraph('Projeto de desenvolvimento de software apresentado ao Colégio Estadual Cívico-Militar Dom Pedro I – EFMP, como requisito parcial para a conclusão e avaliação das atividades práticas de Desenvolvimento de Sistemas.')
paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
paragraph.paragraph_format.left_indent = Cm(7)
paragraph.paragraph_format.first_line_indent = Cm(0)
doc.add_paragraph('\n\n\n')
for text in ['PITANGA – PR', '2026']:
    paragraph = doc.add_paragraph(text)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.runs[0].bold = True
doc.add_page_break()

# Sumário
add_heading(doc, 'SUMÁRIO', 1)
toc = [
    '1 INTRODUÇÃO', '2 OBJETIVO', '3 DESCRIÇÃO DO PROTÓTIPO IMPLEMENTADO',
    '4 PERFIS E PERMISSÕES', '5 FUNCIONALIDADES IMPLEMENTADAS',
    '6 REQUISITOS E LIMITAÇÕES DA VERSÃO ATUAL', '7 TECNOLOGIAS E ORGANIZAÇÃO DO CÓDIGO',
    '8 TELAS DO SISTEMA', '9 CONCLUSÃO', 'REFERÊNCIAS'
]
for item in toc:
    doc.add_paragraph(item)
doc.add_page_break()

add_heading(doc, '1 INTRODUÇÃO', 1)
add_body(doc, 'O MEC INTELLIGENCE é um protótipo de aplicação web para apoiar a organização de uma oficina de veículos pesados. A interface reúne informações de ordens de serviço, equipe, tarefas, agendamentos e solicitações de assistência em uma única experiência de uso.')
add_body(doc, 'A versão apresentada neste documento corresponde ao sistema efetivamente implementado. Trata-se de um protótipo demonstrativo executado no navegador, com dados persistidos localmente no armazenamento do navegador. Portanto, o projeto demonstra fluxos e permissões da interface, mas ainda não representa uma aplicação publicada com servidor, banco de dados remoto ou usuários reais.')
add_body(doc, 'A separação de perfis é um dos pontos centrais do projeto. O patrão administra a oficina e aloca os horários e funcionários; o funcionário acompanha suas tarefas e atualiza o progresso; e o cliente consulta suas ordens e solicita atendimento, sem acesso à agenda interna.')

add_heading(doc, '2 OBJETIVO', 1)
add_body(doc, 'Desenvolver um protótipo navegável de gestão para oficina mecânica, com uma interface clara e responsiva, capaz de demonstrar o fluxo de acesso por perfil, o acompanhamento de ordens de serviço, a organização da equipe, a alocação de funcionários e o controle de agendamentos.')
add_heading(doc, '2.1 Objetivos específicos', 2)
for item in [
    'Demonstrar login de acesso para cliente, funcionário e patrão.',
    'Apresentar painéis diferentes conforme o perfil autenticado.',
    'Permitir ao patrão criar ordens, cadastrar funcionários e alocar agendamentos.',
    'Permitir ao funcionário consultar tarefas e atualizar seu progresso.',
    'Impedir que o cliente visualize a agenda interna ou aloque horários.',
    'Organizar o código em arquivos menores, com configuração, estado, autenticação, interface e ações separadas.'
]:
    add_bullet(doc, item)

add_heading(doc, '3 DESCRIÇÃO DO PROTÓTIPO IMPLEMENTADO', 1)
add_body(doc, 'O sistema inicia em uma tela de login com acessos demonstrativos. Após a autenticação, o usuário é direcionado ao painel correspondente ao seu perfil. O conteúdo da interface, os menus disponíveis e as ações permitidas são definidos pelo papel da sessão.')
add_body(doc, 'Os dados do protótipo são exemplos locais, como ordens OS-1048, OS-1047 e OS-1046, funcionários fictícios e um agendamento demonstrativo. As alterações realizadas durante o uso ficam armazenadas no localStorage do navegador utilizado para a demonstração.')
add_body(doc, 'A personalização visual inclui temas predefinidos, alternância entre modo claro e escuro e um tema OLED com fundo preto. Os textos principais da aplicação ficam centralizados no arquivo de configuração para facilitar a manutenção pelo desenvolvedor.')

add_heading(doc, '4 PERFIS E PERMISSÕES', 1)
add_body(doc, 'As permissões abaixo representam o comportamento implementado no protótipo. Em uma versão de produção, essas regras também deverão ser aplicadas no servidor, além da interface.')
add_table(doc, ['Perfil', 'Acesso implementado', 'Restrições'], [
    ['Patrão', 'Dashboard, ordens, equipe, relatórios, agenda, criação de ordens, cadastro de funcionários e alocação.', 'É o único perfil que cria e remove agendamentos e confirma a alocação.'],
    ['Funcionário', 'Dashboard operacional, tarefas, atualização de progresso e visualização da agenda.', 'Não cria ou remove agendamentos, não cadastra equipe e não altera peças.'],
    ['Cliente', 'Dashboard do veículo, consulta de ordens e solicitação de assistência.', 'Não visualiza a agenda interna, não aloca horários e não altera ordens ou peças.']
])

add_heading(doc, '5 FUNCIONALIDADES IMPLEMENTADAS', 1)
for title_text, description in [
    ('Autenticação demonstrativa', 'Login com três perfis predefinidos e encerramento de sessão. As credenciais são apenas para demonstração local.'),
    ('Dashboard por perfil', 'Resumo de ordens, caminhões, equipe, tarefas e acompanhamento, com conteúdo adaptado ao usuário autenticado.'),
    ('Ordens de serviço', 'Visualização de ordens, status, responsável, veículo, serviço e percentual de progresso. O patrão pode criar e excluir ordens.'),
    ('Alocação de funcionário', 'O patrão pode escolher um funcionário para uma ordem, com indicação visual de compatibilidade.'),
    ('Operação do funcionário', 'O funcionário pode iniciar, pausar e concluir tarefas, atualizando o status e o progresso da ordem.'),
    ('Agenda interna', 'Patrão e funcionário visualizam a agenda. Somente o patrão pode adicionar ou remover agendamentos.'),
    ('Equipe e competências', 'O patrão pode cadastrar funcionários com especialidade, nível e status operacional.'),
    ('Peças', 'A equipe consulta as peças de uma ordem; somente o patrão pode adicionar ou remover registros.'),
    ('Assistência', 'O cliente possui uma tela para solicitar assistência, sem garantia automática de atendimento.'),
    ('Temas e configuração', 'A interface oferece temas visuais, tema OLED, modo claro/escuro e edição de textos diretamente no código de configuração.')
]:
    add_heading(doc, title_text, 2)
    add_body(doc, description)

add_heading(doc, '6 REQUISITOS E LIMITAÇÕES DA VERSÃO ATUAL', 1)
add_body(doc, 'Para manter o documento fiel ao produto entregue, os itens abaixo são explicitamente considerados fora do escopo desta versão:')
for item in [
    'Não há servidor, API REST ou banco de dados PostgreSQL conectado.',
    'Não há cadastro real de clientes, recuperação de senha ou envio de e-mail.',
    'As credenciais são demonstrativas e não devem ser usadas em produção.',
    'Não há publicação, hospedagem, HTTPS, backup ou controle de acesso no servidor.',
    'Não há monetização, anúncios ou assinatura paga implementados.',
    'O cliente não agenda diretamente: ele apenas solicita atendimento; a alocação é feita pelo patrão.',
    'Os indicadores e registros exibidos são dados de demonstração, não métricas operacionais reais.',
    'O armazenamento local não permite uso multiusuário entre dispositivos.'
]:
    add_bullet(doc, item)
add_body(doc, 'Essas limitações não são falhas do protótipo; elas delimitam o que foi efetivamente construído e indicam etapas futuras caso o sistema seja transformado em produto.')

add_heading(doc, '7 TECNOLOGIAS E ORGANIZAÇÃO DO CÓDIGO', 1)
add_body(doc, 'O protótipo foi construído com HTML, CSS e JavaScript, sem dependências de framework. O HTML define o ponto de entrada, o CSS concentra o visual responsivo e os arquivos JavaScript foram divididos por responsabilidade para facilitar leitura e manutenção.')
add_table(doc, ['Arquivo', 'Responsabilidade'], [
    ['config.js', 'Textos editáveis, usuários demonstrativos, temas, menus e dados iniciais.'],
    ['state.js', 'Sessão atual, tema selecionado e regras básicas de permissão.'],
    ['ui.js', 'Temas, modais, notificações e componentes visuais auxiliares.'],
    ['auth.js', 'Login, logout, acessos rápidos e perfil do usuário.'],
    ['views.js', 'Renderização do dashboard, ordens, agenda, equipe, relatórios e assistência.'],
    ['actions.js', 'Criação e alteração de ordens, agendamentos, peças, funcionários e progresso.'],
    ['app.js', 'Inicialização da aplicação quando o documento termina de carregar.']
])

add_heading(doc, '8 TELAS DO SISTEMA', 1)
add_body(doc, 'As imagens abaixo foram capturadas diretamente do protótipo executado no navegador. Elas representam a versão entregue e substituem os espaços reservados do documento anterior.')
add_heading(doc, '8.1 Tela de login', 2)
add_body(doc, 'A tela de login apresenta os acessos demonstrativos dos três perfis. O logo pode ser ocultado pela configuração showLoginLogo em config.js.')
add_image(doc, '02-login.png', 'Figura 1 – Tela de login do protótipo.')
add_heading(doc, '8.2 Painel do patrão', 2)
add_body(doc, 'O painel do patrão apresenta o resumo da operação e a área de alocação inteligente. A partir dele, o responsável acessa ordens, equipe, relatórios e agenda.')
add_image(doc, '03-painel-patrao.png', 'Figura 2 – Dashboard do patrão.')
add_heading(doc, '8.3 Agenda do patrão', 2)
add_body(doc, 'A agenda interna exibe os horários cadastrados e permite ao patrão adicionar ou remover agendamentos. O funcionário pode consultar a agenda, mas não alterá-la; o cliente não possui esse menu.')
add_image(doc, '04-agenda-patrao.png', 'Figura 3 – Agenda interna com permissão de alocação do patrão.')
add_heading(doc, '8.4 Tarefas do funcionário', 2)
add_body(doc, 'O funcionário visualiza suas tarefas e pode atualizar o andamento da execução. A interface operacional não oferece comandos de alocação de horários.')
add_image(doc, '05-tarefas-funcionario.png', 'Figura 4 – Área operacional do funcionário.')
add_heading(doc, '8.5 Painel do cliente', 2)
add_body(doc, 'O cliente visualiza o acompanhamento de suas ordens e a opção de assistência. A agenda interna não aparece para esse perfil, respeitando a regra de que o cliente solicita e o patrão aloca.')
add_image(doc, '01-cliente-dashboard.png', 'Figura 5 – Dashboard do cliente sem acesso à agenda interna.')

add_heading(doc, '9 CONCLUSÃO', 1)
add_body(doc, 'O protótipo MEC INTELLIGENCE apresenta uma interface navegável para apoiar a gestão de uma oficina de veículos pesados. A entrega contempla autenticação demonstrativa, dashboards por perfil, ordens de serviço, controle de tarefas, equipe, agenda interna, assistência e temas visuais.')
add_body(doc, 'A implementação também evidencia a importância de separar permissões. O patrão administra e aloca; o funcionário executa e atualiza; o cliente solicita e acompanha. Essa divisão está refletida nos menus, nas telas e nas validações das ações.')
add_body(doc, 'Como evolução futura, o sistema poderá receber backend, banco de dados, autenticação segura, multiusuário, auditoria e publicação. Esses itens não fazem parte da versão documentada como final e, por isso, foram tratados como limitações em vez de serem apresentados como funcionalidades prontas.')

add_heading(doc, 'REFERÊNCIAS', 1)
for reference in [
    'ABNT. NBR 14724: informação e documentação – trabalhos acadêmicos – apresentação. Rio de Janeiro: ABNT, 2024.',
    'MDN WEB DOCS. HTML, CSS e JavaScript. Disponível em: https://developer.mozilla.org/pt-BR/. Acesso em: 24 nov. 2026.',
    'OWASP FOUNDATION. OWASP Top 10. Disponível em: https://owasp.org/www-project-top-ten/. Acesso em: 24 nov. 2026.'
]:
    paragraph = doc.add_paragraph(reference)
    paragraph.paragraph_format.left_indent = Cm(0)
    paragraph.paragraph_format.first_line_indent = Cm(0)
    paragraph.paragraph_format.space_after = Pt(6)

doc.save(OUTPUT)
print(f'Arquivo atualizado: {OUTPUT}')
