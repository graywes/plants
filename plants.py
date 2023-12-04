import requests
r = requests.get('https://trefle.io/api/v1/genus?token=Gj6PVBkgY2x-Ix-pSKkrC6Z8g0XgirEHpwSA_Vd6pKQ')
with open("hi.txt", "w") as f:
    print(r.json(), file=f)