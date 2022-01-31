import mysql.connector
con = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mc = con.cursor()
mc.execute("Use Test")
import customer_login.acc_opening as custopen
import customer_login.transaction as custtxn
import customer_login.FD as custFD
import customer_login.LOAN as custLOAN
import customer_login.acc_close as custclose
import employee_login.dep_wthd as emptxn
import employee_login.fund_transfer as empFT
import employee_login.loan as emploan
import employee_login.acc_opn_verify as empverifyacc
import employee_login.loan_verify as empverifyloan
print("---------WELCOME To STAR SERVICE BANK----------")
print('''1. Customer
2. Employee
3. Exit''')
ch1 = int(input("Enter your choice: "))
if ch1 == 1:
    print('''What do you want to do?
1. Open an account
2. Deposit money
3. Withdraw money
4. Fund Transfer
5. Apply for Loan
6. Close your Account''')
    ch2 = int(input("Enter your choice: "))
    if ch2 == 1:
        print('''Which type of account you want to open?
1. Savings Account
2. Joint Account
3. Current Account''')
        ch3 = int(input("Enter your choice: "))
        if ch3 == 1:
            data = custopen.savacc()
            print("Thank you for submitting your details!!!")
            ans1,ans2,ans3 = empverifyacc.verfsavacc()
            if ans1 == ans2 == ans3 == 'y' or ans1 == ans2 == ans3 == 'Y':
                print("Your all documents are verified !!!")
                mc.execute(data)
                mc.execute("commit")
                print('Congratulations Your Savings Account has opened Successfully!!!')
                mc.execute("Select * from AccDetails")
                tbaccno = mc.fetchall()
                for row in tbaccno:
                    acno = row[1]
                print("Your Account Number is: ",acno)
            else:
                print("Sorry, your account hasn't opened as you have not submmited valid/all document(s) !!!")
        elif ch3 == 2:
            data = custopen.jointacc()
            ans1,ans2,ans3 = empverifyacc.verfjntacc()
            if ans1 == ans2 == ans3 == 'y' or ans1 == ans2 == ans3 == 'Y':
                mc.execute(data)
                mc.execute("commit")
                print('Congratulations Your Joint Account has opened Successfully!!!')
                mc.execute("Select * from AccDetails")
                tbaccno = mc.fetchall()
                for row in tbaccno:
                    acno = row[1]
                print("Your Account Number is: ",acno)
            else:
                print("Sorry, your account hasn't opened as you have not submmited valid/all document(s) !!!")
        elif ch3 == 3:
            data = custopen.curracc()
            ans1,ans2,ans3 = empverifyacc.verfcurracc()
            if ans1 == ans2 == ans3 == 'y' or ans1 == ans2 == ans3 == 'Y':
                mc.execute(data)
                mc.execute("commit")
                print('Congratulations Your Current Account has opened Successfully!!!')
                mc.execute("Select * from AccDetails")
                tbaccno = mc.fetchall()
                for row in tbaccno:
                    acno = row[1]
                print("Your Account Number is: ",acno)
            else:
                print("Sorry, your account hasn't opened as you have not submmited valid/all document(s) !!!")
    elif ch2 == 3:
        print('''Withdraw From???
1. Saving/Joint/Current Account
2. FD Account''')
        typ = int(input("Enter your choice: "))
        if typ == 1:
            data1 = custtxn.withdraw1(mc)
            mc.execute(data1)
            mc.execute("Commit")
            mc.execute("Select * from Transaction")
            table1 = mc.fetchall()
            def txn(table1):
                for row in table1:
                    acc_no1 = row[0]
                    bal = row[5]
                    wthdrw = row[4]
                return acc_no1,bal,wthdrw
            accno1,balamt,wthdrwamt = txn(table1)
            data2 = emptxn.withdrw1(accno1,wthdrwamt)
            mc.execute(data2)
            mc.execute("Commit")
            print("Withdrawed successfully!!!")
        elif typ == 2:
            accno2,name = custtxn.withdraw2()
            mc.execute("Select * from FDacc")
            table2 = mc.fetchall()
            def txn(table2):
                for row in table2:
                    dep = row[2]
                    roi = row[4]
                    bal = row[5]
                return dep,roi,bal
            depamtFD,roiFD,balFD = txn(table2)
            data2 = emptxn.withdrw2(accno2,depamtFD,roiFD)
            mc.execute(data2)
            mc.execute("Commit")
            print("Withdrawed successfully!!!")
    elif ch2 == 2:
        print('''Deposit To????
1. Savings/Joint/Current Account
2. FD Account''')
        typ = int(input("Enter your choice: "))
        if typ == 1:
            data1 = custtxn.deposit1(mc)
            mc.execute(data1)
            mc.execute("Commit")
            mc.execute("Select * from Transaction")
            table1 = mc.fetchall()
            def txn(table1):
                for row in table1:
                    acc_no1 = row[0]
                    bal = row[5]
                    dep = row[3]
                return acc_no1,bal,dep
            accno1,balamt,depamt = txn(table1)
            data2 = emptxn.depst1(accno1,depamt)
            mc.execute(data2)
            mc.execute("Commit")
            print("Deposited successfully!!!")
        elif typ == 2:
            data1 = custtxn.deposit2()
            mc.execute(data1)
            mc.execute("Commit")
            mc.execute("Select * from FDacc")
            table2 = mc.fetchall()
            def txn(table2):
                for row in table2:
                    acc_no2 = row[0]
                    dep = row[2]
                    bal = row[5]
                return acc_no2,dep,bal
            accno2,depamtFD,balFD = txn(table2)
            data2 = emptxn.depst2(accno2,depamtFD)
            mc.execute(data2)
            mc.execute("Commit")
            print("Deposited successfully!!!")
    elif ch2 == 4:
        data,ch = custtxn.fundtrans()
        mc.execute(data)
        mc.execute("Commit")
        mc.execute("Select * from FundTransfer")
        table = mc.fetchall()
        def ft(table):
            for row in table:
                acc_noS = row[0]
                acc_noR = row[1]
                amtrf = row[2]
                bnkchrg = row[4]
            return acc_noS,acc_noR,amtrf,bnkchrg
        accnoS,accnoR,amttrf,bankchr = ft(table)
        if ch == "Same bank":
            dt1,dt2 = empFT.FT1(accnoS,accnoR,amttrf,bankchr)
            mc.execute(dt1)
            mc.execute(dt2)
            mc.execute("Commit")
            print("Fund Transferrred Successfully!!!")
        elif ch == "NEFT" or ch == "RTGS" or ch == "IMPS":
            dt = empFT.FT2(accnoS,amttrf,bankchr)
            mc.execute(dt)
            mc.execute("Commit")
            print("Fund Transferrred Successfully!!!")
    elif ch2 == 5:
        data1,typ = custLOAN.loan()
        if typ == "Personal":
            ans1,ans2,ans3,ans4 = empverifyloan.perloan()
            if ans1 == ans2 == ans3 == ans4 == 'y' or ans1 == ans2 == ans3 == ans4 == 'Y':
                mc.execute(data1)
                mc.execute("Commit")
                mc.execute("Select * from Loan")
                table1 = mc.fetchall()
                def loantb(table1):
                    for row in table1:
                        name = row[0]
                        typ = row[1]
                        civchr = row[2]
                        lnamt = row[3]
                        dur = row[4]
                        ROI = row[5]
                        freq = row[6]
                    return name,typ,civchr,lnamt,dur,ROI,freq
                nam,typ,civ,loanamt,dura,roi,frequ = loantb(table1)
                emploan.loancalc(frequ,dura,loanamt,roi,mc)
                if civ >= 6 and civ <= 10:
                    print()
                    print("Congratulations your loan has APPROVED!!!")
                    print()
                    print("Your Loan Statement is as Follows:- ")
                    print("Name: ",nam)
                    print("Type of Loan: ",typ)
                    print("Loan Amount: ",loanamt)
                    print("Duration: ",dura)
                    print("Rate of Interest: ",roi)
                    print("Frequency: ",frequ)
                    print()
                    print("Instl Num","\t","Open Prin","\t\t","EMI","\t\t\t","Principal","\t\t","Interest","\t\t","Clos Prin","\t\t","Rate")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    mc.execute("Select * from LoanState")
                    table = mc.fetchall()
                    for row in table:
                        no = row[0]
                        opnprin = row[1]
                        EMI = row[2]
                        prin = row[3]
                        ints = row[4]
                        clsprin = row[5]
                        rate = row[6]
                        print(no,"\t\t",opnprin,"\t\t",EMI,"\t\t",prin,"\t\t",ints,"\t\t",clsprin,"\t\t",rate)
                    mc.execute("Select sum(EMI),sum(Principal),sum(Interest_Amt) from LoanState")
                    total = mc.fetchall()
                    for row in total:
                        totEMI = row[0]
                        totPrin = row[1]
                        totInt = row[2]
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Total: ","\t\t","\t\t",totEMI,"\t\t",totPrin,"\t\t",totInt)
            else:
                print("Loan not APPROVED!!!")
        elif typ == "Home":
            ans1,ans2,ans3,ans4 = empverifyloan.homloan()
            if ans1 == ans2 == ans3 == ans4 == 'y' or ans1 == ans2 == ans3 == ans4 == 'Y':
                mc.execute(data1)
                mc.execute("Commit")
                mc.execute("Select * from Loan")
                table1 = mc.fetchall()
                def loantb(table1):
                    for row in table1:
                        name = row[0]
                        typ = row[1]
                        civchr = row[2]
                        lnamt = row[3]
                        dur = row[4]
                        ROI = row[5]
                        freq = row[6]
                    return name,typ,civchr,lnamt,dur,ROI,freq
                nam,typ,civ,loanamt,dura,roi,frequ = loantb(table1)
                emploan.loancalc(frequ,dura,loanamt,roi,mc)
                if civ >= 6 and civ <= 10:
                    print()
                    print("Congratulations your loan has APPROVED!!!")
                    print()
                    print("Your Loan Statement is as Follows:- ")
                    print("Name: ",nam)
                    print("Type of Loan: ",typ)
                    print("Loan Amount: ",loanamt)
                    print("Duration: ",dura)
                    print("Rate of Interest: ",roi)
                    print("Frequency: ",frequ)
                    print()
                    print("Instl Num","\t","Open Prin","\t\t","EMI","\t\t\t","Principal","\t\t","Interest","\t\t","Clos Prin","\t\t","Rate")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    mc.execute("Select * from LoanState")
                    table = mc.fetchall()
                    for row in table:
                        no = row[0]
                        opnprin = row[1]
                        EMI = row[2]
                        prin = row[3]
                        ints = row[4]
                        clsprin = row[5]
                        rate = row[6]
                        print(no,"\t\t",opnprin,"\t\t",EMI,"\t\t",prin,"\t\t",ints,"\t\t",clsprin,"\t\t",rate)
                    mc.execute("Select sum(EMI),sum(Principal),sum(Interest_Amt) from LoanState")
                    total = mc.fetchall()
                    for row in total:
                        totEMI = row[0]
                        totPrin = row[1]
                        totInt = row[2]
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Total: ","\t\t","\t\t",totEMI,"\t\t",totPrin,"\t\t",totInt)
            else:
                print("Loan not APPROVED!!!")
        elif typ == "Education":
            ans1,ans2,ans3,ans4,ans5,ans6 = empverifyloan.eduloan()
            if ans1 == ans2 == ans3 == ans4 == ans5 == ans6 == 'y' or ans1 == ans2 == ans3 == ans4 == ans5 == ans6 == 'Y':
                mc.execute(data1)
                mc.execute("Commit")
                mc.execute("Select * from Loan")
                table1 = mc.fetchall()
                def loantb(table1):
                    for row in table1:
                        name = row[0]
                        typ = row[1]
                        civchr = row[2]
                        lnamt = row[3]
                        dur = row[4]
                        ROI = row[5]
                        freq = row[6]
                    return name,typ,civchr,lnamt,dur,ROI,freq
                nam,typ,civ,loanamt,dura,roi,frequ = loantb(table1)
                emploan.loancalc(frequ,dura,loanamt,roi,mc)
                if civ >= 6 and civ <= 10:
                    print()
                    print("Congratulations your loan has APPROVED!!!")
                    print()
                    print("Your Loan Statement is as Follows:- ")
                    print("Name: ",nam)
                    print("Type of Loan: ",typ)
                    print("Loan Amount: ",loanamt)
                    print("Duration: ",dura)
                    print("Rate of Interest: ",roi)
                    print("Frequency: ",frequ)
                    print()
                    print("Instl Num","\t","Open Prin","\t\t","EMI","\t\t\t","Principal","\t\t","Interest","\t\t","Clos Prin","\t\t","Rate")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    mc.execute("Select * from LoanState")
                    table = mc.fetchall()
                    for row in table:
                        no = row[0]
                        opnprin = row[1]
                        EMI = row[2]
                        prin = row[3]
                        ints = row[4]
                        clsprin = row[5]
                        rate = row[6]
                        print(no,"\t\t",opnprin,"\t\t",EMI,"\t\t",prin,"\t\t",ints,"\t\t",clsprin,"\t\t",rate)
                    mc.execute("Select sum(EMI),sum(Principal),sum(Interest_Amt) from LoanState")
                    total = mc.fetchall()
                    for row in total:
                        totEMI = row[0]
                        totPrin = row[1]
                        totInt = row[2]
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Total: ","\t\t","\t\t",totEMI,"\t\t",totPrin,"\t\t",totInt)
            else:
                print("Loan not APPROVED!!!")
        elif typ == "Business":
            ans1,ans2,ans3,ans4,ans5,ans6 = empverifyloan.busloan()
            if ans1 == ans2 == ans3 == ans4 == ans5 == ans6 == 'y' or ans1 == ans2 == ans3 == ans4 == ans5 == ans6 == 'Y':
                mc.execute(data1)
                mc.execute("Commit")
                mc.execute("Select * from Loan")
                table1 = mc.fetchall()
                def loantb(table1):
                    for row in table1:
                        name = row[0]
                        typ = row[1]
                        civchr = row[2]
                        lnamt = row[3]
                        dur = row[4]
                        ROI = row[5]
                        freq = row[6]
                    return name,typ,civchr,lnamt,dur,ROI,freq
                nam,typ,civ,loanamt,dura,roi,frequ = loantb(table1)
                emploan.loancalc(frequ,dura,loanamt,roi,mc)
                if civ >= 6 and civ <= 10:
                    print()
                    print("Congratulations your loan has APPROVED!!!")
                    print()
                    print("Your Loan Statement is as Follows:- ")
                    print("Name: ",nam)
                    print("Type of Loan: ",typ)
                    print("Loan Amount: ",loanamt)
                    print("Duration: ",dura)
                    print("Rate of Interest: ",roi)
                    print("Frequency: ",frequ)
                    print()
                    print("Instl Num","\t","Open Prin","\t\t","EMI","\t\t\t","Principal","\t\t","Interest","\t\t","Clos Prin","\t\t","Rate")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    mc.execute("Select * from LoanState")
                    table = mc.fetchall()
                    for row in table:
                        no = row[0]
                        opnprin = row[1]
                        EMI = row[2]
                        prin = row[3]
                        ints = row[4]
                        clsprin = row[5]
                        rate = row[6]
                        print(no,"\t\t",opnprin,"\t\t",EMI,"\t\t",prin,"\t\t",ints,"\t\t",clsprin,"\t\t",rate)
                    mc.execute("Select sum(EMI),sum(Principal),sum(Interest_Amt) from LoanState")
                    total = mc.fetchall()
                    for row in total:
                        totEMI = row[0]
                        totPrin = row[1]
                        totInt = row[2]
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Total: ","\t\t","\t\t",totEMI,"\t\t",totPrin,"\t\t",totInt)
            else:
                print("Loan not APPROVED!!!")
        elif typ == "Vehicle":
            ans1,ans2,ans3,ans4 = empverifyloan.vehloan()
            if ans1 == ans2 == ans3 == ans4 == 'y' or ans1 == ans2 == ans3 == ans4 == 'Y':
                mc.execute(data1)
                mc.execute("Commit")
                mc.execute("Select * from Loan")
                table1 = mc.fetchall()
                def loantb(table1):
                    for row in table1:
                        name = row[0]
                        typ = row[1]
                        civchr = row[2]
                        lnamt = row[3]
                        dur = row[4]
                        ROI = row[5]
                        freq = row[6]
                    return name,typ,civchr,lnamt,dur,ROI,freq
                nam,typ,civ,loanamt,dura,roi,frequ = loantb(table1)
                emploan.loancalc(frequ,dura,loanamt,roi,mc)
                if civ >= 6 and civ <= 10:
                    print()
                    print("Congratulations your loan has APPROVED!!!")
                    print()
                    print("Your Loan Statement is as Follows:- ")
                    print("Name: ",nam)
                    print("Type of Loan: ",typ)
                    print("Loan Amount: ",loanamt)
                    print("Duration: ",dura)
                    print("Rate of Interest: ",roi)
                    print("Frequency: ",frequ)
                    print()
                    print("Instl Num","\t","Open Prin","\t\t","EMI","\t\t\t","Principal","\t\t","Interest","\t\t","Clos Prin","\t\t","Rate")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    mc.execute("Select * from LoanState")
                    table = mc.fetchall()
                    for row in table:
                        no = row[0]
                        opnprin = row[1]
                        EMI = row[2]
                        prin = row[3]
                        ints = row[4]
                        clsprin = row[5]
                        rate = row[6]
                        print(no,"\t\t",opnprin,"\t\t",EMI,"\t\t",prin,"\t\t",ints,"\t\t",clsprin,"\t\t",rate)
                    mc.execute("Select sum(EMI),sum(Principal),sum(Interest_Amt) from LoanState")
                    total = mc.fetchall()
                    for row in total:
                        totEMI = row[0]
                        totPrin = row[1]
                        totInt = row[2]
                    print("---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Total: ","\t\t","\t\t",totEMI,"\t\t",totPrin,"\t\t",totInt)
            else:
                print("Loan not APPROVED!!!")
    elif ch2 == 6:
        custclose.close(mc)
    else:
        print("Invalid Choice")
