def fundtrans():
    accno = int(input("ENTER ACCOUNT NO. : "))
    recacc = int(input("RECIEVER'S ACCOUNT NO. : "))
    amt = float(input("AMOUNT TO TRANSFER : "))
    print("""List of Modes of Fund Transfer:-
1. Same Bank Fund Transfer
>> For Fund Transfer in Different Bank:
2. NEFT(National Electronic Fund Transfer)
3. RTGS(Real Time Gross Settlement)
4. IMPS(Instant Money Payment System)""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("""Requirements & Conditions for Same Bank Fund Transfer:-
1. Fund Transfer Form
2. No bank charge required
3. Early Transfer
4. Transfer take place during 9:00am to 5:00pm (Bank Timing) only
5. No limit on Fund Transfer""")
        ch = "Same bank"
        st = '''INSERT INTO FundTransfer(Acc_No_Sender,Acc_no_Receiver,Amt_to_Transfer,Mode_of_Transfer,Bank_Charge,Net_Amt_Transferred)
    VALUES({},{},{},'{}',{},{})'''.format(accno,recacc,amt,ch,0,amt)
    elif ch == 2:
        print("""Requirements & Conditions for NEFT:-
1. Fund Transfer Form
2. Bank Charge : 4% of Amount to Transfer
3. Time Taken : 24 hours
4. Transfer take place during 9:00am to 5:00pm (Bank Timing) only
5. No limit on Fund Transfer""")
        ch = "NEFT"
        charge = (4/100)*amt
        st = '''INSERT INTO FundTransfer(Acc_No_Sender,Acc_no_Receiver,Amt_to_Transfer,Mode_of_Transfer,Bank_Charge,Net_Amt_Transferred)
    VALUES({},{},{},'{}',{},{})'''.format(accno,recacc,amt,ch,charge,amt-charge)
    elif ch == 3:
        print("""Requirements & Conditions for RTGS:-
1. Fund Transfer Form
2. Bank Charge : 4% of Amount to Transfer
3. Time Taken : 24 hours
4. Transfer take place during 9:00am to 5:00pm (Bank Timing) only
5. Limit on Fund Transfer : Above 2 lakhs""")
        ch = "RTGS"
        charge = (4/100)*amt
        st = '''INSERT INTO FundTransfer(Acc_No_Sender,Acc_no_Receiver,Amt_to_Transfer,Mode_of_Transfer,Bank_Charge,Net_Amt_Transferred)
    VALUES({},{},{},'{}',{},{})'''.format(accno,recacc,amt,ch,charge,amt-charge)
    elif ch == 4:
        print("""Requirements & Conditions for IMPS:-
1. Fund Transfer Form/Online Application
2. Bank Charge : 4% of Amount to Transfer
3. Time Taken : Instant
4. 24 X 7 hours Service Available
5. Limit on Fund Transfer : Maximum 1 lakh""")
        ch = "IMPS"
        charge = (4/100)*amt
        st = '''INSERT INTO FundTransfer(Acc_No_Sender,Acc_no_Receiver,Amt_to_Transfer,Mode_of_Transfer,Bank_Charge,Net_Amt_Transferred)
    VALUES({},{},{},'{}',{},{})'''.format(accno,recacc,amt,ch,charge,amt-charge)
    return st,ch
def withdraw1(mc):
    accno = int(input("ENTER ACCOUNT NO. : "))
    name = input("ACCOUNT HOLDER NAME : ")
    typ = input("TYPE OF ACCOUNT : ")
    wthd = float(input("AMOUNT TO WITHDRAW : "))
    mc.execute("Select * from Transaction")
    table1 = mc.fetchall()
    def balance(table1):
        for row in table1:
            bal1 = row[5]
        return bal1
    blnc1 = balance(table1)
    st = "INSERT INTO Transaction(Acc_No,Holder_Name,Type_of_Acc,Withdrw_Amt,Bal_in_Acc) VALUES({},'{}','{}',{},{})".format(accno,name.upper(),typ.upper(),wthd,blnc1)
    return st
def withdraw2():
    accno = int(input("ENTER FD ACCOUNT NO. : "))
    name = input("ACCOUNT HOLDER NAME : ")
    return accno,name
def deposit1(mc):
    accno = int(input("ENTER ACCOUNT NO. : "))
    name = input("ACCOUNT HOLDER NAME : ")
    dep = float(input("AMOUNT TO DEPOSIT : "))
    typ = input("TYPE OF ACCOUNT : ")
    mc.execute("Select * from Transaction")
    table2 = mc.fetchall()
    if table2 == [] or table2 == ():
        st = "INSERT INTO Transaction(Acc_No,Holder_Name,Type_of_Acc,Dep_Amt) VALUES({},'{}','{}',{})".format(accno,name.upper(),typ.upper(),dep)
    else:
        def balance(table2):
            for row in table2:
                bal2 = row[5]
            return bal2
        blnc2 = balance(table2)
        st = "INSERT INTO Transaction(Acc_No,Holder_Name,Type_of_Acc,Dep_Amt,Bal_in_acc) VALUES({},'{}','{}',{},{})".format(accno,name.upper(),typ.upper(),dep,blnc2)
    return st
def deposit2():
    nam = input("ENTER ACCOUNT HOLDER NAME : ")
    amt = float(input('AMOUNT TO DEPOSIT : '))
    dur = int(input("DURATION(IN MONTHS) : "))
    st = '''INSERT INTO FDacc(Holder_Name,Dep_Amt,Duration,ROI_per_duration)
    VALUES('{}',{},{},12)'''.format(nam.upper(),amt,dur)
    return st