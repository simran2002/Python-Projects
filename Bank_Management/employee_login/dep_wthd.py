# Deposit
def depst1(accno,depamt):
    st = "UPDATE TRANSACTION SET BAL_IN_ACC = BAL_IN_ACC + {} WHERE ACC_NO = {}".format(depamt,accno)
    return st
def depst2(accno,depamt):
    st = "UPDATE FDacc SET BAL_IN_ACC = BAL_IN_ACC + {} WHERE ACC_NO = {}".format(depamt,accno)
    return st
# Withdraw
def withdrw1(accno,wthdrwamt):
    st = "UPDATE TRANSACTION SET BAL_IN_ACC = BAL_IN_ACC - {} WHERE ACC_NO = {}".format(wthdrwamt,accno)
    return st
def withdrw2(accno,depamtFD,roi):
    st = "UPDATE FDacc SET BAL_IN_ACC = BAL_IN_ACC - ({} + {}*({}/100)) WHERE ACC_NO = {}".format(depamtFD,depamtFD,roi,accno)
    return st