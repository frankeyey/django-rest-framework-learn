import requests

def client():
  token_h = "Token c23f8037af1e16203678ea267d78969f957ec29d"
  # credentials = {"username": "frank", "password": "asdfasdf"}

  # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

  headers = {"Authorization": token_h}

  response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

  print("Status code: ", response.status_code)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()