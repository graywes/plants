import requests
print(r"""
Greeting, and welcome to:
  _____  _             _                  
 |  __ \| |           | |                 
 | |__) | | __ _ _ __ | |_   _____  _____ 
 |  ___/| |/ _` | '_ \| __| / _ \ \/ / _ \
 | |    | | (_| | | | | |_ |  __/>  <  __/
 |_|    |_|\__,_|_| |_|\__(_)___/_/\_\___|
      
        By Wesley Grayson

Please enter command:  
      """)
text = 
r = requests.get('https://trefle.io/api/v1/plants/search?token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ&q=coconut')
with open("hi.txt", "w") as f:
    print(r.json(), file=f)