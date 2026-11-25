function title() {
  if (current === 'dashboard') return `Bom dia, ${session.name.split(' ')[0]}.`;
  return navs[session.role].find(item => item[2] === current)?.[1] || texts.appName;
}

function render() {
  if (!session) return login();
  applyTheme();
  const navigation = navs[session.role];
  document.querySelector('#app').innerHTML = `<div class="shell"><aside class="side"><span class="logo">${texts.appName}</span><nav class="nav">${navigation.map(item => `<button class="${current === item[2] ? 'active' : ''}" onclick="go('${item[2]}')">${item[0]} &nbsp; ${item[1]}</button>`).join('')}</nav><div class="side-foot">Sessão ativa<br><b>${session.label}</b><br><button class="ghost" onclick="logout()">↪ Sair da conta</button></div></aside><main class="main"><header class="top"><div><div class="eyebrow">${session.label} / ${texts.workshopName}</div><h1>${title()}</h1></div><div class="actions"><button class="secondary" onclick="toggleTheme()">${theme.mode === 'light' ? '☾' : '☀'} <span class="hide">Tema</span></button><button class="ghost" onclick="openSettings()">⚙</button><button class="avatar" onclick="openProfile()" title="Configurar perfil">${session.name[0]}</button><button class="secondary" onclick="logout()">Sair</button></div></header>${page()}</main></div>`;
}

function go(route) {
  if (route === 'schedule' && !canViewSchedule()) return;
  current = route;
  render();
}

function page() {
  if (current === 'schedule' && !canViewSchedule()) current = 'dashboard';
  return ({ dashboard, orders, team: simpleTeam, schedule, reports, road }[current] || dashboard)();
}

function dashboard() {
  const admin = session.role === 'patrao';
  const client = session.role === 'cliente';
  const stat = (label, value, trend) => `<div class="card stat"><span class="eyebrow">${label}</span><b>${value}</b><span class="trend">${trend}</span></div>`;
  return `<section class="grid stats">${stat(admin ? 'Ordens abertas' : client ? 'Ordens da frota' : 'Tarefas hoje', admin ? '12' : client ? '02' : '04', '↑ 18% este mês')}${stat('Caminhões em box', admin ? '07' : '02', 'Fluxo saudável')}${stat(admin ? 'Equipe disponível' : 'Tempo efetivo', admin ? '06/09' : '04h20', 'Atualizado agora')}${stat('Disponibilidade da frota', '94%', '★★★★★')}</section><br><section class="grid cols"><div class="card"><div class="section-title"><h3>${admin ? 'Pulso da operação' : 'Acompanhamento em tempo real'}</h3><button class="ghost" onclick="go('orders')">Ver tudo →</button></div><div class="list">${data.orders.slice(0, 3).map(orderRow).join('')}</div></div><div class="card"><div class="section-title"><h3>${admin ? 'Alocação inteligente' : 'Próximo passo'}</h3></div>${admin ? `<p class="muted">3 itens aguardam um profissional elegível.</p><div class="row"><div><strong>OS-1047</strong><br><span class="muted">Diagnóstico eletrônico EBS</span></div><span class="tag">98% match</span></div><button class="primary" onclick="openAssign()">Revisar recomendações</button>` : client ? `<p class="muted">Seu Volvo FH 540 está em manutenção.</p><div class="bar"><i style="width:68%"></i></div><p><strong>Diagnóstico concluído</strong><br><span class="muted">Próxima etapa: montagem</span></p>` : `<p class="muted">Sua tarefa prioritária está pronta.</p><button class="primary" onclick="startTask()">Iniciar OS-1048</button>`}</div></section>`;
}

function orderRow(order) {
  return `<div class="row"><div><strong>${order.id}</strong><br><span class="muted">${order.service} · ${order.car}</span></div><div style="min-width:100px"><span class="tag ${order.status === 'Aguardando' ? 'warn' : ''}">${order.status}</span><div class="bar"><i style="width:${order.progress}%"></i></div></div></div>`;
}

