import { useNavigate } from 'react-router-dom';

export default function Landing() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
      <div className="max-w-md text-center bg-white p-8 rounded shadow">
        <h1 className="text-4xl font-bold mb-4">Bem-vindo ao Sistema de Gestão Financeira</h1>
        <p className="mb-6">Controle suas finanças, assine planos e veja relatórios em um só lugar.</p>
        <div className="flex justify-center gap-4">
          <button
            onClick={() => navigate('/login')}
            className="px-6 py-2 bg-green-500 text-white rounded"
          >
            Login
          </button>
          <button
            onClick={() => navigate('/register')}
            className="px-6 py-2 bg-blue-500 text-white rounded"
          >
            Registrar
          </button>
        </div>
      </div>
    </div>
  );
}
