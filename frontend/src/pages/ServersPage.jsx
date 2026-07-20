import { useState, useEffect } from 'react';
import { serverAPI } from '../services/api';
import ServerList from '../components/ServerList';
import ServerForm from '../components/ServerForm';

export default function ServersPage() {
  const [servers, setServers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    fetchServers();
  }, []);

  const fetchServers = async () => {
    try {
      const response = await serverAPI.list();
      setServers(response.data);
    } catch (err) {
      setError('Failed to load servers');
    } finally {
      setLoading(false);
    }
  };

  const handleServerCreated = () => {
    setShowForm(false);
    fetchServers();
  };

  if (loading) return <div className="text-center py-8">Loading...</div>;

  return (
    <div className="container py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Servers</h1>
        <button onClick={() => setShowForm(true)} className="btn btn-primary">
          + New Server
        </button>
      </div>
      {error && <div className="bg-red-100 text-red-700 p-3 rounded mb-4">{error}</div>}
      {showForm && <ServerForm onClose={() => setShowForm(false)} onCreated={handleServerCreated} />}
      <ServerList servers={servers} />
    </div>
  );
}
