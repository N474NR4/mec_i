const escapeText = value => String(value ?? '').replace(/[&<>"']/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character]));

function login() {
  document.body.innerHTML = `<div id="app"><div class="login"><div class="login-box"><section class="hero">${texts.showLoginLogo ? `<span class="logo">${escapeText(texts.appName)}</span>` : ''}<h1>${escapeText(texts.heroTitle)}</h1><p>${escapeText(texts.heroDescription)}</p></section><section class="login-card"><h2>${escapeText(texts.loginTitle)}</h2><p class="muted">${escapeText(texts.loginSubtitle)}</p><label>E-mail</label><input id="email" type="email" placeholder="voce@transportadora.com.br"><label>Senha</label><input id="pass" type="password" placeholder="••••••••"><button class="primary" style="width:100%;justify-content:center;margin-top:20px" onclick="doLogin()">${escapeText(texts.loginButton)}</button><div id="err" class="error"></div><p class="muted">Acesso rápido</p><div class="quick"><button onclick="quick('cliente')">${escapeText(texts.quickTransportadora)}</button><button onclick="quick('funcionario')">${escapeText(texts.quickMecanico)}</button><button onclick="quick('patrao')">${escapeText(texts.quickGestor)}</button></div></section></div></div></div>`;
  applyTheme();
}

function quick(role) {
  $('#email').value = users[role].email;
  $('#pass').value = users[role].pass;
  doLogin();
}

function doLogin() {
  const email = $('#email').value;
  const password = $('#pass').value;
  const role = Object.keys(users).find(key => users[key].email === email && users[key].pass === password);
  if (!role) return $('#err').textContent = 'Credenciais demonstrativas inválidas.';
  session = { ...users[role], role };
  store('mi-session', session);
  current = 'dashboard';
  render();
}

function logout() {
  session = null;
  localStorage.removeItem('mi-session');
  current = 'dashboard';
  login();
}

function openProfile() {
  modal('Configurar meu perfil', `<form onsubmit="event.preventDefault();session.name=this.name.value;session.email=this.email.value;session.phone=this.phone.value;session.pass=this.password.value||session.pass;users[session.role]={...users[session.role],name:session.name,email:session.email,phone:session.phone,pass:session.pass};store('mi-session',session);this.closest('.modal-bg').remove();toast('Perfil atualizado');render()"><label>Nome completo</label><input name="name" value="${escapeText(session.name)}" required><label>E-mail de acesso</label><input name="email" type="email" value="${escapeText(session.email)}" required><label>Telefone</label><input name="phone" value="${escapeText(session.phone || '')}" placeholder="(00) 00000-0000"><label>Nova senha</label><input name="password" type="password" minlength="6" placeholder="Deixe vazio para manter a atual"><br><button class="primary">Salvar perfil</button></form>`);
}
