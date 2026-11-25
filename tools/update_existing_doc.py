from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

SOURCE = Path(r'C:\Users\Positivo\Downloads\MEC_INTELLIGENCE_Projeto_ABNT.docx')
ASSETS = Path(r'C:\Vs Code\Mec intelligence\document-assets')

doc = Document(SOURCE)

def replace_exact(old, new, limit=None):
    count = 0
    for paragraph in doc.paragraphs:
        if old in paragraph.text and (limit is None or count < limit):
            paragraph.text = new
            count += 1
    return count

def replace_first(old, new):
    return replace_exact(old, new, 1)

# Corrige afirmações que descreviam funcionalidades futuras como se já existissem.
replacements = {
    'Nesse contexto, apresenta-se o MEC INTELLIGENCE, uma proposta de sistema web destinado ao gerenciamento de oficinas mecânicas. A plataforma pretende reunir informações sobre clientes, veículos, funcionários, especialidades, serviços, agendamentos e ordens de serviço em um ambiente único. O sistema também prevê um mecanismo de recomendação de mecânicos, que analisa a complexidade do serviço, as competências cadastradas e a disponibilidade dos profissionais.':
    'Nesse contexto, apresenta-se o MEC INTELLIGENCE, um protótipo frontend demonstrativo para gerenciamento de oficina de veículos pesados. A versão implementada reúne dashboards, ordens de serviço, equipe, tarefas, agenda interna e assistência em uma única interface, utilizando dados de demonstração armazenados localmente no navegador.',
    'O projeto considera três perfis principais de utilização: administrador, mecânico e cliente. O administrador organiza a oficina e acompanha o fluxo geral; o mecânico consulta e atualiza as tarefas atribuídas; e o cliente solicita serviços, agenda atendimentos e acompanha o andamento de sua ordem. Cada perfil terá permissões compatíveis com sua função.':
    'O projeto implementado considera três perfis principais: patrão, funcionário e cliente. O patrão organiza a oficina e aloca horários; o funcionário consulta e atualiza suas tarefas; e o cliente solicita atendimento e acompanha suas ordens, sem visualizar a agenda interna.',
    'Além da distribuição de tarefas, o MEC INTELLIGENCE prevê o registro de horários de início, pausa e conclusão das atividades. Esses registros permitirão calcular o tempo efetivamente trabalhado e produzir informações gerenciais. O sistema também deverá permitir a inclusão de serviços adicionais identificados durante uma manutenção, mantendo o histórico associado ao mesmo atendimento e ao veículo correspondente.':
    'A versão atual permite ao funcionário atualizar o status e o percentual de progresso das tarefas. Registro detalhado de horas, cronômetros, serviços adicionais e auditoria de alterações não fazem parte do protótipo entregue e ficam registrados como evolução futura.',
    'A proposta inclui recursos de agendamento e solicitação de socorro mecânico. O pedido emergencial será destacado para análise da equipe administrativa, mas sua prioridade não significará atendimento automático nem garantia de disponibilidade. A oficina deverá confirmar a possibilidade de deslocamento e informar ao cliente as condições do atendimento.':
    'A versão atual inclui agenda interna para patrão e funcionário e uma tela de solicitação de assistência para o cliente. O cliente não escolhe nem aloca horários: ele apenas solicita atendimento, enquanto a definição do agendamento fica sob responsabilidade do patrão.',
    'O sistema será concebido como uma aplicação web responsiva, acessível por navegadores em computadores, tablets e celulares. A escolha busca reduzir a necessidade de instalação e facilitar a utilização por diferentes perfis. A arquitetura técnica prevista utiliza uma interface web, uma camada de servidor responsável pelas regras de negócio e um banco de dados relacional.':
    'O sistema implementado é uma aplicação web frontend responsiva, acessível por navegador em computadores e celulares. A versão atual utiliza HTML, CSS, JavaScript e localStorage; não possui servidor, API ou banco de dados remoto conectado.',
    'A possibilidade de acompanhar o andamento da ordem de serviço também beneficia o cliente. Em vez de depender exclusivamente de ligações ou mensagens, o proprietário poderá consultar etapas gerais do atendimento por meio de um código de acompanhamento seguro. Isso tende a melhorar a comunicação e reduzir consultas repetitivas à recepção.':
    'O cliente consegue consultar o andamento das ordens exibidas no protótipo após o acesso demonstrativo. Código externo de acompanhamento, notificações e autenticação de produção ainda não foram implementados.',
    'A inclusão de serviços adicionais na mesma ordem permite registrar problemas encontrados durante a manutenção sem perder a relação com o atendimento original. O cliente deverá ser informado sobre a necessidade do serviço adicional e, quando houver custo ou alteração de prazo, a execução dependerá de sua autorização, conforme as regras comerciais da oficina.':
    'Serviços adicionais, aprovação comercial e histórico detalhado não estão disponíveis nesta versão. A tela atual concentra-se na consulta da ordem, peças e progresso demonstrativo.',
    'Por fim, o modelo de acesso gratuito com anúncios e opção paga para removê-los procura reduzir a barreira de entrada. A proposta não prevê bloquear as funções essenciais atrás de uma assinatura. A sustentabilidade financeira dependerá da adesão de usuários, do volume de acessos e da disponibilidade de anunciantes, fatores que deverão ser avaliados em testes e estudos posteriores.':
    'Monetização, anúncios, assinaturas e pagamentos foram removidos do escopo desta versão porque não foram implementados no protótipo. O sistema atual é uma demonstração acadêmica local, sem modelo comercial ativo.',
    'Esta seção será destinada à apresentação visual das principais interfaces do MEC INTELLIGENCE. Os protótipos deverão demonstrar como os perfis acessam as funcionalidades descritas nos requisitos. As imagens serão inseridas posteriormente pelo autor, mantendo correspondência com os fluxos e permissões definidos neste documento.':
    'Esta seção apresenta capturas reais do protótipo em viewport vertical de celular. As imagens demonstram os fluxos e as permissões efetivamente implementados para cada perfil.'
}
for old, new in replacements.items():
    replace_exact(old, new)

