import webbrowser
import requests
import base64
import json

# Step 2
def obtain_access_and_refresh_tokens(app_key, app_secret):
    access_code = input("Enter the access code obtained from the browser: ")

    basic_auth = base64.b64encode(f'{app_key}:{app_secret}'.encode())
    headers = {
        'Authorization': f"Basic {basic_auth}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = f'code={access_code}&grant_type=authorization_code'
    response = requests.post('https://api.dropboxapi.com/oauth2/token', data=data, auth=(app_key, app_secret))
    response_data = response.json()
    access_token = response_data.get("access_token")
    refresh_token = response_data.get("refresh_token")

    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    return access_token, refresh_token

# Step 1
def authenticate(app_key, app_secret):
    url = f'https://www.dropbox.com/oauth2/authorize?client_id={app_key}&' \
          f'response_type=code&token_access_type=offline'
    webbrowser.open(url)

    obtain_access_and_refresh_tokens(app_key=app_key, app_secret=app_secret)