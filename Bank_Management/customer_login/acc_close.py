def close(mc):
    accno = int(input("ENTER YOUR ACCOUNT NO. : "))
    mc.execute("Select * from AccDetails")
    table = mc.fetchall()
    for row in table:
        acno = row[1]
        if accno == acno:
            mc.execute("DELETE FROM AccDetails WHERE Acc_No = {}".format(accno))
            mc.execute("Commit")
            print("Account Deleted successfully!!!")
        else:
            continue