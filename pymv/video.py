from pymv.ffcommand import ffcommand
from pymv.codec import codec

class Video(ffcommand):
    codec_obj = None

    def __init__(self):
        code_obj = codec()

    def Codec(self, codec_info):
        return self.codec_obj.Codec(codec_info)