def verfsavacc():
    print("Verify the following documents submitted by the customer for Opening a Savings Account:-")
    print(">>OVD(Official Valid Documents")
    ans1 = input("1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)[Y/N]: ")
    ans2 = input("2. ID Proof(Adhaar Card)[Y/N]: ")
    ans3 = input("3. Tax Proof(Pan Card) ; School permission letter for student[Y/N]: ")
    return ans1,ans2,ans3
def verfjntacc():
    print("Verify the following documents submitted by the customer for Opening a Joint Account:-")
    print(">>OVD(Official Valid Documents)(of all the members)")
    ans1 = input("1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)[Y/N]: ")
    ans2 = input("2. ID Proof(Adhaar Card)[Y/N]: ")
    ans3 = input("3. Tax Proof(Pan Card)[Y/N]: ")
    return ans1,ans2,ans3
def verfcurracc():
    print("Verify the following documents submitted by the customer for Opening a Current Account:-")
    print(">>OVD(Official Valid Documents)")
    ans1 = input("1. Address Proof(Electricity Bill, Adhaar Card, Voter-ID Card)[Y/N]: ")
    ans2 = input("2. ID Proof(Adhaar Card)[Y/N]: ")
    ans3 = input("3. Tax Proof(Pan Card)[Y/N]: ")
    return ans1,ans2,ans3