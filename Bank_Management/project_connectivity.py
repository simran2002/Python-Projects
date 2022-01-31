#Program for connectivity
def connection():
    import mysql.connector
    con = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
    mc = con.cursor()
    #mc.execute("Drop database if exists BANK_MANAGEMENT")
    #mc.execute("Create database BANK_MANAGEMENT")
    mc.execute("Use TEST")
    #Account/Customer Details Table(Acc. Opening)
    mc.execute("Drop table if exists AccDetails")
    mc.execute("""Create table AccDetails
(Type_of_acc varchar(20),
Acc_No int primary key auto_increment,
Acc_Name varchar(30),
UID_No int(10),
Guar_Name varchar(30) default 'NULL',
Member_Name varchar(30) default 'NULL',
DOB date,
Gender varchar(5) default 'NULL',
Marital_Status varchar(10) default 'NULL',
Address varchar(100),
Mob_No int(10))""")
    #mc.execute("Alter table AccDetails auto_increment=1000")
    #Transaction Table
    mc.execute("Drop table if exists Transaction")
    mc.execute("""Create table Transaction
(Acc_No int(10) references AccDetails(Acc_No),
Holder_Name varchar(30),
Type_of_Acc varchar(20),
Dep_Amt decimal(10,2) default 0.00,
Withdrw_Amt decimal(10,2) default 0.00,
Bal_in_Acc decimal(10,2) default 0.00)""")
    #Table for FD Account
    mc.execute("Drop table if exists FDacc")
    mc.execute("""Create table FDacc
(Acc_No int primary key auto_increment,
Holder_Name varchar(30),
Dep_Amt decimal(10,2) default 0.00,
Duration integer(5) default 0,
ROI_per_duration decimal(10,2) default 0.00,
Bal_in_Acc decimal(10,2) default 0.00)""")
    #mc.execute("Alter table FDacc auto_increment=100")
    #Money/Fund Transfer Table
    mc.execute("Drop table if exists FundTransfer")
    mc.execute("""Create table FundTransfer
(Acc_No_Sender int(10) references AccDetails(Acc_No),
Acc_No_Receiver int(10),
Amt_to_Transfer decimal(10,2) default 0.00,
Mode_of_Transfer varchar(10),
Bank_Charge decimal(10,0) default 0.00,
Net_Amt_Transferred decimal(10,2) default 0.00)""")
    #Loan Details Table
    mc.execute("Drop table if exists Loan")
    mc.execute("""Create table Loan
(Customer_Name varchar(30),
Type_of_loan varchar(30),
Cust_Civil_Charge int(3),
Loan_Amt decimal(10,2) default 0.00,
Time_Duration int(5) default 0,
Rate_of_Interest decimal(10,2) default 0.00,
Frequency varchar(20) default 'Monthly')""")
    return con