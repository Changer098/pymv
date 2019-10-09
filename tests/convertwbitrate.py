import sys
sys.path.insert(1, '../pymv')
from pymv import mv

mov = mv()
mov.Input('filename.mkv') \
.Map(0, 0) \
.Map(0, 1) \
.Map(0, 2) \
.Codec().Video('h264').Audio('ac3', streamIndex=0).Audio('aac', streamIndex=1)
mov.Bitrate().Video('1M').Audio('512k', streamIndex=0).Audio('192k', streamIndex=1)
mov.Output('output.mkv')
print(mov.get_command())