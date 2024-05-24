import requests

def get_uuid(nickname):
    url = f"https://api.mojang.com/users/profiles/minecraft/{nickname}"
    response = requests.get(url)
    try:
        data = response.json()
        return data['id']
    except KeyError as e:
        print(f"Ошибка: попробуйте заново.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: не удалось получить UUID для никнейма (статус: {response.status_code})")

def get_name_history(uuid):
    url = f'https://laby.net/api/user/{uuid}/get-snippet'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    }
    try:
        res = requests.get(url, headers=headers)
        data = res.json()['name_history']
        print('=-----------------------=')
        for i in range(len(data)):
            userData = data[i]
            userString = ''
            userString += userData['username']
            userString += ' - ' + (str(userData['changed_at'])[:10] + ' ' + str(userData['changed_at'])[11:-6]).replace('-', '/')
            print(userString.replace('None', 'Первый никнейм'))
        print('=-----------------------=')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

def main():
    nickname = input('\033[96m> Введите никнейм: \033[0m')
    uuid = get_uuid(nickname)
    if uuid != None:
        get_name_history(uuid)
    else:
        print("Не удалось получить UUID.")

if __name__ == "__main__":
    main()
