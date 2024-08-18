import React from 'react';
import { FormControl, FormLabel, Checkbox, FormGroup, FormControlLabel } from '@mui/material';

function SourceSelection() {
    return (
        <FormControl component="fieldset" margin="normal">
            <FormLabel component="legend">Select an available source:</FormLabel>
            <FormGroup>
            <FormControlLabel control={<Checkbox />} label="City of Light" />
            <FormControlLabel control={<Checkbox />} label="Saddleback" />
            <FormControlLabel control={<Checkbox defaultChecked />} label="Alexanderplatz" />
            </FormGroup>
        </FormControl>
    );
}

export default SourceSelection;