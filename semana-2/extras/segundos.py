segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos)

dias = segundos / 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes / 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes / 60
segundos = segundos_restantes % 60

print(int(dias), "dias,", int(horas), "horas,", int(minutos), "minutos e", int(segundos), "segundos.")
