import requests

def obter_dados_meteorologicos():

    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    resposta = requests.get(url, params=parametros, timeout=15)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Falha encontrada: {resposta.raise_for_status()}")
        temperatura = dados["current"]["temperature_2m"]
        umidade = dados["current"]["relative_humidity_2m"]
        sensacao = dados["current"]["apparent_temperature"]
        precipitacao = dados["current"]["precipitation"]
        vento = dados["current"]["wind_speed_10m"]
        tempo = dados["current"]["time"]

        print(f"Tempo: {tempo}")
        print(f"Temperatura: {temperatura} °C")
        print(f"Umidade relativa: {umidade} %")
        print(f"Sensação térmica: {sensacao} °C")
        print(f"Precipitação: {precipitacao} mm")
        print(f"Velocidade do vento: {vento} km/h")
        return dados

    else:
        print("Falha na requisição.")
        print(f"Falha encontrada: {resposta.raise_for_status()}")

obter_dados_meteorologicos()