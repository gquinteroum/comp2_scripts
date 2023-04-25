import threading
import time
 
# Set the resource to False initially
shared_resource = False
 # A lock for the shared resource
#lock = threading.Lock()
 
def perform_computation():
    global shared_resource    
    # Thread A will call this function and manipulate the resource
    print(f'Thread {threading.current_thread().name} - performing some computation....')
    time.sleep(5)
    shared_resource = True
    print(f'Thread {threading.current_thread().name} - set shared_resource to True!')
    print(f'Thread {threading.current_thread().name} - Finished!')
#    time.sleep(1)
 
def monitor_resource():
    global shared_resource    
    # Thread B will monitor the shared resource
#    print(f'Thread {threading.current_thread().name} - monitoring....')
    while shared_resource == False:
        print("Hilo %s esperando..." % threading.current_thread().name)
        time.sleep(1)
    print(f'Thread {threading.current_thread().name} - Detected shared_resource = True')
    time.sleep(1)
    print(f'Thread {threading.current_thread().name} - Finished!')
 
 
if __name__ == '__main__':
    a = threading.Thread(target=perform_computation, name='A')
    b = threading.Thread(target=monitor_resource, name='B', daemon=True)
 
    # Now start both threads
    a.start()
    b.start()

    # espera a los hilos no daemon
    #a.join()
    b.join()
    print("Finalizando el programa principal")
    # si usan thread daemon usen join()!!

