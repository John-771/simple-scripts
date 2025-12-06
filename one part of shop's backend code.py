# Bunday kodlar restaran kafe yoki shunga o'xshash joylarda mijoz xoxish-istagini bildirishi uchun yaratilgan dasturning backend qismida uchraydi

mahsulotlar=['sut','qatiq','anor','banan','olma']
savat=[]
print('3 ta mahsulot qo\'shing')
for n in range(3):
    savat.append(input(f'{n+1}-mahsulot: '))
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f'Do\'konimizda {mahsulot} bor!')
        else:
            print(f'Do\'konimizda {mahsulot} mavjud emas')
else:
    print('Savat bo\'sh')