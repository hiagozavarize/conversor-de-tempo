# Um minuto tem 60 segundos.
# Uma hora tem 3600 segundos.
# um dia tem 24 horas.
continuar = 1;

while continuar == 1:
    print("========== Conversor de tempo ==========")
    
    convert = int(input(" Digite (1) para converter minutos em segundo\n Digite (2) para converter segundos em minuto\n Digite (3) para converter horas em minuto\n Digite (4) para converter horas em segundos\n Digite (5) para converter dia em horas\n========================================\n--> "));
    # se digitar 1, converte para minutos.
    if convert == 1:
        # recebe um valor em minutos.
        qtd_minuts = float(input("Digite o valor em minutos que quer converter para segundos:\n--> "));
        total_segunds = qtd_minuts * 60;
        print("{} minutos são {:.2f} segundos".format(qtd_minuts, total_segunds));
    # se digitar 2, converte para segundos.    
    if convert == 2:
        # recebe um valor em segundos.
        qtd_segunds = float(input("Digite o valor em segundos que quer converter para minutos:\n--> "));
        total_minuts = qtd_segunds // 60;
        print("{} segundos são {:.2f} minutos".format(qtd_segunds, total_minuts));
    # se digitar 3, converte de horas para minutos.    
    if convert == 3:
        #recebe um valor em horas.
        qtd_horas = float(input("Digite o valor em horas que quer converter para minutos:\n--> "));
        total_minuts = qtd_horas * 60;
        print("{} horas são {:.2f} minutos".format(qtd_horas, total_minuts));
    # se digitar 4, converte de horas para segundos.
    if convert == 4:
        #recebe um valor em horas.
        qtd_horas = float(input("Digite o valor em horas que quer converter para segundos:\n--> "));
        total_segunds = qtd_horas * 3600;
        print("{} horas são {:.2f} segundos".format(qtd_horas, total_segunds));
    # se digitar 5, converte dias em horas.
    if convert == 5:
        # recebe um valor em dias.
        qtd_dias = int(input("Digite a quantidade de dias que quer converter em horas\n--> "));
        total_horas = qtd_dias * 24;
        print("{} dias tem {} horas".format(qtd_dias, total_horas));
    print("========================================"); 
    continuar = int(input("Fazer outra converção? SIM(1) NÃO(2):\n--> "));
    if continuar == 2:
        print("Até mais!");