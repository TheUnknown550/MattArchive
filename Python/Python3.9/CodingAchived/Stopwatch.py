import time
x=input("Start stopwatch: ")
Start=time.time()
x=input("Stop stopwatch: ")
End=time.time()
Time=End-Start
print('Total time passed: ',Time)