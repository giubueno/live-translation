import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Event from './pages/Event';
import Home from './pages/Home';
import Translation from './pages/Translation';
import NotFound from './pages/NotFound';

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/events" element={<Event />} />
          <Route path="/translations/:language" element={<Translation />} />
          <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
