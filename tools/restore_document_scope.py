from pathlib import Path
from docx import Document

path = Path(r'C:\Users\Positivo\Downloads\MEC_INTELLIGENCE_Projeto_ABNT.docx')
doc = Document(path)

def replace_current(current, original):
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() == current.strip():
            paragraph.text = original
            return True
    return False

restore = {
    'Nesse contexto, apresenta-se o MEC INTELLIGENCE, um protótipo frontend demonstrativo para gerenciamento de oficina de veículos pesados. A versão implementada reúne dashboards, ordens de serviço, equipe, tarefas, agenda interna e assistência em uma única interface, utilizando dados de demonstração armazenados localmente no navegador.':
    'Nesse contexto, apresenta-se o MEC INTELLIGENCE, uma proposta de sistema web destinado ao gerenciamento de oficinas mecânicas. A plataforma pretende reunir informações sobre clientes, veículos, funcionários, especialidades, serviços, agendamentos e ordens de serviço em um ambiente único. O sistema também prevê um mecanismo de recomendação de mecânicos, que analisa a complexidade do serviço, as competências cadastradas e a disponibilidade dos profissionais.',
    'O projeto implementado considera três perfis principais: patrão, funcionário e cliente. O patrão organiza a oficina e aloca horários; o funcionário consulta e atualiza suas tarefas; e o cliente solicita atendimento e acompanha suas ordens, sem visualizar a agenda interna.':
    'O projeto considera três perfis principais de utilização: administrador, mecânico e cliente. O administrador organiza a oficina e acompanha o fluxo geral; o mecânico consulta e atualiza as tarefas atribuídas; e o cliente solicita serviços, agenda atendimentos e acompanha o andamento de sua ordem. Cada perfil terá permissões compatíveis com sua função.',
    'A versão atual permite ao funcionário atualizar o status e o percentual de progresso das tarefas. Registro detalhado de horas, cronômetros, serviços adicionais e auditoria de alterações não fazem parte do protótipo entregue e ficam registrados como evolução futura.':
    'Além da distribuição de tarefas, o MEC INTELLIGENCE prevê o registro de horários de início, pausa e conclusão das atividades. Esses registros permitirão calcular o tempo efetivamente trabalhado e produzir informações gerenciais. O sistema também deverá permitir a inclusão de serviços adicionais identificados durante uma manutenção, mantendo o histórico associado ao mesmo atendimento e ao veículo correspondente.',
    'A versão atual inclui agenda interna para patrão e funcionário e uma tela de solicitação de assistência para o cliente. O cliente não escolhe nem aloca horários: ele apenas solicita atendimento, enquanto a definição do agendamento fica sob responsabilidade do patrão.':
    'A proposta inclui recursos de agendamento e solicitação de socorro mecânico. O pedido emergencial será destacado para análise da equipe administrativa, mas sua prioridade não significará atendimento automático nem garantia de disponibilidade. A oficina deverá confirmar a possibilidade de deslocamento e informar ao cliente as condições do atendimento.',
    'O sistema implementado é uma aplicação web frontend responsiva, acessível por navegador em computadores e celulares. A versão atual utiliza HTML, CSS, JavaScript e localStorage; não possui servidor, API ou banco de dados remoto conectado.':
    'O sistema será concebido como uma aplicação web responsiva, acessível por navegadores em computadores, tablets e celulares. A escolha busca reduzir a necessidade de instalação e facilitar a utilização por diferentes perfis. A arquitetura técnica prevista utiliza uma interface web, uma camada de servidor responsável pelas regras de negócio e um banco de dados relacional.',
    'O cliente consegue consultar o andamento das ordens exibidas no protótipo após o acesso demonstrativo. Código externo de acompanhamento, notificações e autenticação de produção ainda não foram implementados.':
    'A possibilidade de acompanhar o andamento da ordem de serviço também beneficia o cliente. Em vez de depender exclusivamente de ligações ou mensagens, o proprietário poderá consultar etapas gerais do atendimento por meio de um código de acompanhamento seguro. Isso tende a melhorar a comunicação e reduzir consultas repetitivas à recepção.',
    'Serviços adicionais, aprovação comercial e histórico detalhado não estão disponíveis nesta versão. A tela atual concentra-se na consulta da ordem, peças e progresso demonstrativo.':
    'A inclusão de serviços adicionais na mesma ordem permite registrar problemas encontrados durante a manutenção sem perder a relação com o atendimento original. O cliente deverá ser informado sobre a necessidade do serviço adicional e, quando houver custo ou alteração de prazo, a execução dependerá de sua autorização, conforme as regras comerciais da oficina.',
    'Monetização, anúncios, assinaturas e pagamentos foram removidos do escopo desta versão porque não foram implementados no protótipo. O sistema atual é uma demonstração acadêmica local, sem modelo comercial ativo.':
    'Por fim, o modelo de acesso gratuito com anúncios e opção paga para removê-los procura reduzir a barreira de entrada. A proposta não prevê bloquear as funções essenciais atrás de uma assinatura. A sustentabilidade financeira dependerá da adesão de usuários, do volume de acessos e da disponibilidade de anunciantes, fatores que deverão ser avaliados em testes e estudos posteriores.',
}
for current, original in restore.items():
    replace_current(current, original)

