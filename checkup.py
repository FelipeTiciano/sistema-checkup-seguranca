import psutil
import socket
import os
from datetime import datetime

print("==== CHECKUP DO SISTEMA ====\n")

# CPU
cpu = psutil.cpu_percent(interval=1)
print(f"Uso da CPU: {cpu}%")

# Memória
memoria = psutil.virtual_memory()
print(f"Uso da RAM: {memoria.percent}%")

# Disco
disco = psutil.disk_usage('/')
print(f"Uso do Disco: {disco.percent}%")

# IP da máquina
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"IP da máquina: {ip}")

# Processos rodando
print("\nProcessos ativos (top 5):")
processos = list(psutil.process_iter(['pid', 'name']))

for proc in processos[:5]:
    print(proc.info)

# Verificar se Windows Defender está rodando
print("\nVerificação de segurança:")
defender = False

for proc in processos:
    if "MsMpEng.exe" in str(proc.info):
        defender = True

if defender:
    print("Status de segurança: Antivírus ativo)")
else:
    print("Antivírus NÃO identificado")

print("\n==== CHECKUP FINALIZADO ====")

agora = datetime.now()

with open("relatorio.txt", "w") as f:
    f.write(f"Data: {agora}\n")
    f.write(f"CPU: {cpu}%\n")
    f.write(f"RAM: {memoria.percent}%\n")
    f.write(f"Disco: {disco.percent}%\n")
    f.write(f"IP: {ip}\n")