def loancalc(freq,dur,lnamt,ROI,mc):
    mc.execute("Drop table if exists LoanState")
    mc.execute("""Create table LoanState
(Ins_No int primary key auto_increment,
Opening_Prin decimal(20,3) default 0.000,
EMI decimal(20,3) default 0.000,
Principal decimal(20,3) default 0.000,
Interest_Amt decimal(20,3) default 0.000,
Closing_Prin decimal(20,3) default 0.000,
Rate decimal(4,3) default 0.000)""")
    if freq == 'MONTHLY':
        instnum = 12*dur
        openprin = lnamt
        mthROI = ROI/1200
        mthEMI = round(((openprin*mthROI*((1+mthROI)**instnum))/(((1+mthROI)**instnum)-1)),2)
        while instnum > 0:
            mthIntamt = round(((openprin*mthROI)),2)
            mthPrinAmt = round((mthEMI - mthIntamt),2)
            closeprin = openprin-mthPrinAmt
            mc.execute('''Insert into LoanState(Opening_prin,EMI,Principal,Interest_Amt,Closing_Prin,Rate)
values({},{},{},{},{},{})'''.format(openprin,mthEMI,mthPrinAmt,mthIntamt,closeprin,ROI/12))
            mc.execute("Commit")
            openprin = closeprin
            instnum = instnum - 1
    elif freq == 'QUARTERLY':
        instnum = 3*dur
        openprin = lnamt
        quarROI = ROI/300
        quarEMI = round(((openprin*quarROI*((1+quarROI)**instnum))/(((1+quarROI)**instnum)-1)),2)
        while instnum > 0:
            quarIntamt = round(((openprin*quarROI)),2)
            quarPrinAmt = round((quarEMI - quarIntamt),2)
            closeprin = openprin-quarPrinAmt
            mc.execute('''Insert into LoanState(Opening_prin,EMI,Principal,Interest_Amt,Closing_Prin,Rate)
values({},{},{},{},{},{})'''.format(openprin,quarEMI,quarPrinAmt,quarIntamt,closeprin,ROI/3))
            mc.execute("Commit")
            openprin = closeprin
            instnum = instnum - 1
    elif freq == 'HALF - YEARLY':
        instnum = 2*dur
        openprin = lnamt
        halfROI = ROI/200
        halfEMI = round(((openprin*halfROI*((1+halfROI)**instnum))/(((1+halfROI)**instnum)-1)),2)        
        while instnum > 0:
            halfIntamt = round(((openprin*halfROI)/100),2)
            halfPrinAmt = round((halfEMI - halfIntamt),2)
            closeprin = openprin-halfPrinAmt
            mc.execute('''Insert into LoanState(Opening_prin,EMI,Principal,Interest_Amt,Closing_Prin,Rate)
values({},{},{},{},{},{})'''.format(openprin,halfEMI,halfPrinAmt,halfIntamt,closeprin,ROI/2))
            mc.execute("Commit")
            openprin = closeprin
            instnum = instnum - 1
    elif freq == 'YEARLY':
        instnum = dur
        openprin = lnamt
        yearROI = ROI/100
        yearEMI = round(((openprin*yearROI*((1+yearROI)**instnum))/(((1+yearROI)**instnum)-1)),2)                
        while instnum > 0:
            yearIntamt = round(((openprin*yearROI)/100),2)
            yearPrinAmt = round((yearEMI - yearIntamt),2)
            closeprin = openprin-yearPrinAmt
            mc.execute('''Insert into LoanState(Opening_prin,EMI,Principal,Interest_Amt,Closing_Prin,Rate)
values({},{},{},{},{},{})'''.format(openprin,yearEMI,yearPrinAmt,yearIntamt,closeprin,ROI))
            mc.execute("Commit")
            openprin = closeprin
            instnum = instnum - 1

