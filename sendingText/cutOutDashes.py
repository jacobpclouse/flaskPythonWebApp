
def telephoneCutOut(tel):
    newlist = ''
    for x in tel:
        #newlist+ x.replace('-', '')
        if x != '-':
            newlist = newlist + x

    print(newlist)


telephoneCutOut("1-518-867-5309")