import sys
import time as _time

class loadanim:
    
    def __init__(self, text1, text2, end="ok", time=1, wait=0.04, val=["—", "\\", "|", "/"]):
        self._play(text1, time, wait, val)

        print(str(text2))


    def _remLastLine(self):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')


    def _play(self, text, time, wait, val):
        i = 0
        
        while True:
            for ch in val:

                print(str(text).replace("%c", ch))
            
                i += wait
                _time.sleep(wait)
                
                self._remLastLine()
                
                if i >= time:
                    return
