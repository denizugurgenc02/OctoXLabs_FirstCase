import json
import requests
import os

class RequestFactory: #pdf'de istenen sınıf.
    def __init__(self,path_address,method,headers,data):
        self.main_URL = os.getenv("main_URL", "https://httpbin.org/")
        self.path_address = path_address
        self.method = method
        self.headers = headers
        self.myData = data
        self.appStart()

    #constractor a girilen metod seçimine göre yönlendirme yapılacak.
    def appStart(self):
        if self.method.upper() == "GET":
            self.getRequest()
        elif self.method.upper() == "POST":
            self.postRequest()
        elif self.method.upper() == "PUT":
            self.putRequest()
        elif self.method.upper() == "DELETE":
            self.deleteRequest()
        else: #Yanlış formatta girilmiş ise exeption atar.
            raise Exception("Not Acceptable Value.!")

    #Get metodu sunucudan veri alır.
    def getRequest(self):
        response = requests.get(f"{self.main_URL}/{self.path_address}", headers = self.headers)
        print("Server Response:",response.status_code)#Sunucunun cevabını konsola yazar. bazı web sayfaları request isteğine cevap vermez örnek: sahibinden.com
        self.write(response.text)#Cevabı write fonksiyonuna gönderir.

    #Post metodu sunucuya işlenmesi için veri gönderir.
    def postRequest(self):
        response = requests.post(f"{self.main_URL}/{self.path_address}", data = self.myData, headers=self.headers)
        print("Server Response:",response.status_code)
        self.write(response.text)

    #Put metodu sunucudaki veriyi günceller.
    def putRequest(self):
        response = requests.put(f"{self.main_URL}/{self.path_address}", data = self.myData, headers=self.headers)
        print("Server Response:",response.status_code)
        self.write(response.text)

    #Delete metodu sunucudaki veriyi siler.Tehlikeli.!
    def deleteRequest(self):
        response = requests.delete(f"{self.main_URL}/{self.path_address}", headers=self.headers)
        print("Server Response:",response.status_code)
        self.write(response.text)

    #Sunucudan gelen cevabı proje adresine json formatında yazar.
    def write(self,data):
        with open("demo.txt", "w") as outfile: # w = üstüne yazmaz.
            outfile.write(data)

#Test Ediyorum.
app = RequestFactory("post", "post", {"accept": "application/json"}, {"username":"denizugurgenc02"})