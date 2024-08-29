import React from 'react';
import { Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';

function Translation() {
  const { language } = useParams();

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Live Translation for {language}
      </Typography>
    </Container>
  );
}

export default Translation;
