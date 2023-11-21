import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard'; 

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} /> 
        {/* <Route path="/dummy" element={<Dummy />} /> You guys can copy this format for every new page you build and import like above also make pages within pages subdirectory  */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
