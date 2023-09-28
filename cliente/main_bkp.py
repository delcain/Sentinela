import requests
import os
import subprocess
import socket
from datetime import datetime
import ctypes
import asyncio

async def jornada():
    while True:
        try:
            user = os.getlogin()
            hosttime = datetime.now()
            hosttimestring = hosttime.strftime("%H:%M")
            hostname = socket.gethostname()
            # URL da API
            # Coleta os dados baseado no nome do usuário logado no windows
            url = 'http://sentinela.cuidadodigital.com.br/username/?username=' + user
            response = requests.get(url=url)
            response_data = response.json()

            for user in response_data:
                nome = (user['nome'])
                username = (user['username'])
                jor1 = (user['jor1'])
                jor2 = (user['jor2'])
                jor3 = (user['jor3'])
                jor4 = (user['jor4'])

                print(username, jor1, jor2, jor3, jor4)

            # Verifica se a hora do computador é maior que o horário de retorno do almoço e menor que inicio do retorno do almoço
            if hosttimestring > jor2 and hosttimestring < jor3:
                subprocess.Popen(r'%windir%\system32\mshta.exe \\sari.adv.br\\NETLOGON\\sari_splash_bloquear.hta', shell=True)
                # Envia post para API como ação executada
                requests.post("http://sentinela.cuidadodigital.com.br/api/sinal/", json={
                    "username": username,
                    "hostname": hostname,
                    "acao": "lockstation"})
                ctypes.windll.user32.LockWorkStation()

            # Verifica se hora do computador é Maior que horário de saída e menor que horario de entrada
            if hosttimestring > jor4 or hosttimestring < jor1:
                # Chama Splah com agradecimento
                subprocess.Popen(r'%windir%\system32\mshta.exe \\sari.adv.br\\NETLOGON\\sari_splash_desligar.hta', shell=True)
                # Faz o post na API informando a ação
                requests.post("http://sentinela.cuidadodigital.com.br/api/sinal/", json={
                    "username": username,
                    "hostname": hostname,
                    "acao": "shutdown"})
                # Chama o Shutdown
                os.system("shutdown /s /t 180 ")
            # Await assincrono.. Tarefa se repete a cada 5 seg.

            await asyncio.sleep(100)
        except Exception:
            pass

async def dados():
    while True:
        try:
            #Envia a cada 5 minutos dados do computador.
            username = os.getlogin()
            hostname = socket.gethostname()
            dados = {
                "username": username,
                "hostname": hostname,
            }
            requests.post("http://sentinela.cuidadodigital.com.br/api/dados/", json=dados)
            await asyncio.sleep(300)

            print("Envio de Sinal:", username, hostname, dados)

        except Exception:
            pass

loop = asyncio.get_event_loop()

asyncio.ensure_future(jornada())
asyncio.ensure_future(dados())

loop.run_forever()