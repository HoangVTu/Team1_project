import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'; 
import { faPencilAlt } from '@fortawesome/free-solid-svg-icons';

function Dashboard() {
    const [quote, setQuote] = useState('');
    const [author, setAuthor] = useState('');
    const [notes, setNotes] = useState([]);
    const navigate = useNavigate();
  
    async function fetchQuote() {
      try {
        const response = await fetch('https://type.fit/api/quotes');
        const quotes = await response.json();
        if (quotes.length > 0) {
          const randomIndex = Math.floor(Math.random() * quotes.length);
          const randomQuote = quotes[randomIndex];
          setQuote(randomQuote.text);
          setAuthor(randomQuote.author);
        }
      } catch (error) {
        console.error("Error fetching quote:", error);
      }
    }
  
    async function fetchNotes() {
      try {
          console.log("Fetching notes from URL:", '/api/notes');
          const response = await fetch('/api/notes');
          const data = await response.json();
          setNotes(data);
          console.log("hello:", data);
      } catch (error) {
          console.error("Error fetching notes:", error);
      }
  }

  useEffect(() => {
    fetchQuote();
    fetchNotes();
}, []);


    const navigateToNewPage = () => {
      navigate('/notes'); 
    };
  
    return (
      <div className="App flex flex-col items-center justify-center">
        <div className="w-2/3 bg-gray-200 p-4 border-black border rounded-lg my-2">
          <h1 className="text-center font-bold">Inspirational Quote</h1>
          <p className="text-center">{quote}</p>
          <em className="text-center block">{author ? author : "Unknown"}</em>
        </div>
        <div className="w-2/3 bg-gray-200 p-4 border-black border rounded-lg my-2">
          <button 
            onClick={navigateToNewPage} 
            className="mr-auto p-2 border-black border rounded-lg">
            <FontAwesomeIcon icon={faPencilAlt} /> 
          </button>
        </div>
        <div className="w-2/3 bg-gray-200 p-4 border-black border rounded-lg my-2">
                <h2 className="text-center font-bold">Your Notes</h2>
                {notes.map(note => (
                    <div key={note.id}> 
                        <h3>{note.title}</h3>
                        <p>{note.content}</p>
                    </div>
                ))}
            </div>
      </div>
    );
}

export default Dashboard;
