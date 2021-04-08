import threading

transaction = 0
balance = 0

def depositor(lock):
    global transaction
    global balance
    lock.acquire()
    while transaction < 5000:
        transaction = transaction +1
        balance = balance + 1
    lock.release()

lock = threading.Lock()
deposit1 = threading.Thread(target=depositor, args=(lock,))
deposit2 = threading.Thread(target=depositor, args=(lock,))
deposit3 = threading.Thread(target=depositor, args=(lock,))
deposit4 = threading.Thread(target=depositor, args=(lock,))
deposit5 = threading.Thread(target=depositor, args=(lock,))

deposit1.start()
deposit2.start()
deposit3.start()
deposit4.start()
deposit5.start()

deposit1.join()
deposit2.join()
deposit3.join()
deposit4.join()
deposit5.join()
        
print(transaction)
print(balance)