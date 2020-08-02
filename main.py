import urllib3
import json
import smtplib

http = urllib3.PoolManager()

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YourMailAddress@gmail.com', 'YourMailPassword') #Enter your gmail and password
    server.sendmail('YourMailAddress@gmail.com', to, content)
    server.close()

YourName=input("Enter Your name :")
numP=int(input("Enter No. of People You Wanna Wish :"))
prt_arr=list()
for i in range(numP):
    person=input("Enter mail address of the person you wanna send main(eg. xyzaaa@gmail.com) :")
    prt_arr.append(person)

def getQuote():
    url = "https://friends-quotes-api.herokuapp.com/quotes/random"
    r = http.request('GET', url)
    quote = json.loads(r.data.decode('utf-8'))
    content = f"\n*HAPPY FRIENDSHIP DAY*\n\n{quote['quote']}\n\n - {YourName}"
    return content

def wish():
    for i in range(numP):
        sendMail(prt_arr[i],getQuote())

wish()
print("All wishes has been sent successfully")