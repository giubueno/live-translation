import React from 'react';
import { FormControl, FormLabel, Checkbox, FormGroup, FormControlLabel } from '@mui/material';

function languageSelection() {
    return (
        <FormControl component="fieldset" margin="normal">
            <FormLabel component="legend">Select the languages:</FormLabel>
            <FormGroup>
            <FormControlLabel control={<Checkbox />} label="German" />
            <FormControlLabel control={<Checkbox />} label="Spanish" />
            <FormControlLabel control={<Checkbox defaultChecked />} label="Turkish" />
            </FormGroup>
        </FormControl>
    );
}

export default languageSelection;