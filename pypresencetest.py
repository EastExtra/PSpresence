import time 
from pypresence import Presence 

CLIENT_ID = '1542244771790323823'

rpc = Presence(CLIENT_ID)
rpc.connect() 

rpc.update(
    details="Testing Stuff",
    state ="Getting Rich Presence working",
    start = time.time(),
)
print("Presence set")

while True: 
    time.sleep(15) 