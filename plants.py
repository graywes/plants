import requests
import json
import re
print(r"""
Greetings, and welcome to:
  _____  _             _                  
 |  __ \| |           | |                 
 | |__) | | __ _ _ __ | |_   _____  _____ 
 |  ___/| |/ _` | '_ \| __| / _ \ \/ / _ \
 | |    | | (_| | | | | |_ |  __/>  <  __/
 |_|    |_|\__,_|_| |_|\__(_)___/_/\_\___|
      
        By Wesley Grayson
     Commands
         exit
         search
         filter

Please enter command:  
      """)
text = input()
if text == "exit":
    quit
if text == "hi":
    r = requests.get('https://trefle.io/api/v1/plants/search?token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ&q=coconut')
    with open("hi.txt", "w") as f:
        print(r.json(), file=f)
if text == "search":
    print(r"""
1: common name
2: genus
3: scientific name
          """)
    query = input("enter property to search: ")
    if query == "common name" or query == "1":
        query = input("enter common name: ")
        search = 'https://trefle.io/api/v1/plants/search?q=' + query + '&token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ&filter=common_name'
        searched = requests.get(search)
        for j in searched.json().get("data"):
            print(j.get("common_name"))
        exit
    if query == "genus" or query == "2":
        query = input("how many pages?: ")
        page = input("which page to start?")
        for num in range(0, int(query)):
            search = 'https://trefle.io/api/v1/genus?token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ&page=' + (num + int(page)).__str__()
            searched = requests.get(search)
            for j in searched.json().get("data"):
                print(j.get("name"))
    if query == "scientific name" or "science" or "3":
        query = input("enter common name: ")
        search = 'https://trefle.io/api/v1/plants/search?q=' + query + '&token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ'
        searched = requests.get(search)
        for j in searched.json().get("data"):
            print(j.get("scientific_name"))
if text == "filter":
    query = input("enter common name: ")
    search = 'https://trefle.io/api/v1/plants/filter[5Bcommon_name]5D=' + query + '&token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ&'
    searched = requests.get(search)
    for j in searched.json().get("data"):
        print(j.get("common_name"))
    pass