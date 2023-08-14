tempo=int(input("qual o tempo em segundos: "))
distancia_percorrido = 2
velocidade_inicial = 3
aceleração = 10
espaço_percorrido = distancia_percorrido + velocidade_inicial * tempo + 1/2 * aceleração * tempo **2

print(f"o espaço percorrido é {espaço_percorrido}")