import React, { useEffect, useState } from 'react';
import { Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';

const URL = "http://192.168.0.148:8000/translations";

function Translation() {
  const { language } = useParams();
  const url = `${URL}/${language}`;

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, [url]);

  return (
    <Container maxWidth="sm">
      {loading && <Typography variant="h4" align="center" gutterBottom>Loading...</Typography>}
      {error && <Typography variant="h4" align="center" gutterBottom>Error: {error.message}</Typography>}
      {!loading && !error && <Typography variant="h4" align="center" gutterBottom>{data}</Typography>}
    </Container>
  );
}

export default Translation;
