import requests
import json

def obtain_new_access_token(refresh_token, app_key, app_secret):
    # Returns the new access token
    data = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
        'client_id': app_key,
        'client_secret': app_secret,
    }

    response = requests.post('https://api.dropbox.com/oauth2/token', data=data)
    response_text = response.text
    response_data = json.loads(response_text)
    access_token = response_data["access_token"]
    return access_token