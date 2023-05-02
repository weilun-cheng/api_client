import sys
import logging
import time
logger = logging.getLogger('test')
formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=formatter)

import api_client.fortipam_client as client


ApiClient=client.FortiPAMApiClient

if __name__ == "__main__":
    api = [("10.160.29.32", 443, True)]
    user = "admin"
    password = "fortinet"
    cli = ApiClient(api, user, password, singlethread=False, auto_login=True, http_timeout=300)
    secret_name = 'test10001'
    message = {
        "folder": 3,
        "name": secret_name,
        "secret_template": "FortiProduct (SSH Password)",
        "host": "1.1.1.1",
        "username": "admin",
        "password": "password",
        "url": "",
        "inherit_permission": "enable"
    }
    res = cli.request('CREATE_SECRET', **message)
    print(f'CREATE_SECRET: {res.body}')
    res = cli.request('CREATE_SECRET', **message)
    print(f'CREATE_SECRET: {res.body}')
    # res = cli._login()