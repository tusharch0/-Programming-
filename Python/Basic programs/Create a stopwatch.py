import time
print ("Press ENTER to start the stopwatch")
print ("and, press CTRL + to stop the stopwatch")

while True:
    try:
        input ()
        start_time = time.time()
        print("Stopwatch started...")

    except KeyboardInterrupt:
        print("Stopwatch stopped...")
        end_time = time.time()
        print("The total time: ",round(end_time-start_time,2),"second")
        break