export default function ServerList({ servers }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {servers.map((server) => (
        <div key={server.id} className="card cursor-pointer hover:bg-gray-700">
          <h3 className="text-lg font-bold mb-2">{server.name}</h3>
          <p className="text-gray-400 text-sm mb-3">{server.description}</p>
          <div className="flex justify-between items-center">
            <span className="text-xs text-gray-500">Owner: {server.owner.username}</span>
            <span className="text-xs bg-blue-600 text-white px-2 py-1 rounded">
              {server.channels?.length || 0} channels
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}
