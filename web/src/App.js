import React, {useState, useEffect} from 'react';
import { FormControl, Select, MenuItem, InputLabel, Box } from '@mui/material';
import Grid from '@mui/material/Grid2';
import Typography from '@mui/material/Typography';
import logo from "./images/logo.png";
import background from "./images/background.png";

// API URL - Change this to your API URL
const URL = 'http://192.168.0.148:8000';

function App() {
  const [language, setLanguage] = useState('german');
  const [translation, setTranslation] = useState();

  const handleChange = (event) => {
    setLanguage(event.target.value);
  }; 
  
  // Fetch data from API every 5 seconds
// Fetch data from API every 5 seconds
useEffect(() => {
  const fetchData = () => {
    fetch(`${URL}/translations/${language}`)
      .then(response => response.json())
      .then(data => setTranslation(data))
      .catch(error => console.error('Error:', error));
  };

  fetchData(); // Initial fetch

  const intervalId = setInterval(fetchData, 1000); // Fetch every 5 seconds

  return () => clearInterval(intervalId); // Cleanup interval on unmount
}, [language]);

  return (
    <Grid container spacing={4}>
      <Grid id="top" size={12} style={{ backgroundImage: `url(${background})` }}>
        <img id="logo" src={logo} alt="Logo"/>
        <FormControl id="language" sx={{ width: 200 }}>
          <InputLabel id="demo-simple-select-label">Select a language</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={language}
            label="Select a language"
            onChange={handleChange}
          >
            {translation && translation.languages.map((lang) => <MenuItem value={lang}>{lang}</MenuItem>)}
          </Select>
        </FormControl>
      </Grid>
      <Grid id="translations" size={12}>
        {translation && translation.messages.map((text) => <Typography variant="body1">{text}</Typography>) }
        <Typography variant="body1"></Typography>
      </Grid>
    </Grid>
  );
}

export default App;
