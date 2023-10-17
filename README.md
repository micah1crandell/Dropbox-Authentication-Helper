# Dropbox Authentication Helper

This Python package simplifies the process of obtaining and managing Dropbox application tokens for your projects. With this package, you can easily obtain and refresh your access tokens, making it convenient to work with Dropbox's API.

## Usage

Follow these steps to get started with the Dropbox Authentication Helper:

1. **Obtain App Key and App Secret**:

   First, you need to get your App Key and App Secret from the Dropbox App Console. If you don't have these credentials, create a Dropbox app on their developer platform.

2. **Installation**:

   You can install the package using pip:

   ```bash
   pip install dbx-auth-helper
   ```

3. **Import the Package**:

    Import the package in your Python code:

    ```bash
    from dbx-auth-helper import auth, access
    ```

4. **Set App Key and App Secret**:

    Set your App Key and App Secret in your code. Replace "app_key_goes_here" and "app_secret_goes_here" with your actual credentials:

    ```bash
    REFRESH_TOKEN = ""
    APP_KEY = "your_app_key"
    APP_SECRET = "your_app_secret"
    ```

5. **Authentication**:

    Use the package to authenticate with Dropbox. Run the following code:

    ```bash
    auth.authenticate(APP_KEY, APP_SECRET)
    ```
    
    This will open a web browser. Click \"Continue\" and \"Allow\" to grant the necessary permissions. After that, you\'ll receive an access code. Copy this code.

    **Paste Access Code**:

    Go back to your terminal and paste the access code you obtained from the browser into the terminal.

    **Get Access and Refresh Tokens**:

    Running the authentication process will print your new access token and refresh token. Copy the refresh token and replace the REFRESH_TOKEN value with it.

    **Remove Authentication Code**:

    Remove the following line from your code as you only need to authenticate once:

    ```bash
    auth.authenticate(APP_KEY, APP_SECRET)
    ```

    Remove \'auth\' from your import

    ```bash
    from dbx-auth-helper import access
    ```

6. **Obtain New Access Token**:

    Use the following code to obtain a new access token:

    ```bash
    ACCESS_TOKEN = access.obtain_new_access_token(REFRESH_TOKEN, APP_KEY, APP_SECRET)
    ```

7. **Final Configuration**:

    After the setup, your code should look like this for future use:

    ```bash
    from dbx_auth_helper import access
    

    REFRESH_TOKEN = "your_refresh_token"
    APP_KEY = "your_app_key"
    APP_SECRET = "your_app_secret"

    ACCESS_TOKEN = access.obtain_new_access_token(REFRESH_TOKEN, APP_KEY, APP_SECRET)

## With these steps, you can easily manage your Dropbox access tokens using this package.

# License

This project is licensed under the MIT License. See the LICENSE file for details.
