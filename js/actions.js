function openOrder() {
  if (session.role === 'cliente') return toast('Clientes não podem criar ordens diretamente');
  modal('Nova ordem de serviço', `<form onsubmit="event.preventDefault();data.orders.unshift({id:'OS-'+(1049+data.orders.length),car:this.car.value,service:this.service.value,status:'Aguardando',tech:'Não atribuído',progress:0});saveData();this.closest('.modal-bg').remove();toast('Ordem criada com sucesso');render()"><div class="form-grid"><div><label>Caminhão / placa Mercosul</label><input name="car" required placeholder="Ex.: DAF XF • BRA2E19"></div><div><label>Serviço pesado</label><input name="service" required placeholder="Ex.: Revisão de diferencial"></div></div><label>Descrição do problema</label><textarea required rows="3" placeholder="Ruído, falha, quilometragem, carga..."></textarea><br><button class="primary">Criar ordem</button></form>`);
}

function openAssign() {
  const order = data.orders.find(item => item.id === 'OS-1047') || data.orders[0];
  modal('Escolher funcionário', `<p class="muted">${order.id} · ${order.service}</p><form onsubmit="event.preventDefault();order.tech=this.employee.value;order.status='Aguardando';saveData();this.closest('.modal-bg').remove();toast('Funcionário escolhido e alocação registrada');render()"><label>Recomendação por especialidade, nível e disponibilidade</label>${data.employees.map((employee, index) => `<label class="row"><span><input type="radio" name="employee" value="${employee.name}" ${index === 0 ? 'checked' : ''}> <strong>${employee.name}</strong><br><small class="muted">${employee.specialty} · nível ${employee.level}/5 · ${employee.status}</small></span><span class="tag">${index === 0 ? '98' : '81'}% match</span></label>`).join('')}<button class="primary">Confirmar funcionário</button></form>`);
}

function openSchedule() {
  if (!canManageSchedule()) return toast('Somente o patrão pode alocar horários');
  modal('Novo agendamento', `<form onsubmit="event.preventDefault();data.appointments.push({id:Date.now(),time:this.time.value,name:this.name.value,service:this.service.value,vehicle:this.vehicle.value});saveData();this.closest('.modal-bg').remove();toast('Agendamento criado');render()"><div class="form-grid"><div><label>Horário</label><input name="time" type="time" required></div><div><label>Transportadora / cliente</label><input name="name" required placeholder="Nome ou empresa"></div></div><label>Caminhão / placa</label><input name="vehicle" required placeholder="Scania R 450 - BRA2E19"><label>Serviço</label><input name="service" required placeholder="Revisão preventiva"><br><button class="primary">Salvar agendamento</button></form>`);
}

function removeAppointment(id) {
  if (!canManageSchedule()) return toast('Somente o patrão pode remover agendamentos');
  data.appointments = data.appointments.filter(item => String(item.id || item.time) !== String(id));
  saveData();
  toast('Agendamento removido');
  render();
}

function removeOrder(id) {
  if (session.role !== 'patrao') return toast('Somente o patrão pode excluir ordens');
  if (!confirm('Remover esta ordem de serviço?')) return;
  data.orders = data.orders.filter(order => order.id !== id);
  delete data.parts[id];
  saveData();
  toast('Ordem removida');
  render();
}

function partsModal(id) {
  const order = data.orders.find(item => item.id === id);
  const parts = data.parts[id] || [];
  const canEdit = session.role === 'patrao';
  modal(`Peças vendidas · ${order.car}`, `<div class="list">${parts.length ? parts.map((part, index) => `<div class="row"><span><strong>${part.name}</strong><br><small class="muted">${part.qty} un. · R$ ${(part.price * part.qty).toFixed(2).replace('.', ',')}</small></span>${canEdit ? `<button class="danger" onclick="removePart('${id}',${index})">Remover</button>` : ''}</div>`).join('') : '<p class="muted">Nenhuma peça registrada nesta ordem.</p>'}</div><br>${canEdit ? `<button class="primary" onclick="addPart('${id}')">＋ Adicionar peça</button>` : '<p class="muted">Somente o patrão pode alterar peças desta ordem.</p>'}`);
}

function addPart(id) {
  if (session.role !== 'patrao') return toast('Somente o patrão pode alterar peças');
  modal('Adicionar peça', `<form onsubmit="event.preventDefault();data.parts[id]=data.parts[id]||[];data.parts[id].push({name:this.name.value,qty:Number(this.qty.value),price:Number(this.price.value)});saveData();this.closest('.modal-bg').remove();partsModal('${id}')"><label>Nome da peça</label><input name="name" required placeholder="Filtro de ar, pastilha, sensor..."><div class="form-grid"><div><label>Quantidade</label><input name="qty" type="number" min="1" value="1" required></div><div><label>Preço unitário (R$)</label><input name="price" type="number" step="0.01" min="0" required></div></div><br><button class="primary">Adicionar peça</button></form>`);
}

function removePart(id, index) {
  if (session.role !== 'patrao') return toast('Somente o patrão pode alterar peças');
  data.parts[id].splice(index, 1);
  saveData();
  partsModal(id);
}

function openEmployee() {
  if (session.role !== 'patrao') return toast('Somente o patrão pode cadastrar funcionários');
  modal('Novo funcionário', `<form onsubmit="event.preventDefault();data.employees.push({name:this.name.value,email:this.email.value,password:this.password.value,specialty:this.specialty.value,level:this.level.value,status:this.status.value});saveData();this.closest('.modal-bg').remove();toast('Funcionário cadastrado');render()"><label>Nome completo</label><input name="name" required placeholder="Nome do mecânico"><div class="form-grid"><div><label>E-mail de acesso</label><input name="email" type="email" required placeholder="mecanico@oficina.com.br"></div><div><label>Senha inicial</label><input name="password" type="password" minlength="6" required placeholder="Mínimo de 6 caracteres"></div></div><label>Especialidade</label><input name="specialty" required placeholder="Ex.: Motores diesel"><div class="form-grid"><div><label>Nível (1 a 5)</label><select name="level"><option>5</option><option>4</option><option>3</option><option>2</option><option>1</option></select></div><div><label>Status</label><select name="status"><option>Livre</option><option>Ocupado</option><option>Ausente</option></select></div></div><br><button class="primary">Cadastrar funcionário</button></form>`);
}

function setProgress(id, status, progress) {
  if (session.role !== 'funcionario') return toast('Somente o funcionário pode atualizar o progresso');
  const order = data.orders.find(item => item.id === id);
  if (!order) return;
  order.status = status;
  order.progress = progress;
  saveData();
  toast(`Progresso atualizado para ${progress}%`);
  render();
}

function startTask() { setProgress(data.orders[0].id, 'Em execução', 72); }
