import subprocess
wifis = subprocess.check_output(['netsh' ,'wlan', 'show' ,'profiles'], encoding="cp858")

for wifi in wifis.split('\n'):
    if 'Todos os Perfis de Usuários' in wifi:
        info = subprocess.check_output(['netsh' ,'wlan', 'show' ,'profile', f'{wifi[wifi.find(":")+2:]}', 'key', '=', 'clear'], encoding="cp858")
        for senha in info.split('\n'):
            if 'Conteúdo da Chave' in senha:
                nome_wifi = wifi[wifi.find(":")+2:]
                print(f'wi-fi: {nome_wifi} {" " * (20-len(nome_wifi))} |   Senha: {senha[senha.find(":")+2:]}')
            