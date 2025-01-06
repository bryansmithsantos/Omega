import React, { useState } from 'react';
import axios from 'axios';

const App: React.FC = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Array<{text: string, isUser: boolean}>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!input.trim()) return;

    // Adiciona mensagem do usuário
    setMessages(prev => [...prev, { text: input, isUser: true }]);
    
    try {
      const response = await axios.post('http://localhost:5000/predict', { input });
      setMessages(prev => [...prev, { text: response.data.message, isUser: false }]);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
    }

    setInput('');
  };

  return (
    <div className="container mx-auto p-4 max-w-4xl">
      <h1 className="text-3xl font-bold mb-8 text-center">Omega Assistant</h1>
      
      <div className="bg-white rounded-lg shadow-lg p-6 mb-4 h-[500px] overflow-y-auto">
        {messages.map((msg, idx) => (
          <div key={idx} className={`mb-4 ${msg.isUser ? 'text-right' : 'text-left'}`}>
            <div className={`inline-block p-3 rounded-lg ${
              msg.isUser ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}>
              {msg.text}
            </div>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-2 border rounded-lg"
          placeholder="Digite sua mensagem..."
        />
        <button 
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
        >
          Enviar
        </button>
      </form>
    </div>
  );
};

export default App; 