
import requests

def GetCurrency(amount,current,next):
    url1 = f"https://v6.exchangerate-api.com/v6/04e870f6d0d9facfc2360ac5/latest/{current}"
    data = requests.get(url1)
    toJson1 = data.json()
    basecurrency = toJson1['base_code']
    print(basecurrency)
    # dollor = toJson1['conversion_rates']['USD']
    # rupees = toJson1['conversion_rates']['NPR']
    
    total_amount = amount * toJson1['conversion_rates'][next]
    print(total_amount)
    
    # print(f"Dollor : {dollor}")
    # print(f"Ruppees : {rupees}")
    
GetCurrency(1000,"NPR","USD")


try:
    amount = int(input("Enter a amount : "))
    current = input("Enter a Current Currency : ".upper())
    next = input("Enter a Next Currency : ").upper()
    
    GetCurrency(amount,current,next)
except Exception as e:
    print(e)