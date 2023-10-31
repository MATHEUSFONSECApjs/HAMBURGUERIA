from os import system

system('cls')

nota_fiscal = []
total_value = 0
order_closed = False

while not order_closed:
    menu = int(input('''--------CARDAPIO--------
[1] TOP BURGUER........: R$ 14,90
[2] BIG BURGUER ESPECIAL ........: R$ 16,90
[3] BIG CLASSIC........: R$ 17,90
[4] BIG BURGUER DUBLE........: R$ 19,90
[5] X-BURGUER ESPECIAL........: R$ 22,90
[6] X-ESPECIAL DUBLE........: R$ 29,90
[7] PROXIMO>>> (Bebidas)
[8] ENCERRAR PEDIDO\n'''))

    if menu == 1:
        nota_fiscal.append(("TOP BURGUER", 1, 14.90))
    elif menu == 2:
        nota_fiscal.append(("BIG BURGUER ESPECIAL", 1, 16.90))
    elif menu == 3:
        nota_fiscal.append(("BIG CLASSIC", 1, 17.90))
    elif menu == 4:
        nota_fiscal.append(("BIG BURGUER DUBLE", 1, 19.90))
    elif menu == 5:
        nota_fiscal.append(("X-BURGUER ESPECIAL", 1, 22.90))
    elif menu == 6:
        nota_fiscal.append(("X-ESPECIAL DUBLE", 1, 29.90))
    elif menu == 7:
        while True:
            menu = int(input('''-------- BEBIDA --------
[1] FANTA LATA......: R$ 4.00
[2] COCA LATA......: R$ 4.00
[3] SODA LATA......: R$ 4.00
[4] GUARANÁ LATA......: R$ 4.00
[5] PROXIMO>>> (Porção Adicional)
[6] ENCERRAR PEDIDO\n'''))

            if menu == 1:
                nota_fiscal.append(("FANTA LATA", 1, 4.00))
            elif menu == 2:
                nota_fiscal.append(("COCA LATA", 1, 4.00))
            elif menu == 3:
                nota_fiscal.append(("SODA LATA", 1, 4.00))
            elif menu == 4:
                nota_fiscal.append(("GUARANÁ LATA", 1, 4.00))
            elif menu == 5:
                while True:
                    menu = int(input('''-------- PORÇÃO ADICIONAL --------
[1] BATATA FRITA......: R$ 8.00
[2] ANEIS DE CEBOLA FRITA......: R$ 12.00
[3] NUGGETS......: R$ 6.00
[4] ENCERRAR PEDIDO\n'''))

                    if menu == 1:
                        nota_fiscal.append(("BATATA FRITA", 1, 8.00))
                    elif menu == 2:
                        nota_fiscal.append(("ANEIS DE CEBOLA FRITA", 1, 12.00))
                    elif menu == 3:
                        nota_fiscal.append(("NUGGETS", 1, 6.00))
                    elif menu == 4:
                        order_closed = True
                        break
            elif menu == 6:
                order_closed = True
                break
    elif menu == 8:
        order_closed = True

for item in nota_fiscal:
    total_value += item[2]

print("\n--- NOTA FISCAL ---")
for item in nota_fiscal:
    print(f"{item[0]} x{item[1]}: R$ {item[1] * item[2]:.2f}")

print(f"Total: R$ {total_value:.2f}")

