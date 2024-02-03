import requests    # pip install requests

# Înlocuiește aceste valori cu informațiile tale
X_AUTH_EMAIL = 'email@example.com'
X_AUTH_KEY = 'your_api_key'
ZONE_ID = 'your_zone_id'

# Header pentru autentificare
headers = {
    'X-Auth-Email': X_AUTH_EMAIL,
    'X-Auth-Key': X_AUTH_KEY,
    'Content-Type': 'application/json',
}

def delete_dns_records(zone_id):
    # Obține lista de înregistrări DNS
    dns_records_url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    dns_records = requests.get(dns_records_url, headers=headers).json()

    if dns_records['success']:
        for record in dns_records['result']:
            delete_url = f'{dns_records_url}/{record["id"]}'
            delete_response = requests.delete(delete_url, headers=headers).json()
            if delete_response['success']:
                print(f'Succes: Înregistrarea {record["name"]} a fost ștearsă.')
            else:
                print(f'Eroare: Nu s-a putut șterge înregistrarea {record["name"]}.')
    else:
        print('Eroare: Nu s-au putut obține înregistrările DNS.')

# Apelarea funcției
delete_dns_records(ZONE_ID)
