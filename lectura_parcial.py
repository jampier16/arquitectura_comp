import time 

if __name__=='__main__':

    codigo=""

    inicio=time.perf_counter() 
    with open("codigo.txt", "r", encoding="utf-8") as f:
        
        for _ in range(200):
            codigo += f.readline()
    
    fin= time.perf_counter()
    print(codigo)
    print(f"tiempo de ejecucion:{fin-inicio} segundos")
