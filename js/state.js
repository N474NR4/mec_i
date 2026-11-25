let session = store('mi-session');
let theme = store('mi-theme') || {};
let current = 'dashboard';

const canViewSchedule = () => session && ['patrao', 'funcionario'].includes(session.role);
const canManageSchedule = () => session?.role === 'patrao';
