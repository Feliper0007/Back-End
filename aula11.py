km__percorridos = float(input("Quantos Km foram percorridos? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
preco_total = (dias_alugados * 60) + (km__percorridos * 0.15)
print(f"O total a pagar é R$ {preco_total:.2f}")
