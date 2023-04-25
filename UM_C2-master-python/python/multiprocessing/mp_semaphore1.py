"""
    Simulador de playa de estacionamiento
"""

import multiprocessing
import time

# metemos un auto al estacionamiento
def EntraAuto(slots,entra,entraL):
        slots.acquire()
        print("------------------------------------> Entró auto! Slots: %d" % slots.get_value())
        # usar lock para delimitar secciones criticas de variables compartidas
        entraL.acquire()
        entra.value = entra.value+1
        entraL.release()
        print(">>>>> Entrando auto: %d" % (entra.value))

# sacamos un auto del estacionamiento
def SaleAuto(slots,sale,saleL):
        slots.release()
        print("------------------------------------> Salio auto! Slots: %d" % slots.get_value())
        saleL.acquire()
        sale.value = sale.value+1
        saleL.release()
        print("<<<<< Saliendo auto: %d" % (sale.value))


# simulador de autos entrando al estacionamiento
def entrando(slots,entra, entraL):
    while(True):
        time.sleep(1)
        incomingCar = multiprocessing.Process(target=EntraAuto, args=(slots,entra,entraL))
        incomingCar.start()

# simulador de autos saliendo del estacionamiento
def saliendo(slots,sale, saleL):
    while(True):
        time.sleep(3)
        outgoingCar = multiprocessing.Process(target=SaleAuto, args=(slots,sale,saleL))
        outgoingCar.start()


if __name__=="__main__":

    entra = multiprocessing.Value('d', 0)
    sale = multiprocessing.Value('d', 0)

    slots = multiprocessing.Semaphore(10)
    entraL = multiprocessing.Lock()
    saleL = multiprocessing.Lock()
   

    print("Slots iniciales: %d" % slots.get_value())
    entraProc = multiprocessing.Process(target=entrando, args=(slots,entra, entraL))
    saleProc = multiprocessing.Process(target=saliendo, args=(slots,sale, saleL))
    entraProc.start()
    saleProc.start()

