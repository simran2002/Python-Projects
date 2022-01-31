def loan():
    nam = input("ENTER NAME : ")
    print("""1. Personal Loan
2. Home Loan
3. Education Loan
4. Business Loan
5. Vehicle Loan""")
    typ = int(input("ENTER YOUR CHOICE: "))
    print("""General Requirements:-
1. Address Proof
2. Tax Proof
3. Photo ID Proof
4. Processing Fees - Rs. 100/lakh + GST 18% (For All)
5. Documentation Fees - Rs. 400/lakh (Not For All)
6. If loan above 3 lakh then Processing Fees + Documentation Fees
General Criteria:-
1. Civil Charge should be in range 6 to 10""")
    if typ == 1:
        print("""Personal Loan - Criteria, Requirements, Interest & Duration:-
1. ITR(Income Tax Return) should be fullfilled
2. Interest - 18% p.a.
3. Duration - Maximum 5 years""")
        typ = "Personal"
        ROI = 18
    elif typ == 2:
        print("""Home Loan - Criteria, Requirements, Interest & Duration:-
1. ITR(Income Tax Return) should be fullfilled
2. Interest - 12% p.a.
3. Duration - 10, 20, 30 years""")
        typ = "Home"
        ROI = 12
    elif typ == 3:
        print("""Education Loan - Criteria, Requirements, Interest & Duration:-
1. Preferred to students who have applied for A - Grade colleges(such as IIM, IIT, etc)
2. No ITR(Income Tax Return) required
3. College addmission letter
4. College ID Proof
5. Fees Quotation from College
6. Parent's Income Proof
7. Interest - 10.5% p.a.
8. Duration - Maximum 5 to 10 years
        >>> EMI will start after Morotorian Period <<<
        (Monotorian Period - the period in which the do not pay any EMI
                    i.e. complete college years + 6 months)""")
        typ = "Education"
        ROI = 10.5
    elif typ == 4:
        print("""Business Loan - Criteria, Requirements, Interest & Duration:-
1. ITR(Income Tax Return) should be fullfilled
2. GST Number
3. CIN(Customer Identification Number)
4. Interest - 10% p.a.
5. No specific Duration""")
        typ = "Business"
        ROI = 10
    elif typ == 5:
        print("""Vehicle Loan - Criteria, Requirements, Interest & Duration:-
1. ITR(Income Tax Return) should be fullfilled
2. Interest - 8% p.a.
3. Duration - 7 years""")
        typ = "Vehicle"
        ROI = 8
    amt = int(input("LOAN AMOUNT : "))
    dur = int(input("DURATION(IN YEARS) : "))
    civchr = int(input("ENTER CIVIL CHARGE: "))
    print('''Choose Frequency:
1. Monthly
2. Quarterly
3. Half - Yearly
4. Yearly''')
    ch = int(input("Enter Frequency: "))
    if ch == 1:
        freq = 'MONTHLY'
    elif ch == 2:
        freq = 'QUARTERLY'
    elif ch == 3:
        freq = 'HALF - YEARLY'
    elif ch == 4:
        freq = 'YEARLY'
    st = '''Insert into Loan
values('{}','{}',{},{},{},{},'{}')'''.format(nam.upper(),typ,civchr,amt,dur,ROI,freq)
    return st,typ