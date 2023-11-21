import React, { useState, useEffect } from 'react';

function Dashboard() {
    const [quote, setQuote] = useState('');
    const [author, setAuthor] = useState('');
  
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
  
    useEffect(() => {
      fetchQuote();
    }, []);
  
    return (
      <div className="App">
        <header className="App-header">
          <h1>Inspirational Quote</h1>
          <p>{quote}</p>
          <em>- {author ? author : "Unknown"}</em>
        </header>
      </div>
    );
}

export default Dashboard;
