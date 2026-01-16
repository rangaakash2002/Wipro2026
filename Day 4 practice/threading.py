import threading

def task(name):
    print(f"{name} is running")

t2 = threading.Thread(target=task, args=("thread2",))
t2.start()
t2.join()

print("main thread is done")
