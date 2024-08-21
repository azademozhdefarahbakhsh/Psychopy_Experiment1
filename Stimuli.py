from psychopy import visual, core

class Stimuli:
    def __init__(self, window):
        self.window = window

    def show_text(self, text, duration=2.0):
        text_stim = visual.TextStim(win=self.window, text=text, height=0.1)
        text_stim.draw()
        self.window.flip()
        core.wait(duration)

    def show_image(self, image_path, duration=2.0):
        image_stim = visual.ImageStim(win=self.window, image=image_path, size=(500, 500))
        image_stim.draw()
        self.window.flip()
        core.wait(duration)

    def show_fixation(self, duration=1.0):
        fixation = visual.TextStim(win=self.window, text='+', height=0.1)
        fixation.draw()
        self.window.flip()
        core.wait(duration)
