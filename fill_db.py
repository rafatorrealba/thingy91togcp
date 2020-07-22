import time
import requests

func_url = "https://us-central1-guminator.cloudfunctions.net/query_write"
num_data = 10
rec_sec = 10
start = 1

while start < (num_data + 1):
	req = requests.get(func_url).text
	if str(req) == "Base de datos actualizada":
		print(start, req)
	else:
		print(start, requests.get(func_url).text)
	time.sleep(rec_sec)
	start += 1

print("Según el acuerdo cada dato colectado equivale a 0.5 USD, los datos colectados en el ultimo ciclo de trabajo son:", num_data, "datos.\nEl precio a pagar es de:", (start - 1) * 0.5, "USD.")
