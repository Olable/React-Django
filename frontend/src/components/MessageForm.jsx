import { useState } from 'react';
import { useAuth } from '../hooks/useAuth';

export default function MessageForm({ onSubmit }) {
  const { user } = useAuth();
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!content.trim()) return;

    setLoading(true);
    try {
      await onSubmit(content);
      setContent('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-gray-800 border-t border-gray-700 px-6 py-4">
      <div className="flex gap-2">
        <input
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Type your message..."
          className="input-field flex-1"
          disabled={loading}
        />
        <button type="submit" disabled={loading} className="btn btn-primary">
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </form>
  );
}
