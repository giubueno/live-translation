import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import EventForm from '../components/EventForm';

function Event() {
  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Start a new live Translation Event
      </Typography>
      <Button variant="contained" color="primary" fullWidth>
        New event
      </Button>
      <EventForm />
    </Container>
  );
}

export default Event;
