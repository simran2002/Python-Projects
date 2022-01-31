def FD():
    nam = input("ENTER ACCOUNT HOLDER NAME : ")
    amt = int(input('AMOUNT TO DEPOSIT : '))
    dur = int(input("DURATION(IN MONTHS) : "))
    st = '''INSERT INTO FDacc(Holder_Name,Dep_Amt,Duration,ROI_per_duration)
    VALUES('{}',{},{},{})'''.format(nam.upper(),amt,dur,'12%')
    return st,amt