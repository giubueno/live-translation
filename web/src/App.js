import React, {useState, useEffect} from 'react';
import { Grid, FormControl, FormLabel, Radio, RadioGroup, FormControlLabel } from '@mui/material';
import Typography from '@mui/material/Typography';

// API URL - Change this to your API URL
const URL = 'https://api.aboa.today';

function App() {
  const [language, setLanguage] = useState('english');
  const [text, setText] = useState();

  const handleRadioChange = (event) => {
    setLanguage(event.target.value);
  };
  
  // Fetch data from API every 5 seconds
// Fetch data from API every 5 seconds
useEffect(() => {
  const fetchData = () => {
    fetch(`${URL}/translations/${language}`)
      .then(response => response.json())
      .then(data => setText(data));
  };

  fetchData(); // Initial fetch

  const intervalId = setInterval(fetchData, 5000); // Fetch every 5 seconds

  return () => clearInterval(intervalId); // Cleanup interval on unmount
}, [language]);

  return (
    <Grid container spacing={0.5}>
      <Grid columns={{ xs: 4, sm: 4, md: 4, lg: 4 }}>
        <FormControl>
          <FormLabel id="demo-radio-buttons-group-label">Language:</FormLabel>
          <RadioGroup 
            aria-labelledby="demo-radio-buttons-group-label" 
            defaultValue="english" 
            name="radio-buttons-group"
            onChange={handleRadioChange}
          >
            <FormControlLabel value="english" control={<Radio />} label="English" />
            <FormControlLabel value="turkish" control={<Radio />} label="Turkish" />
            <FormControlLabel value="arabic" control={<Radio />} label="Arabic" />
          </RadioGroup>
        </FormControl>
      </Grid>
      <Grid columns={{ xs: 8, sm: 8, md: 8, lg: 8 }}>
        <Typography variant="body1" gutterBottom>{text}</Typography>
      </Grid>
    </Grid>
  );
}

export default App;