# Ajusta objetivos que estavam escritos como promessa de implementação futura.
objective_replacements = {
    'Desenvolver a especificação e o protótipo de um sistema web para gerenciamento de oficinas mecânicas, com cadastro de clientes, veículos, funcionários e serviços, controle de ordens de serviço, recomendação de profissionais conforme suas competências e disponibilidade, acompanhamento da execução e consulta do andamento pelo cliente.':
    'Desenvolver e documentar um protótipo web demonstrativo para gerenciamento de oficina, com acesso por perfil, controle de ordens, equipe, tarefas, agenda interna, assistência e acompanhamento do andamento pelo cliente.',
    'Criar mecanismos de autenticação e controle de acesso para os perfis de administrador, mecânico e cliente.':
    'Demonstrar login e controle de acesso por perfil no frontend.',
    'Permitir o cadastro e a atualização dos dados dos clientes, veículos, funcionários, especialidades e serviços oferecidos pela oficina.':
    'Permitir, no protótipo, o cadastro local de funcionários pelo patrão e a consulta de dados demonstrativos de veículos, equipe e ordens.',
    'Registrar ordens de serviço com descrição do problema, classificação de complexidade, prioridade, veículo e serviços solicitados.':
    'Exibir e criar ordens de serviço demonstrativas com veículo, serviço, responsável, status e progresso.',
    'Implementar uma lógica de recomendação que considere a especialidade exigida, o nível de competência e a disponibilidade do mecânico.':
    'Apresentar uma recomendação visual de funcionário para apoiar a decisão de alocação do patrão.',
    'Permitir que a chefia aprove, rejeite ou substitua a sugestão de alocação, registrando a decisão.':
    'Permitir que o patrão escolha o funcionário e registre a alocação no estado local do protótipo.',
    'Disponibilizar ao mecânico uma lista de tarefas e ações para iniciar, pausar, retomar, concluir ou sinalizar problemas.':
    'Disponibilizar ao funcionário uma lista de tarefas com ações de iniciar, pausar e concluir.',
    'Registrar os tempos de execução e manter histórico das alterações relevantes da ordem de serviço.':
    'Atualizar status e percentual de progresso; cronômetro e histórico completo ficam fora do escopo atual.',
    'Permitir a inclusão de serviços adicionais vinculados ao atendimento original, com registro de aprovação do cliente quando necessário.':
    'Consultar peças e informações da ordem; serviços adicionais e aprovação do cliente ficam fora do escopo atual.',
    'Oferecer agendamento, solicitação de socorro mecânico e acompanhamento seguro do andamento da ordem.':
    'Oferecer agenda interna para patrão e funcionário, solicitação de assistência para cliente e consulta demonstrativa de ordens.'
}
for old, new in objective_replacements.items():
    replace_exact(old, new)

# Corrige diretamente a descrição do cliente, que antes dizia que ele escolhia horários.
replace_first('O cliente será o usuário externo da oficina. Poderá criar uma conta, cadastrar um ou mais veículos, solicitar serviços e escolher horários disponíveis. Também poderá informar a urgência percebida, sem que essa classificação substitua a avaliação técnica da oficina. Em caso de socorro mecânico, o cliente fornecerá localização e contato, sujeitos à confirmação do atendimento.',
              'O cliente é o usuário externo da oficina. No protótipo, ele consulta ordens demonstrativas e solicita assistência. Não visualiza a agenda interna nem escolhe horários; a alocação é responsabilidade do patrão.')
replace_first('O acompanhamento da ordem será realizado por autenticação na conta ou por código individual de consulta, associado a uma validação adicional. A placa do veículo, isoladamente, não será considerada credencial suficiente, pois pode ser conhecida por terceiros.',
              'O acompanhamento é demonstrativo e ocorre dentro da sessão local. Código individual, validação adicional e autenticação de produção não foram implementados.')

