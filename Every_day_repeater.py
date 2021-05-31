import time

zero = float(0)
while zero == 0:
    start_time = time.time()
    
###########################################
    print("Your code here")
###########################################

    WorkSpeed = time.time() - start_time
    DaySec = 86400
    Timer = DaySec-WorkSpeed
    time.sleep(Timer)
