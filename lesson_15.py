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
           'irlandiya':'Konor Makregor',
           'avstraliya':'Aleksandr Valkanovskiy',
           'qozog\'iston':'Shavkat Rahmanov',
           'qirg\'iziston':'Myktybek Oralbay',
           'italiya':'Marvin Vettori',
           'kanada':'Georg Sent-Pier (GSP)',
           'xitoy':'Song Yadong',
           'koreya':'Chan Sung Jung',
           'yaponiya':'Kazushi Sakuraba',
           'tailand':'Loma Lookboonmee',
           'avg\'oniston':'Nasrat Haqparast',
           'afrika':'Kamaru Usman',
           'ozarbayjon':'Rafael Fiziev',
           'Germaniya':'Dennis Siver',
           'polsha':'Jan Blachowicz',
           'fransiya':'Kiryl Gane',
           'turkiya':'Jengiz Nurmagamedov'}
davlat=input('Qaysi davlatning UFC jangchisini ko\'rishni xoxlaysiz? ').lower()
jangchi=f_country.get(davlat)
if davlat in f_country.keys():
    print(f'{davlat.title()}lik mashxur UFC jangchilaridan biri bu {jangchi.title()}')
else:
    print('Bu davlat sporti haqida bizda ma\'lumot mavjud emas!')