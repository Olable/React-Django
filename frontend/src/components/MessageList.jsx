import { useAuth } from '../hooks/useAuth';

export default function MessageList({ messages }) {
  const { user } = useAuth();

  return (
    <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
      {messages.length === 0 ? (
        <div className="text-center text-gray-400 py-8">No messages yet. Start the conversation!</div>
      ) : (
        messages.map((message) => (
          <div key={message.id} className="bg-gray-700 rounded p-3">
            <div className="flex justify-between items-start">
              <div>
                <span className="font-bold text-blue-400">{message.author.username}</span>
                <span className="text-gray-400 text-xs ml-2">
                  {new Date(message.created_at).toLocaleTimeString()}
                </span>
              </div>
            </div>
            <p className="mt-1 text-gray-100">{message.content}</p>
          </div>
        ))
      )}
    </div>
  );
}
