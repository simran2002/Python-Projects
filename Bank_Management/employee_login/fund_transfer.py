# Fund Transfer
def FT1(accnoR,amttrf,accnoS,bankchr):                     #Received
    st1 = """Update Transaction
set Bal_in_Acc = Bal_in_Acc + {}
where Acc_No = {}""".format(amttrf,accnoR)
    st2 = """Update Transaction
set Bal_in_Acc = Bal_in_Acc - ({} + {})
where Acc_No = {}""".format(amttrf,bankchr,accnoS)             #Sent
    return st1,st2
def FT2(amttrf,accnoS,bankchr):                             
    st = """Update Transaction
set Bal_in_Acc = Bal_in_Acc - ({} + {})
where Acc_No = {}""".format(amttrf,bankchr,accnoS)             #Sent
    return st