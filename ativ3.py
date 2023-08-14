altura_da_parede = int(input("digite a altura da parede:"))
largura = int(input("digite a largura da parede:"))
area_da_parede = altura_da_parede * largura

altura_do_azulejo = int(input("digite a altura do azulejo:"))
largura_do_azulejo = int(input("digite a altura do azulejo:"))
area_do_azulejo = altura_do_azulejo * largura_do_azulejo

quant_azuleijos_necessarios = area_da_parede / area_do_azulejo

print(f"vai precisar de {quant_azuleijos_necessarios} azuleijos")
