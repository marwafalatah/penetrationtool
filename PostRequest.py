import requests
import re

'''
setup DVWA on local Host
https://www.youtube.com/watch?v=Zh7WCKVuz1c
by watching this video the DVWA server is run on LOCALHOst nad th given script is sent post request to login on DVWA server provided by user naame and password

'''
"""
This method send the post request to Local host with payload of credentials and url is /dvwa/login.php

"""


def post_request(_username=" ", _password=""):
    with requests.Session() as c:
        url = 'https://jsonplaceholder.typicode.com/posts'  # thsi is url wher server is running
        data = {
            "userId": 1,
            "id": 1,
            "title": "Title is change by post request",
            "body": "minus omnis soluta quia\nqui sed adipisci voluptates illum ipsam voluptatem\neligendi officia ut in\neos soluta similique molestias praesentium blanditiis",
            "username": _username,
            "password": _password
        }  # thsi is the data we want to change on server
        """
        the below overall_data contain all data receive from get request to specified URL 
        """
        overall_data = c.get(
            url=str(url + "/1"))  # thsi is the data we receive from server before modificatioin /uploading
        print("Data receive from URL is given below before post request \n" + overall_data.text)

        '''
        The below metho will post the data to url in JSON format 
        '''

        updated_data = c.post(url=url,
                              data=data)  # here we will update data by using post request and retun updated data
        print("Data receive from URL is given below after post request \n" + updated_data.text)

        # token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
        # payload['user_token'] = token

        # p = c.post('https://127.0.0.1/dvwa/login.php', data=payload)
        # r = c.get('http://127.0.0.1/dvwa/vulnerabilities/exec')


if __name__ == "__main__":
    try:
        post_request()
    except ConnectionError:
        print("DVWA service is not running")
    except:
        print("DVWA service is not running")

'''
to run this file you must setup DVWA on your machine Provided by link https://www.youtube.com/watch?v=Zh7WCKVuz1c
th DVWA server is not setup on your machine so the above code throws error 
there isconnection error because the DVWA is not running on address 127.00.0.1:80
so first you setup the server and then postRequest file is run else remaing code work successfully with no bugs :)

'''
