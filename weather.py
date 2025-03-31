import requests
def main():
    places = ["Лондон","Шереметьево","Череповец"] 
    payload = {"nTqmM&":"","lang":"ru"} 
    for place in places: 
        response = requests.get(f"https://wttr.in/{place}",params=payload )
        response.raise_for_status() 
        print(response.text)
if __name__ =='__main__': 
    main()
