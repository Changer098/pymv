from pymv.commandbuilder import commandbuilder
from pymv.runner import runner
from pymv.prober import prober

class mv(commandbuilder):
    prober = None
    Input = None
    Output = None
    Video = None

    def __init__(self):
        super().__init__()
        self.prober = prober(self.get_ffprobe())
        self.Input = self.inputobj
        self.Output = self.outputobj
        self.Video = self.videoobj

    def run(self):
        run = runner(self.get_arguments(), self.get_ffmpeg())
        run.run()