# Substitui a seção de monetização por limitações reais sem apagar seus parágrafos, preservando o volume do documento.
paragraphs = doc.paragraphs
start = next((i for i, p in enumerate(paragraphs) if p.text.strip() == '12 MONETIZAÇÃO'), None)
end = next((i for i, p in enumerate(paragraphs) if i > (start or 0) and p.text.strip() == '13 CONCLUSÃO'), None)
if start is not None and end is not None:
    limitations = [
        '12 LIMITAÇÕES E EVOLUÇÕES FUTURAS',
        'A versão documentada é um protótipo frontend acadêmico. O foco desta entrega está na navegação, na apresentação visual e na demonstração das permissões por perfil.',
        'Não há servidor, API REST ou banco de dados remoto conectado. Os dados são fictícios e ficam no armazenamento local do navegador.',
        'As credenciais disponíveis são demonstrativas e não devem ser utilizadas como mecanismo de segurança em produção.',
        'Não foram implementados cadastro real de clientes, recuperação de senha, envio de e-mails ou notificações externas.',
        'Não foram implementados cronômetro, apontamento detalhado de horas, auditoria completa ou serviços adicionais com aprovação comercial.',
        'A agenda é interna: o patrão aloca horários e o funcionário pode consultar. O cliente apenas solicita atendimento.',
        'Não foram implementados hospedagem, HTTPS, backup, multiusuário entre dispositivos ou integração com serviços externos.',
        'Relatórios, indicadores, percentual de progresso e recomendações exibidos na interface são dados de demonstração.',
        'Uma evolução futura poderá criar um backend seguro, banco de dados, autenticação real e sincronização entre dispositivos.',
        'Outra evolução possível é adicionar testes automatizados, auditoria, recuperação de acesso e regras comerciais da oficina.',
        'Esses itens não foram apresentados como funcionalidades prontas porque não fazem parte do protótipo final entregue.',
    ]
    for index in range(start, end):
        paragraphs[index].text = limitations[min(index - start, len(limitations) - 1)]

# Corrige tecnologias propostas para refletir a entrega real, sem excluir a tabela.
for table in doc.tables:
    for row in table.rows:
        values = [cell.text for cell in row.cells]
        if values and values[0] == 'Servidor':
            row.cells[1].text = 'Não implementado nesta versão'
            row.cells[2].text = 'Backend futuro; não participa do protótipo atual.'
        elif values and values[0] == 'API':
            row.cells[1].text = 'Não implementada nesta versão'
            row.cells[2].text = 'Comunicação futura entre frontend e backend.'
        elif values and values[0] == 'Banco de dados':
            row.cells[1].text = 'localStorage do navegador'
            row.cells[2].text = 'Persistência local de dados demonstrativos.'
        elif values and values[0] == 'Prototipação':
            row.cells[1].text = 'HTML, CSS e JavaScript'
            row.cells[2].text = 'Interface navegável implementada no projeto.'

# Troca cada espaço reservado por uma imagem vertical de celular, mantendo a seção e o conteúdo do documento.
screens = {
    '[ESPAÇO RESERVADO PARA INSERÇÃO DA IMAGEM – TELA DE LOGIN]': ('02-login.png', 'Figura – Tela de login em viewport mobile.'),
    '[ESPAÇO RESERVADO PARA INSERÇÃO DA IMAGEM – PAINEL ADMINISTRATIVO]': ('03-painel-patrao.png', 'Figura – Painel do patrão em viewport mobile.'),
    '[ESPAÇO RESERVADO PARA INSERÇÃO DA IMAGEM – ÁREA DO MECÂNICO]': ('05-tarefas-funcionario.png', 'Figura – Tarefas do funcionário em viewport mobile.'),
    '[ESPAÇO RESERVADO PARA INSERÇÃO DA IMAGEM – ÁREA DO CLIENTE]': ('01-cliente-dashboard.png', 'Figura – Área do cliente em viewport mobile.'),
}
# Agenda pode aparecer como espaço próprio ou ser acrescentada à seção administrativa.
for paragraph in doc.paragraphs:
    if paragraph.text.strip() in screens:
        filename, caption = screens[paragraph.text.strip()]
        paragraph.clear()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.add_run().add_picture(str(ASSETS / filename), width=Cm(9.2))
        run = paragraph.add_run(f'\n{caption}')
        run.italic = True
        run.font.size = Pt(10)

# Insere a agenda mobile logo após a legenda do painel, sem remover páginas existentes.
if not any('Agenda do patrão em viewport mobile' in paragraph.text for paragraph in doc.paragraphs):
  for index, paragraph in enumerate(list(doc.paragraphs)):
    if 'Painel do patrão em viewport mobile' in paragraph.text:
        new_paragraph = paragraph.insert_paragraph_before()
        new_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        new_paragraph.add_run().add_picture(str(ASSETS / '04-agenda-patrao.png'), width=Cm(9.2))
        run = new_paragraph.add_run('\nFigura – Agenda do patrão em viewport mobile.')
        run.italic = True
        run.font.size = Pt(10)
        break

doc.save(SOURCE)
print(f'Atualizado sem remover seções: {SOURCE}')
