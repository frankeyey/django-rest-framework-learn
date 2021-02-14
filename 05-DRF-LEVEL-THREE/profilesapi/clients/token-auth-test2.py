import requests

def client():

  # data = {
  #   "username": "frank1",
  #   "email": "test@rest.com",
  #   "password1": "asdfasdf123",
  #   "password2": "asdfasdf123"
  # }

  # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

  token_h = "Token 3b2741cfc76b1b048961ac155bcf770b714dbd55"

  headers = {"Authorization": token_h}

  response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

  print("Status code: ", response.status_code)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()