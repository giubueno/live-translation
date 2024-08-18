import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import EventForm from './components/EventForm';

function App() {
  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Live Translations
      </Typography>
      <Button variant="contained" color="primary" fullWidth>
        New event
      </Button>
      <EventForm />
    </Container>
  );
}

export default App;
