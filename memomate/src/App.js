import React, { useState, useEffect } from 'react';

function App() {
  const [quote, setQuote] = useState('');
  const [author, setAuthor] = useState('');

  async function fetchQuote() {
    try {
      const response = await fetch('https://zenquotes.io/api/random');
      const data = await response.json();
      if (data.length > 0) {
        setQuote(data[0].q);
        setAuthor(data[0].a);
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
        <em>- {author}</em>
      </header>
    </div>
  );
}


export default App;
