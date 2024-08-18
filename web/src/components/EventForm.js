import React from 'react';
import { Paper, TextField, FormControl, Button } from '@mui/material';
import LanguageSelection from './LanguageSelection';
import SourceSelection from './SourceSelection';

function EventForm() {
  return (
    <Paper style={{ padding: 16, marginTop: 16 }}>
      <FormControl fullWidth margin="normal">
        <TextField label="Name your event" variant="outlined" />
      </FormControl>

        <SourceSelection />
        <LanguageSelection />

      <Button variant="contained" color="primary" fullWidth>
        Try now
      </Button>
    </Paper>
  );
}

export default EventForm;