function orders() {
  if (session.role === 'funcionario') return employeeOrders();
  const canDelete = session.role === 'patrao';
  return `<div class="card"><div class="section-title"><h3>${session.role === 'cliente' ? 'Minhas ordens' : 'Ordens de serviço'}</h3>${session.role !== 'cliente' ? '<button class="primary" onclick="openOrder()">＋ Nova ordem</button>' : ''}</div><div style="overflow:auto"><table class="table"><thead><tr><th>Ordem</th><th>Serviço / veículo</th><th>Responsável</th><th>Status</th><th>Progresso</th><th>Ações</th></tr></thead><tbody>${data.orders.map(order => `<tr><td><strong>${order.id}</strong></td><td>${order.service}<br><span class="muted">${order.car}</span></td><td>${order.tech}</td><td><span class="tag">${order.status}</span></td><td><div class="bar"><i style="width:${order.progress}%"></i></div><small class="muted">${order.progress}%</small></td><td><button class="secondary" onclick="partsModal('${order.id}')">Peças</button>${canDelete ? ` <button class="danger" onclick="removeOrder('${order.id}')">Excluir</button>` : ''}</td></tr>`).join('')}</tbody></table></div></div>`;
}

function employeeOrders() {
  return `<div class="task-grid">${data.orders.map(order => `<article class="task-card"><div class="task-head"><div><span class="eyebrow">${order.id}</span><h3>${order.service}</h3></div><span class="tag">${order.status}</span></div><p class="muted">${order.car}</p><div class="task-info"><span>Responsável<br><strong>${order.tech}</strong></span><span>Progresso<br><strong>${order.progress}%</strong></span></div><div class="bar"><i style="width:${order.progress}%"></i></div><div class="task-actions"><button class="secondary" onclick="partsModal('${order.id}')">Peças</button><button class="primary" onclick="setProgress('${order.id}','Em execução',25)">Iniciar</button><button class="secondary" onclick="setProgress('${order.id}','Pausada',${order.progress})">Pausar</button><button class="primary" onclick="setProgress('${order.id}','Concluída',100)">Concluir</button></div></article>`).join('')}</div>`;
}

function simpleTeam() {
  return `<div class="card"><div class="section-title"><h3>Equipe & competências</h3><button class="primary" onclick="openEmployee()">＋ Novo funcionário</button></div>${data.employees.map(employee => `<div class="row"><div><strong>${employee.name}</strong><br><span class="muted">${employee.specialty} · nível ${employee.level}/5</span></div><span class="tag ${employee.status === 'Ausente' ? 'red' : employee.status === 'Ocupado' ? 'warn' : ''}">${employee.status}</span></div>`).join('')}</div>`;
}

function schedule() {
  if (!canViewSchedule()) return '';
  const canManage = canManageSchedule();
  return `<div class="grid cols"><div class="card"><div class="section-title"><h3>Agenda de hoje</h3>${canManage ? '<button class="primary" onclick="openSchedule()">＋ Agendar</button>' : ''}</div>${data.appointments.map(appointment => `<div class="row"><strong>${appointment.time}</strong><span>${appointment.name}<br><small class="muted">${appointment.service} · ${appointment.vehicle || 'Frota'}</small></span>${canManage ? `<button class="danger" onclick="removeAppointment('${appointment.id || appointment.time}')">Remover</button>` : ''}</div>`).join('')}</div><div class="card"><h3>Próximos horários</h3><p class="muted">A oficina tem 4 janelas livres hoje.</p><div class="bar"><i style="width:62%"></i></div><br><span class="muted">${canManage ? 'Somente o patrão pode alocar horários.' : 'Visualização da agenda da oficina.'}</span></div></div>`;
}

function reports() {
  const items = [['Faturamento estimado', 'R$ 48,2k', '↑ 12,4%'], ['Tempo médio', '3h42', '↓ 8,1%'], ['Conclusão no prazo', '86%', '↑ 5,2%']];
  return `<div class="grid stats">${items.map(item => `<div class="card stat"><span class="eyebrow">${item[0]}</span><b>${item[1]}</b><span class="trend">${item[2]}</span></div>`).join('')}</div><br><div class="card"><h3>Volume de serviços</h3>${['Diagnóstico', 'Revisão', 'Freios', 'Suspensão'].map((item, index) => `<div class="row"><span>${item}</span><strong>${[82, 68, 54, 41][index]}%</strong><div style="width:42%"><div class="bar"><i style="width:${[82, 68, 54, 41][index]}%"></i></div></div></div>`).join('')}</div>`;
}

function road() {
  return `<div class="card"><h3>Assistência na estrada</h3><p class="muted">Registre uma solicitação de socorro e a equipe confirmará a disponibilidade de atendimento.</p><label>Localização</label><input placeholder="Endereço ou ponto de referência"><label>Problema percebido</label><textarea rows="4" placeholder="Descreva o que aconteceu"></textarea><br><button class="primary" onclick="toast('Solicitação enviada para análise')">Solicitar assistência</button></div>`;
}
