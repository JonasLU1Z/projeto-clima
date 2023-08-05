import requests

#  Entre no site https://openweathermap.org crie uma conta e utilize sua API-Key onde diz appid (não se esqueça de por entre aspas '').

appid = 
cidade = input('Qual a sua cidade? ').lower()

# A API para clima/tempo necessita das informações de latitude e longitude da cidade.
# A função abaixo utiliza uma API disponibilizada pelo próprio site para retornar as informações de latitude e longitude. 

def geo():
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={cidade}&appid={appid}'
    r = requests.get(url)
    resultado = r.json()
    latitude = resultado[0]['lat']
    longitude = resultado[0]['lon']
    return latitude, longitude

lat, lon = geo()

# A função abaixo utiliza as informações de latitude e longitude para retonar os dados sobre o clima/tempo da cidade que o usuario procurou.

def tempo():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=pt_br&units=metric&appid={appid}'
    r = requests.get(url)
    resultado = r.json()
    descricao = resultado['weather'][0]['description']
    temp_atual = resultado['main']['temp']
    sensacao = resultado['main']['feels_like']
    temp_maxi = resultado['main']['temp_max']
    temp_mini = resultado['main']['temp_min']
    humidade = resultado['main']['humidity']
    return descricao, temp_atual, sensacao, temp_maxi, temp_mini, humidade 

descricao, temp_atual, sensacao, temp_maxi, temp_mini, humidade = tempo()

clima = tempo()

# Resultado que aparecerá para o usuario no final.

print(f'Descrição: {descricao}')
print(f'Temperatura Atual: {temp_atual}°C')
print(f'Sensação Térmica: {sensacao}°C')
print(f'Temperatura Máxima: {temp_maxi}°C')
print(f'Temperatura Mínima: {temp_mini}°C')
print(f'Umidade: {humidade}%')


