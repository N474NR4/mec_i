function applyTheme() {
  const [brand, accent, background] = themes[theme.name || 'aurora'];
  document.body.className = theme.mode === 'light' ? 'light' : theme.name === 'oled' ? 'oled' : '';
  document.documentElement.style.setProperty('--brand', brand);
  document.documentElement.style.setProperty('--accent', accent);
  document.documentElement.style.setProperty('--bg', background);
  document.title = texts.siteTitle;
}

function toggleTheme() {
  theme.mode = theme.mode === 'light' ? 'dark' : 'light';
  store('mi-theme', theme);
  render();
}

function setTheme(name) {
  theme.name = name;
  if (name === 'oled') theme.mode = 'dark';
  store('mi-theme', theme);
  applyTheme();
  toast(`Tema ${name} aplicado`);
  document.querySelector('.modal-bg')?.remove();
  render();
}

function toast(message) {
  const element = document.createElement('div');
  element.className = 'toast';
  element.textContent = message;
  document.body.append(element);
  setTimeout(() => element.remove(), 2600);
}

function modal(title, body) {
  const element = document.createElement('div');
  element.className = 'modal-bg';
  element.innerHTML = `<div class="modal"><div class="modal-head"><h3>${title}</h3><button class="ghost" onclick="this.closest('.modal-bg').remove()">✕</button></div>${body}</div>`;
  document.body.append(element);
}

function openSettings() {
  modal('Personalização da oficina', `<p class="muted">${Object.keys(themes).length} identidades visuais salvas neste navegador.</p><label>Escolha sua identidade</label><div class="theme-grid">${Object.keys(themes).map(name => `<button class="theme-choice" onclick="setTheme('${name}')"><i style="background:${themes[name][0]}"></i>${name}</button>`).join('')}</div><br><button class="secondary" onclick="toggleTheme();this.closest('.modal-bg').remove()">Alternar claro / escuro</button>`);
}
