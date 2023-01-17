import random
import time
import threading

def codigo():
    while True:
        numeros = ['1','2','3','4','5','6','7','8','9','0']
        cod = [random.choice(numeros) for i in range (7)]
        code = ''
        for i in cod:
            code += i
        int1 = int(code)
        time.sleep(1)
        return int1
    
t = threading.Thread(target=codigo)
t.start()