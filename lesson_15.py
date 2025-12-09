# Davlat nomi orqali shu davlatlik UFC jangchilaridan birining ismini chiqarish

f_country={'brazilia':'Charles Oliviera',
           'ispaniya':'Ilia Topuria',
           "o'zbekiston":'Ramazon Temirov',
           'rassiya':'Pyotr Yan',
           "dog'iston":'Islam Maxachev',
           'avstraliya':'Aleksandr Valkanovskiy',
           'checheniston':'Xamzat Chimayev',
           'armaniston':'Arman Sarukiyan',
           'gruziya':'Merab Dvalashvili',
           'amerika':'Dastin Porier',
           'irlandiya':'Konor Makregor'}
davlat=input('Qaysi davlatning UFC jangchisini ko\'rishni xoxlaysiz? ').lower()
jangchi=f_country.get(davlat)
if davlat in f_country.keys():
    print(f'{davlat.title()}lik jangchilardan biri bu {jangchi.title()}')
else:
    print('Bu davlat sporti haqida bizda ma\'lumot mavjud emas!')