objectives = {
    'Desenvolver e documentar um protótipo web demonstrativo para gerenciamento de oficina, com acesso por perfil, controle de ordens, equipe, tarefas, agenda interna, assistência e acompanhamento do andamento pelo cliente.':
    'Desenvolver a especificação e o protótipo de um sistema web para gerenciamento de oficinas mecânicas, com cadastro de clientes, veículos, funcionários e serviços, controle de ordens de serviço, recomendação de profissionais conforme suas competências e disponibilidade, acompanhamento da execução e consulta do andamento pelo cliente.',
    'Demonstrar login e controle de acesso por perfil no frontend.': 'Criar mecanismos de autenticação e controle de acesso para os perfis de administrador, mecânico e cliente.',
    'Permitir, no protótipo, o cadastro local de funcionários pelo patrão e a consulta de dados demonstrativos de veículos, equipe e ordens.': 'Permitir o cadastro e a atualização dos dados dos clientes, veículos, funcionários, especialidades e serviços oferecidos pela oficina.',
    'Exibir e criar ordens de serviço demonstrativas com veículo, serviço, responsável, status e progresso.': 'Registrar ordens de serviço com descrição do problema, classificação de complexidade, prioridade, veículo e serviços solicitados.',
    'Apresentar uma recomendação visual de funcionário para apoiar a decisão de alocação do patrão.': 'Implementar uma lógica de recomendação que considere a especialidade exigida, o nível de competência e a disponibilidade do mecânico.',
    'Permitir que o patrão escolha o funcionário e registre a alocação no estado local do protótipo.': 'Permitir que a chefia aprove, rejeite ou substitua a sugestão de alocação, registrando a decisão.',
    'Disponibilizar ao funcionário uma lista de tarefas com ações de iniciar, pausar e concluir.': 'Disponibilizar ao mecânico uma lista de tarefas e ações para iniciar, pausar, retomar, concluir ou sinalizar problemas.',
    'Atualizar status e percentual de progresso; cronômetro e histórico completo ficam fora do escopo atual.': 'Registrar os tempos de execução e manter histórico das alterações relevantes da ordem de serviço.',
    'Consultar peças e informações da ordem; serviços adicionais e aprovação do cliente ficam fora do escopo atual.': 'Permitir a inclusão de serviços adicionais vinculados ao atendimento original, com registro de aprovação do cliente quando necessário.',
    'Oferecer agenda interna para patrão e funcionário, solicitação de assistência para cliente e consulta demonstrativa de ordens.': 'Oferecer agendamento, solicitação de socorro mecânico e acompanhamento seguro do andamento da ordem.'
}
for current, original in objectives.items():
    replace_current(current, original)

# Mantém a descrição original do perfil cliente, mas ajusta apenas a regra final de agenda.
replace_current(
    'O cliente é o usuário externo da oficina. No protótipo, ele consulta ordens demonstrativas e solicita assistência. Não visualiza a agenda interna nem escolhe horários; a alocação é responsabilidade do patrão.',
    'O cliente será o usuário externo da oficina. Poderá criar uma conta, cadastrar um ou mais veículos, solicitar serviços e acompanhar o andamento de sua ordem. A solicitação de horário será encaminhada à oficina; o cliente não visualizará a agenda interna nem realizará a alocação, que será responsabilidade do patrão. Também poderá informar a urgência percebida, sem que essa classificação substitua a avaliação técnica da oficina. Em caso de socorro mecânico, o cliente fornecerá localização e contato, sujeitos à confirmação do atendimento.'
)
replace_current(
    'O acompanhamento é demonstrativo e ocorre dentro da sessão local. Código individual, validação adicional e autenticação de produção não foram implementados.',
    'O acompanhamento da ordem será realizado por autenticação na conta ou por código individual de consulta, associado a uma validação adicional. A placa do veículo, isoladamente, não será considerada credencial suficiente, pois pode ser conhecida por terceiros.'
)

