"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
import requests
from HuelLibrary_Config import Browser,Students_WeChatSessionID
requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()

timeouts = 30
def network(urls):
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests_with_session.get(url=urls,headers=Browser,cookies=Students_WeChatSessionID,timeout=timeouts,verify=False)
    return response