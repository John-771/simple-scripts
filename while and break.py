# while sikli va break operatori qatnashgan dastur

matn='Sotib olmoqchi bo\'lgan buyumlaringizni kiriting: '
buyumlar=''
savat=[]
while True:
    buyumlar=input(matn)
    savat.append(buyumlar.title())
    if buyumlar=='exit' or buyumlar=='quit':
        break

print(f'\nDastur tugadi. Sizning savatingizda quyidagilar mavjud: ')
del savat[-1]
for m in savat:
    print(m)
