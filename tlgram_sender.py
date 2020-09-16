import requests
import time

def send_msg(txt):
    
    api_token="your telegram token"
    chat_id="your channel (i.e) chat id"
    # txt1="Updated: Nokia 6.1, Nokia 6.1 Plus, Nokia 7 Plus %26 Nokia 7.1 receiving August Security update now https://nokiapoweruser.com/nokia-7-1-nokia-6-1-plus-nokia-7-plus-receiving-august-security-update-now/"
    send_req="https://api.telegram.org/bot"+api_token+"/sendMessage?chat_id="+chat_id+"&text="+txt
    wait=0
    snd_flag=False
    while wait<30:
        try:
            resp=requests.get(send_req)
            wait=31
            snd_flag=True
        except:
            print("waiting for internet connection")
            time.sleep(10)
            wait+=10
    if snd_flag:
        if resp.json()['ok']==True:
            # print(f"the message has been send successfully to the channel")
            return(True)
    else:
        print(f"please try again after sometime...!!")
        return(False)




if __name__ == "__main__":
    usr_inp=input("enter your message: ")
    # usr_inp="<a href='https://nokiapoweruser.com/nokia-7-1-nokia-6-1-plus-nokia-7-plus-receiving-august-security-update-now/'>Updated: Nokia 6.1, Nokia 6.1 Plus, Nokia 7 Plus & Nokia 7.1 receiving August Security update now</a>"

    print(send_msg(usr_inp))