# Restaura integralmente a seção de monetização, que fazia parte da estrutura solicitada.
paragraphs = doc.paragraphs
start = next((i for i, p in enumerate(paragraphs) if p.text.strip() == '12 LIMITAÇÕES E EVOLUÇÕES FUTURAS'), None)
end = next((i for i, p in enumerate(paragraphs) if i > (start or 0) and p.text.strip() == '13 CONCLUSÃO'), None)
if start is not None and end is not None:
    monetization = [
        '12 MONETIZAÇÃO',
        'A estratégia de monetização do MEC INTELLIGENCE será baseada em um modelo de acesso gratuito com publicidade e uma opção paga para remoção dos anúncios. A proposta procura reduzir a barreira de entrada para oficinas e clientes, permitindo o uso das funcionalidades essenciais sem a obrigação de contratar uma assinatura.',
        '12.1 Acesso gratuito com anúncios',
        'Na modalidade gratuita, os usuários poderão utilizar os recursos centrais do sistema, como cadastro, gerenciamento de ordens de serviço, alocação, acompanhamento e agendamento. A receita será obtida por meio de anúncios exibidos em espaços reservados da interface ou por formatos publicitários compatíveis com a experiência de uso.',
        'A publicidade deverá ser discreta e não poderá interferir em tarefas operacionais. Não serão exibidos anúncios sobre botões de iniciar ou concluir serviço, formulários de autorização, cronômetros, alertas de segurança ou solicitações de socorro. Também não deverão ser utilizados formatos que induzam cliques acidentais ou confundam publicidade com comandos do sistema.',
        '12.2 Opção paga para remover anúncios',
        'O usuário poderá contratar uma opção de remoção de anúncios. Essa modalidade manterá as funcionalidades essenciais da versão gratuita, mas retirará a publicidade da experiência de utilização. O pagamento poderá ser estruturado como assinatura mensal ou anual, após avaliação de custos, aceitação do público e viabilidade financeira.',
        'A contratação deverá informar claramente preço, período, renovação, cancelamento e condições de reembolso. O sistema deverá confirmar o pagamento por meio de um provedor confiável e atualizar o status da conta somente após receber confirmação válida. O cancelamento deverá impedir cobranças futuras conforme as regras do meio de pagamento.',
        '',
        '12 MONETIZAÇÃO',
        '12.3 Política de exibição dos anúncios',
        'A publicidade deverá respeitar o contexto de cada perfil. Na área administrativa, poderá ocupar espaços laterais ou rodapés, sem interferir em decisões. Na área do mecânico, deverá ser evitada durante a execução operacional. Para o cliente, poderá aparecer em páginas informativas, sem interromper agendamentos ou consultas.',
        'Os anúncios deverão ser identificados e compatíveis com a finalidade da plataforma. Cookies e tecnologias de rastreamento deverão respeitar a legislação de proteção de dados e as escolhas de privacidade do usuário.',
        '12.4 Fontes de receita e sustentabilidade',
        'O modelo possui duas fontes principais: receita publicitária, que depende de impressões, interações válidas e condições comerciais da rede de anúncios; e receita da opção paga de remoção, que depende da quantidade de usuários que optarem por pagar. Não é possível estimar receita com precisão antes de conhecer o número de usuários ativos, frequência de utilização, taxa de conversão e valores praticados pelos provedores.',
        'A viabilidade será avaliada por usuários ativos, oficinas cadastradas, receita média, adesão à remoção de anúncios e custos de hospedagem e suporte. Os formatos deverão ser revistos se prejudicarem a experiência ou não apresentarem retorno suficiente.',
        '12.5 Princípios do modelo comercial',
        'As funcionalidades essenciais de gestão não serão bloqueadas apenas para forçar a contratação da opção paga.',
        'A publicidade deverá ser identificada e posicionada fora das áreas operacionais críticas.',
        'A opção de remoção deverá ser simples de localizar, contratar e cancelar.',
        'Os dados pessoais não deverão ser vendidos; qualquer tratamento para publicidade deverá respeitar a legislação e as escolhas do usuário.'
    ]
    for offset in range(start, end):
        paragraphs[offset].text = monetization[offset - start] if offset - start < len(monetization) else ''

# Restaura a tabela de tecnologias como proposta arquitetural, sem afirmar que tudo já existe.
for table in doc.tables:
    for row in table.rows:
        first = row.cells[0].text if row.cells else ''
        if first == 'Servidor':
            row.cells[1].text = 'Node.js'
            row.cells[2].text = 'Executar regras de negócio e atender requisições.'
        elif first == 'API':
            row.cells[1].text = 'API REST sobre HTTP'
            row.cells[2].text = 'Comunicar interface e servidor.'
        elif first == 'Banco de dados':
            row.cells[1].text = 'PostgreSQL'
            row.cells[2].text = 'Armazenar usuários, clientes, veículos e operações.'
        elif first == 'Prototipação':
            row.cells[1].text = 'Ferramenta de desenho de interfaces'
            row.cells[2].text = 'Planejar e validar a disposição das telas.'

doc.save(path)
print('Conteúdo original compatível restaurado; telas mobile preservadas.')
