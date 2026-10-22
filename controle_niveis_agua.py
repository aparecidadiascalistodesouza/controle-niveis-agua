
from colorama import Fore, Style, init

init(autoreset=True)

niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

niveis_monitorados = [1, 2, 3, 4, 5]

print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in niveis_monitorados:
    mensagem = niveis_agua[nivel - 1]
    cor = definir_cor(nivel)
    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