elif ch1 == 2:
    psw = input("Enter Password: ")
    if psw == 'BANK':
        print('''1. Customer Details
2. Transaction Details
3. FD Account Details
4. Fund Transfer Details
5. Loan Details''')
        ch2 = int(input("Enter your choice: "))
        if ch2 == 1:
            acno = int(input("Enter Account Number: "))
            mc.execute("Select * from AccDetails where Acc_no = {}".format(acno))
            table = mc.fetchall()
            if table == [] or table == ():
                print("Record not found!!!")
            else:
                print("Acc_type"," "*5,"Acc_No"," "*5,"Name"," "*4,"UID_No"," "*7,"Guar"," "*4,"Member"," "*4,"DOB"," "*8,"Gen"," "*5,"Mar"," "*5,"Address"," "*5,"Mob_No")
                for row in table:
                    typ = row[0]
                    accno = row[1]
                    name = row[2]
                    uid = row[3]
                    guar = row[4]
                    mem = row[5]
                    dob = row[6]
                    gen = row[7]
                    mar = row[8]
                    add = row[9]
                    mob = row[10]
                    print(typ," "*7,accno," "*5,name," "*4,uid," "*3,guar," "*3,mem," "*5,dob," "*2,gen," "*4,mar," "*4,add," "*4,mob)
        elif ch2 == 2:
            acno = int(input("Enter Account Number: "))
            mc.execute("Select * from Transaction where Acc_no = {}".format(acno))
            table = mc.fetchall()
            print("Acc_No","\t","Holder","\t","Type","\t\t","DepAmt","\t","Withdraw","\t","Bal")
            for row in table:
                accno = row[0]
                hold = row[1]
                typ = row[2]
                depamt = row[3]
                wthamt = row[4]
                bal = row[5]
                print(accno,"\t",hold,"\t",typ,"\t",depamt,"\t",wthamt,"\t\t",bal)
        elif ch2 == 3:
            acno = int(input("Enter Account Number: "))
            mc.execute("Select * from FDacc where Acc_no = {}".format(acno))
            table = mc.fetchall()
            print("Acc_No","\t","Holder","\t","DepAmt","\t","Duration","\t","ROI","\t","Bal")
            for row in table:
                accno = row[0]
                hold = row[1]
                depamt = row[2]
                dur = row[3]
                roi = row[4]
                bal = row[5]
                print(accno,"\t",hold,"\t",depamt,"\t",dur,"\t",roi,"\t",bal)
        elif ch2 == 4:
            acno = int(input("Enter Account Number: "))
            mc.execute("Select * from FundTransfer where Acc_no_Sender = {}".format(acno,acno))
            table = mc.fetchall()
            print("Acc_NoSend","\t","Acc_NoReceive","\t","TransAmt","\t","TransMode","\t","Charge","\t","NetTrans")
            for row in table:
                accnoS = row[0]
                accnoR = row[1]
                TraAmt = row[2]
                TraMod = row[3]
                chrg = row[4]
                NetTrans = row[5]
                print(accnoS,"\t\t",accnoR,"\t\t",TraAmt,"\t",TraMod,"\t\t",chrg,"\t",NetTrans)
        elif ch2 == 5:
            name = input("Enter Customer Name: ")
            mc.execute("Select * from Loan where Customer_Name like '{}'".format(name.upper()))
            table = mc.fetchall()
            print("Name","\t","Type","\t","Civil_Chrg","\t","Loan_Amt","\t","Duration","\t","ROI","\t","Frequency")
            for row in table:
                name = row[0]
                typ = row[1]
                civchr = row[2]
                loanamt = row[3]
                dur = row[4]
                roi = row[5]
                freq = row[6]
                print(name,"\t",typ,"\t",civchr,"\t",loanamt,"\t",dur,"\t",roi,"\t",freq)
        else:
            print("Invalid Choice")
    else:
        print("Invalid Password")
elif ch1 == 3:
    print("------Thank You-------")
else:
    print("Invalid Choice")
con.close()
