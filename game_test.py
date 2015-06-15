import os
import sys
import select
import time
from fcntl import *
from game_memo import *


rpipe, wpipe = os.pipe()
wpipe = os.fdopen(wpipe, "w")
rpipe = os.fdopen(rpipe, "r")

flags = fcntl(rpipe, F_GETFL)
fcntl(rpipe, F_SETFL, flags | os.O_NONBLOCK)

pid = os.fork()

if pid == 0:
    rpipe.close()
    wpipe.write("hello")
    wpipe.flush()
    
    root = Tk()
    root.title("Hanabi Memo")
    app = GUIDemo(master=root, pipe=wpipe, player_num=4, ID=0)
    app.mainloop()
    
    print("Child finish")

else:
    print("parent")
    wpipe.close()
    rqueue = [rpipe]
    while 1:
        rlist, wlist, elist = select.select(rqueue, [], [], 1)
        if len(rlist) != 0:
            str = rpipe.read(4096)
            if len(str) != 0:
                print("Parent receive: {" + str + "}")
            
