import { Outlet, useNavigate } from 'react-router-dom';

export default function Layout() {
  const navigate = useNavigate();
  const logout = () => {
    localStorage.removeItem('token');
    navigate('/login', { replace: true });
  };

  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-gray-800 text-white p-6">
        <h2 className="text-2xl font-bold mb-8">Gestão Financeira</h2>
        <nav className="flex flex-col gap-4">
          <button onClick={() => navigate('/dashboard')} className="text-left">Dashboard</button>
          <button onClick={() => navigate('/login')} className="text-left">Login</button>
          <button onClick={() => navigate('/register')} className="text-left">Registrar</button>
          <button onClick={logout} className="mt-8 text-red-400 text-left">Sair</button>
        </nav>
      </aside>
      <main className="flex-1 bg-gray-100 p-8">
        <Outlet />
      </main>
    </div>
  );
}
