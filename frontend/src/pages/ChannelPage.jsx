import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { channelAPI, messageAPI } from '../services/api';
import MessageList from '../components/MessageList';
import MessageForm from '../components/MessageForm';

export default function ChannelPage() {
  const { channelId } = useParams();
  const [channel, setChannel] = useState(null);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const channelRes = await channelAPI.retrieve(channelId);
        setChannel(channelRes.data);

        const messagesRes = await channelAPI.messages(channelId);
        setMessages(messagesRes.data);
      } catch (err) {
        setError('Failed to load channel');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [channelId]);

  const handleNewMessage = async (content) => {
    try {
      const response = await messageAPI.create({
        channel: channelId,
        content,
      });
      setMessages([...messages, response.data]);
    } catch (err) {
      setError('Failed to send message');
    }
  };

  if (loading) return <div className="text-center py-8">Loading...</div>;
  if (error) return <div className="text-red-500 text-center py-8">{error}</div>;

  return (
    <div className="flex flex-col h-screen">
      <div className="bg-gray-800 border-b border-gray-700 px-6 py-4">
        <h1 className="text-xl font-bold">#{channel?.name}</h1>
        {channel?.topic && <p className="text-gray-400 text-sm">{channel.topic}</p>}
      </div>
      <MessageList messages={messages} />
      <MessageForm onSubmit={handleNewMessage} />
    </div>
  );
}
