import sys
import logging
import time
# logger = logging.getLogger('test')
# formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=formatter)

import api_client.fortipam_client as client


ApiClient=client.FortiPAMApiClient

if __name__ == "__main__":
    api = [("1.1.1.1", 443, True)]
    user = "admin"
    password = "password"
    cli = ApiClient(api, user, password)
    cli._login()
    secret_name = 'test10001'
    message = {
        "folder": 3,
        "name": secret_name,
        "secret_template": "FortiProduct (SSH Password)",
        "host": "1.1.1.1",
        "username": "admin",
        "password": "password",
        "url": "",
        "inherit-permission": "enable"
    }
    res = cli.request('CREATE_SECRET', **message)
    print(res.status)
    print(res.body)
    time.sleep(2)
    res = cli.request('GET_SECRETS')
    print(res.status)
    print(res.body)
    secrets = res.body['results']
    secret_id = 0
    for secret in secrets:
        if secret['name'] == secret_name:
            secret_id = secret['id']
            break
    print(secret_id)
    res = cli.request('GET_SECRET', id=secret_id)
    print(res.status)
    print(res.body)
    res = cli.request('DELETE_SECRET', id=secret_id)
    print(res.status)
    print(res.body)

    # test FortiPAM folder API
    folder_name = "Auto_folder"
    message = {
        "name": folder_name
    }
    res = cli.request('CREATE_FOLDER', **message)
    print(res.status)
    print(res.body)
    time.sleep(2)
    res = cli.request('GET_FOLDERS')
    print(res.status)
    print(res.body)
    folders = res.body['results']
    for folder in folders:
        if folder['name'] == folder_name:
            folder_id = folder['id']
            break
    res = cli.request('GET_FOLDER', id=folder_id)
    print(res.status)
    print(res.body)
    res = cli.request('DELETE_FOLDER', id=folder_id)
    print(res.status)
    print(res.body)
