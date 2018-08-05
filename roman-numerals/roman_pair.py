def decimal_to_roman(decimal_number):
    import collections

    roman = [[1,'I'],[5,'V'],[10,'X'],[50,'L'],[100,'C'],[500,'D'],[1000,'M']]
    exc = collections.OrderedDict()
    exc['DCCCC'] = ['CM']
    exc['CCCC'] = ['CD']
    exc['LXXXX'] = ['XC']
    exc['XXXX'] = ['XL']
    exc['VIIII'] = ['IX']
    exc['IIII'] = ['IV']

    i = 0
    e = 0
    newd = decimal_number
    ro = ''
    while newd > 0:
        for k in roman:
            #print('k is: {}'.format(k))
            if k[0] <= newd:
               i += 1
               #print('i is: {}'.format(i))
            else:
               #print('substract now: {}'.format(roman[i-1][0]))
               newd -= roman[i-1][0]
               #print('newd is: {}'.format(newd))
               ro += roman[i-1][1]
               #print('ro is: {}'.format(ro))
               i = 0
               #e += 1
               break
        #print(newd, ro)

    #PARSE THROUGH ANSWER AND REMOVE EXCEPTIONS
    for thing in exc:
        print('thing is: ', thing)
        if thing in ro:
            switchto=exc.get(thing)
            print (type(switchto))
            print (switchto)
            #switchto = exc[thing]
            print('switchto is: ',str(switchto))
            newnotation = ro.replace(ro, str(switchto), 1)
            print(type(newnotation))
            print('ro was: ', ro, 'newnotation is: ', str(newnotation))
        else:
            print(ro)
            #break


#decimal_to_roman(1000)
#decimal_to_roman(900)
#decimal_to_roman(657)
decimal_to_roman(443)
#decimal_to_roman(90)
#decimal_to_roman(94)
#decimal_to_roman(43)
