#!/usr/bin/env python

import time
import os
import inspect

import api_client.fortiauth_client as client
import os
import random
from werkzeug.datastructures import FileStorage
import string
from io import BufferedReader
from codecs import encode, getreader

ApiClient=client.FortiAuthApiClient

if __name__ == "__main__":
    api = [("10.160.83.171", 8443, True)]
    key_file = '/etc/faccloud/ssl/client/cert201805231612.key'
    cert_file = '/etc/faccloud/ssl/client/cert201805231612.crt'
    ca_file = '/etc/faccloud/ssl/client/chain.pem'
    cli = ApiClient(api, key_file=key_file, cert_file=cert_file, ca_file=ca_file,
                    http_timeout=5, connect_timeout=5)

    print("----TESTING SYSTEMINFO------")
    res = cli.request("GET_SYSTEMINFO")
    assert res.status == 200
    print(res.body)


    print("----TESTING FTPSERVERS------")
    res = cli.request("GET_FTPSERVERS")
    assert res.status == 200
    print(res.body)

    print("----TESTING BACKUP------")
    res = cli.request("BACKUP_CONFIG")
    assert res.status == 200

    print("----TESTING UPGRADE------")
    params = {'url': 'http://10.160.83.217/faccloud111739/firmwares/FAC_VM_KVM-v6-build0976-FORTINET.out'}
    res = cli.request('UPGRADE_FIRMWARE', content_type='multipart/form-data', **params)
    print(res.status)
    print(res.body)

    print("----TESTING RESTORE------")
    fp = open('/home/weilun/Downloads/FACVMKVM-v6.4.1-build0976_180322-2138.conf', 'rb')
    message = {
        "file": fp
    }
    res = cli.request('RESTORE_CONFIG', content_type='multipart/form-data', **message)
    print(res.status)
    print(res.body)
