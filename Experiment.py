from psychopy import visual, core, event
import pandas as pd
from stimuli import Stimuli
from utils import save_data

class ImaginationExperiment:
    def __init__(self):
        self.window = visual.Window([800, 600], color="black")
        self.stimuli = Stimuli(self.window)
        self.responses = []
    
    def run_trial(self, trial_number):
        # Example trial logic (customize as needed)
        self.stimuli.show_text(f"Trial {trial_number}", duration=2.0)
        self.stimuli.show_fixation(duration=1.0)
        self.stimuli.show_image('images/sample_image.png', duration=2.0)
        response = event.waitKeys(keyList=['1', '2', '3', '4'])
        self.responses.append((trial_number, response))

    def run(self):
        num_trials = 5
        for i in range(num_trials):
            self.run_trial(i + 1)
        
        save_data(self.responses)
        self.window.close()
        core.quit()
