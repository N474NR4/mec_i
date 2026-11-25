// Configuração central da aplicação. Edite os textos deste arquivo.
const $ = selector => document.querySelector(selector);

function store(key, value) {
  if (value !== undefined) {
    localStorage.setItem(key, JSON.stringify(value));
    return value;
  }

  try {
    return JSON.parse(localStorage.getItem(key) || 'null');
  } catch {
    return null;
  }
}

const texts = {
  showLoginLogo: false,
  siteTitle: 'MEC Intelligence',
  appName: 'Mec',
  workshopName: 'Mec Intelligence',
  loginTitle: 'Entrar no sistema',
  loginSubtitle: 'Acesso demonstrativo frontend · Brasil',
  heroTitle: 'Mec Intelligence',
  heroDescription: 'Gestão inteligente para quem mantém a estrada em movimento.',
  loginButton: 'Acessar plataforma →',
  quickTransportadora: 'Cliente',
  quickMecanico: 'Funcionario',
  quickGestor: 'Gestor'
};

const users = {
  cliente: { email: 'cliente@mecintelligence.com', pass: 'mec123', name: 'Marina Costa', label: 'Cliente' },
  funcionario: { email: 'funcionario@mecintelligence.com', pass: 'mec123', name: 'Rafael Silva', label: 'Mecânico' },
  patrao: { email: 'patrao@mecintelligence.com', pass: 'mec123', name: 'João Mendes', label: 'Patrão' }
};

const themes = {
  aurora: ['#36d6c4', '#ff9e5e', '#08111f'], oceano: ['#49a9ff', '#ffcf70', '#081321'],
  diesel: ['#f6a623', '#eb596e', '#17120d'], floresta: ['#83d66b', '#f2c14e', '#0b1713'],
  brasil: ['#39d353', '#ffdf00', '#07170e'], racing: ['#ff4d67', '#52d5ff', '#170b16'],
  concreto: ['#b9c3cf', '#ff8b5c', '#161a20'], noturno: ['#a78bfa', '#f472b6', '#100d20'],
  logistica: ['#22d3ee', '#facc15', '#07151b'], claro: ['#1677ff', '#ff7b54', '#f3f7fa'],
  oled: ['#00e5ff', '#ff3d81', '#000000']
};

const navs = {
  patrao: [['◈', 'Visão geral', 'dashboard'], ['▣', 'Ordens de serviço', 'orders'], ['♙', 'Equipe & competências', 'team'], ['◷', 'Agendamentos', 'schedule'], ['▤', 'Relatórios', 'reports']],
  funcionario: [['◉', 'Minha operação', 'dashboard'], ['▣', 'Minhas tarefas', 'orders'], ['◷', 'Agendamentos', 'schedule']],
  cliente: [['◉', 'Meu veículo', 'dashboard'], ['▣', 'Minhas ordens', 'orders'], ['⚑', 'Assistência', 'road']]
};

const defaultData = {
  orders: [
    { id: 'OS-1048', car: 'Volvo FH 540 • BCD-2E34', service: 'Revisão de câmbio automatizado', status: 'Em execução', tech: 'Rafael Silva', progress: 68 },
    { id: 'OS-1047', car: 'Scania R 450 • KLM-9P80', service: 'Diagnóstico eletrônico EBS', status: 'Aguardando', tech: '—', progress: 22 },
    { id: 'OS-1046', car: 'Mercedes-Benz Actros • QWE-5R67', service: 'Freios, suspensão e quinta roda', status: 'Concluída', tech: 'Ana Souza', progress: 100 }
  ],
  appointments: [{ time: '09:30', name: 'Transportadora Costa Norte', service: 'Troca de óleo e filtros' }],
  employees: [
    { name: 'Ana Souza', specialty: 'Transmissão', level: 5, status: 'Livre' },
    { name: 'Rafael Silva', specialty: 'Diagnóstico eletrônico', level: 4, status: 'Ocupado' },
    { name: 'Bruno Lima', specialty: 'Suspensão e freios', level: 4, status: 'Livre' },
    { name: 'Carlos Mendes', specialty: 'Motores diesel', level: 3, status: 'Ausente' }
  ],
  parts: {
    'OS-1048': [{ name: 'Filtro de combustível', qty: 2, price: 189.9 }, { name: 'Óleo motor 15W40', qty: 24, price: 42.5 }],
    'OS-1047': [{ name: 'Sensor ABS dianteiro', qty: 2, price: 420 }]
  }
};

const data = store('mi-data') || structuredClone(defaultData);
data.employees ||= structuredClone(defaultData.employees);
data.parts ||= structuredClone(defaultData.parts);
function saveData() { store('mi-data', data); }
