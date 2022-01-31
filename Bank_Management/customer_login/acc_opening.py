def savacc():
    print("""Requirements for Opening Savings Account are:
>>OVD(Official Valid Documents)
1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)
2. ID Proof(Adhaar Card)
3. Tax Proof(Pan Card) ; School permission letter for student""")
    print("""Conditions for Savings Account are:
1. Minimum Balance Required - Rs.2,000 ; No minimum balance for student
2. Limited Transactions - upto Rs.50,000 at once
3. No Saving Interest given""")
    print("\t\t>>>FD(Fixed Deposit) Available<<<")
    print("---PLEASE FILL IN CAPITALS---")
    nam = input("ENTER NAME(MR./MRS.) : ")
    uid = int(input("10-DIGIT AADHAR NO. : "))
    guar = input("FATHER/HUSBAND/GUARDIAN NAME : ")
    dob = input("DATE OF BIRTH (YYYY/MM/DD): ")
    gen = input("GENDER(M/F/OTHER) : ")
    mar = input("MARITAL STATUS(MARRIED/SINGLE) : ")
    add = input("RESIDENTIAL ADDRESS : ")
    num = input("MOBILE NUMBER : ")
    st = '''INSERT INTO AccDetails(Type_of_acc,Acc_name,UID_no,Guar_name,DOB,Gender,Marital_Status,Address,Mob_No)
VALUES('{}','{}',{},'{}','{}','{}','{}','{}',{})'''.format('Saving',nam.upper(),uid,guar.upper(),dob,gen.upper(),mar.upper(),add.upper(),num)
    return st

    
def jointacc():
    print("""Requirements for Opening Joint Account are:
>>OVD(Official Valid Documents)(of all the members)
1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)
2. ID Proof(Adhaar Card)
3. Tax Proof(Pan Card)""")
    print("""Conditions for Joint Account are:
1. Minimum Balance Required - Rs.2,000
2. Limited Transactions - upto Rs.50,000 at once
3. No Saving Interest given""")
    print("\t\t>>>FD(Fixed Deposit) Available<<<")
    print("---PLEASE FILL IN CAPITALS---")
    nam = input("ENTER NAME(MR./MRS.) : ")
    uid = int(input("10-DIGIT AADHAR NO. : "))
    mem = input("MEMBER NAME : ")
    dob = input("DATE OF BIRTH (YYYY/MM/DD): ")
    add = input("RESIDENTIAL ADDRESS : ")
    num = input("MOBILE NUMBER : ")
    st = '''INSERT INTO AccDetails(Type_of_acc,Acc_name,UID_no,Member_name,DOB,Address,Mob_No)
VALUES('{}','{}',{},'{}','{}','{}',{})'''.format('Joint',nam.upper(),uid,mem.upper(),dob,add.upper(),num)
    return st


def curracc():
    print("""Requirements for Opening Current Account are:
>>OVD(Official Valid Documents)
1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)
2. ID Proof(Adhaar Card)
3. Tax Proof(Pan Card)""")
    print("""Conditions for Current Account(Normal) are:
1. Minimum Balance Required - Rs.5,000
2. Unlimited Transactions
3. No Saving Interest given""")
    print("\t\t>>>FD(Fixed Deposit) Available<<<")
    print("---PLEASE FILL IN CAPITALS---")
    nam = input("ENTER NAME(MR./MRS.) : ")
    uid = int(input("10-DIGIT AADHAR NO. : "))
    guar = input("FATHER/HUSBAND/GUARDIAN NAME : ")
    dob = input("DATE OF BIRTH (YYYY/MM/DD): ")
    gen = input("GENDER(M/F/OTHER) : ")
    mar = input("MARITAL STATUS(MARRIED/SINGLE) : ")
    add = input("RESIDENTIAL ADDRESS : ")
    num = input("MOBILE NUMBER : ")
    st = '''INSERT INTO AccDetails(Type_of_acc,Acc_name,UID_no,Guar_name,DOB,Gender,Marital_Status,Address,Mob_No)
VALUES('{}','{}',{},'{}','{}','{}','{}','{}',{})'''.format('Current',nam.upper(),uid,guar.upper(),dob,gen.upper(),mar.upper(),add.upper(),num)
    return st