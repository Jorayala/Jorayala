#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:11:38 2019

@author: JorgeAlonsoAyala
"""



import requests


def get_token():
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers

    )

    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

def main():
    token = get_token()

    api_path =  "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}


    get_resp = requests.get(
        f"{api_path}/intent/api/v1/interface/count", headers=headers
        )

    import json; print(json.dumps(get_resp.json(), indent=2))


if __name__ == "__main__":
    main()
