#!/usr/bin/python3

import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bs

def get_codes(data):
    obj = bs(data, "html.parser")
    return obj.body.code

def main():
    parser = argparse.ArgumentParser(description="jenkins.yaml(jcas) export file tool")
    parser.add_argument('--user', type=str, default=None, help='username')
    parser.add_argument('--password', type=str, default=None, help='password')
    parser.add_argument('--url', type=str, default=None, help='domain or ip address')

    args = parser.parse_args()
    if args.url == None:
        print(parser.print_help())
        exit()

    auths = HTTPBasicAuth(args.user, args.password)

    r = requests.post(args.url, auth=auths, verify=False)
    if r.status_code == 200:
        _file = r'./jcas.yaml'
        _data = get_codes(r.text)
        try:
            f = open(_file, 'w')
            for line in _data:
                f.write(line)
        except Exception as e:
            print('error %s' % e)
        finally:
            f.close()
            print("Getting the jcas.yaml file finished")
    else:
        print("Response is not valid. Code: %d" % r.status_code)

if __name__ == "__main__":
    main()