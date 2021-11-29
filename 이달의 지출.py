#이달의 지출

jan = 0
feb = 0
mar = 0
apr = 0
may = 0
jun = 0
jul = 0
aug = 0
sep = 0
oct = 0
nov = 0
dec = 0


print('이달의 지출 프로그램을 시작합니다.')
print()
while True:
    execute = input("\n어떤 기능을 사용하실건가요? '끝내기'를 입력하면 프로그램이 종료됩니다.\n(지출기록, 월별 지출 확인, 올해 지출 확인, 끝내기) :")
    if execute =='끝내기':
        break

    elif execute == '지출기록' :
        month = input('\n몇 월인가요? ex. 1월, 12월 : ')
        spend = int(input('\n얼마를 썼나요? ex. 30000, 654000 : '))
        if month == '1월' :
            jan=jan+spend
        elif month == '2월' :
            feb=feb+spend
        elif month == '3월' :
            mar=mar+spend
        elif month == '4월' :
            apr=apr+spend
        elif month == '5월' :
            may=may+spend
        elif month == '6월' :
            jun=jun+spend
        elif month == '7월' :
            jul=jul+spend
        elif month == '8월' :
            aug=aug+spend
        elif month == '9월' :
            sep=sep+spend
        elif month == '10월' :
            oct=oct+spend
        elif month == '11월' :
            nov=nov+spend
        else :
            dec=dec+spend

    elif execute == '월별 지출 확인' :
        monthsum = input('\n지출을 확인할 해당 월을 입력해주세요 :')
        if monthsum == '1월' :
            print('\n1월은 %d원을 썼습니다.' % jan)
        elif monthsum == '2월' :
            print('\n2월은 %d원을 썼습니다.' % feb)
        elif monthsum == '3월' :
            print('\n3월은 %d원을 썼습니다.' % mar)
        elif monthsum == '4월' :
            print('\n4월은 %d원을 썼습니다.' % apr)
        elif monthsum == '5월' :
            print('\n5월은 %d원을 썼습니다.' % may)
        elif monthsum == '6월' :
            print('\n6월은 %d원을 썼습니다.' % jun)
        elif monthsum == '7월' :
            print('\n7월은 %d원을 썼습니다.' % jul) 
        elif monthsum == '8월' :
            print('\n8월은 %d원을 썼습니다.' % aug)
        elif monthsum == '9월' :
            print('\n9월은 %d원을 썼습니다.' % sep)
        elif monthsum == '10월' :
            print('\n10월은 %d원을 썼습니다.' % oct)
        elif monthsum == '11월' :
            print('\n11월은 %d원을 썼습니다.' % nov)     
        else :
            print('\n12월은 %d원을 썼습니다.' % dec)


    else:
        def yearaddition(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12):
            return (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12)

        print('\n%d월 ~ %d월의 지출 총 합계는 %d원입니다.' % (1, 12, yearaddition(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec)))
           
