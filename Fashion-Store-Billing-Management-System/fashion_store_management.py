print("---------------------WELCOME To FASHION STORE-----------------------")
print("What do you want to buy?")
L = "Ladies' Wear"
M = "Mens' Wear"
K = "Kids' Wear"
Ac = "Accessories"
print("1. ", L)
print("2. ", M)
print("3. ", K)
print("4. ", Ac)
answer = "Y"
answer2 = "Y"
mrpl = mrpm = mrpk = mrpa = mrpj = 0
disl = dism = disk = disa = disj = 0
amtl = amtm = amtk = amta = amtj = 0
ans1 = ans2 = ans3 = ans4 = ans5 = "Y"
ans1 = ans2 = ans3 = ans4 = ans5 = "y"
totall = totalm = totalk = totala = totalj = total = 0
bill = []
qty = 0
quantity,quantityj = 0,0
disctotal =0
mrptotal = 0
while answer == 'y' or answer == 'Y':
     option = input("Please select any category: ")
     if option == '1':
          print("What would you like to buy in Ladies' Wear?")
          A,mrpA = "Tops, Tees and Shirts",550
          B,mrpB = "Shorts and Skirts",750
          C,mrpC = "Jeans and Trousers",800
          D,mrpD = "Suits",900
          E,mrpE = "Formal Wear",600
          F,mrpF = "Sarees",700
          G,mrpG = "Lehnga, Gowns and Dresses",1200
          print("    Items", "\t \t \t \t \t", "Price")
          print("    -----------------------------------------------------------")
          print("A. ", A, "\t \t \t Rs.",mrpA)
          print("B. ", B, "\t \t \t \t Rs.",mrpB)
          print("C. ", C, "\t \t \t \t Rs.",mrpC)
          print("D. ", D, "\t \t \t \t \t Rs.",mrpD)
          print("E. ", E, "\t \t \t \t Rs.",mrpE)
          print("F. ", F, "\t \t \t \t \t Rs.",mrpF)
          print("G. ", G, "\t \t \t Rs.",mrpG)
          print("\t","There is 15% discount on every ladies' wear")
          ans1 = 'y'
          while ans1 == "y" or ans1 == "Y":
               option2 = input("Please select any ladies' wear: ")
               if option2 == 'A' or option2 == 'B' or option2 == 'C' or option2 == 'D' or option2 == 'E' or option2 == 'F' or option2 == 'G' or option2 == 'a' or option2 == 'b' or option2 == 'c' or option2 == 'd' or option2 == 'e' or option2 == 'f' or option2 == 'g':
                    qty = int(input("Please specify quantity: "))
                    if option2 == "A" or option2 == "a":
                         mrpl = mrpA
                         option2 = "Tp/T/Shrt"
                    elif option2 == "B" or option2 =="b":
                         mrpl = mrpB
                         option2 = "Shrt/skrt"
                    elif option2 == "C" or option2 =="c":
                         mrpl = mrpC
                         option2 = "Jns/Trsr "
                    elif option2 == "D" or option2 =="d":
                         mrpl = mrpD
                         option2 = "Suit     "
                    elif option2 == "E" or option2 =="e":
                         mrpl = mrpE
                         option2 = "F-Wr     "
                    elif option2 == "F" or option2 =="f":
                         mrpl = mrpF
                         option2 = "Saree    "
                    elif option2 == "G" or option2 =="g":
                         mrpl = mrpG
                         option2 = "Lh/Gw/Drs"
                    totall = (mrpl*qty)
                    disl = mrpl*(15/100)*qty
                    amtl = totall - disl
                    total += amtl
                    disctotal += disl
                    quantity += qty
                    mrptotal += totall
                    option = "LW"
                    ctgr = option
                    itm = option2
               else:
                    print("Invalid Entry")
               ans1 = input("Do you want to buy any other ladies' wear? (Y/N) : ")
               bill.append([ctgr,itm.upper(),qty,mrpl,disl,amtl])
               
          else:
               answer = input("Do you want to buy any other item from our Fashion Store? (Y/N): ")
     elif option == '2':
          print("What would you like to buy in Mens' Wear?")
          Pm,mrpPm = "Formal Pants",650
          Sm,mrpSm = "Trousers",550
          Jem,mrpJem = "Jeans",500
          CPm,mrpCPm = "Blazers",1000
          Jam,mrpJam = "Jackets",800
          SGm,mrpSGm = "Shirts and T - Shirts",750
          print("    Items", "\t \t \t \t \t", "Price")
          print("    -----------------------------------------------------------")
          print("A. ", Pm, "\t \t \t \t Rs.",mrpPm)
          print("B. ", Sm, "\t \t \t \t \t Rs.",mrpSm)
          print("C. ", Jem, "\t \t \t \t \t Rs.",mrpJem)
          print("D. ", CPm, "\t \t \t \t \t Rs.",mrpCPm)
          print("E. ", Jam, "\t \t \t \t \t Rs.",mrpJam)
          print("F. ", SGm, "\t \t \t Rs.",mrpSGm)
          print("\t","There is 10% discount on every mens' wear")
          ans2 = 'y'
          while ans2 == "y" or ans2 == "Y":
               option2 = input("Please select any mens wear: ")
               if option2 == 'A' or option2 == 'B' or option2 == 'C' or option2 == 'D' or option2 == 'E' or option2 == 'F' or option2 == 'a' or option2 == 'b' or option2 == 'c' or option2 == 'd' or option2 == 'e' or option2 == 'f':
                    qty = int(input("Please specify quantity: "))
                    if option2 == "A" or option2 == "a":
                         mrpm = mrpPm
                         option2 = "F-Pant   "
                    elif option2 == "B" or option2 =="b":
                         mrpm = mrpSm
                         option2 = "Trsr     "
                    elif option2 == "C" or option2 =="c":
                         mrpm = mrpJem
                         option2 = "Jns      "
                    elif option2 == "D" or option2 =="d":
                         mrpm = mrpCPm
                         option2 = "Blazer   "
                    elif option2 == "E" or option2 =="e":
                         mrpm = mrpJam
                         option2 = "Jkt      "
                    elif option2 == "F" or option2 =="f":
                         mrpm = mrpSGm
                         option2 = "S/T-Shrt "
                    totalm = (mrpm*qty)
                    dism = mrpm*(10/100)*qty
                    amtm = totalm - dism
                    total += amtm
                    disctotal += dism
                    quantity += qty
                    mrptotal += totalm
                    option="MW"
                    ctgr = option
                    itm = option2
               else:
                    print("Invalid Entry")
               ans2 = input("Do you want to buy any other mens' wear? (Y/N) : ")
               bill.append([ctgr,itm.upper(),qty,mrpm,dism,amtm])
          else:
               answer = input("Do you want to buy any other item from our Fashion Store? (Y/N): ")
     elif option == '3':
          print("What would you like to buy in Kids' Wear?")
          Tk,mrpTk = "Tops for Girls",550
          Sk,mrpSk = "Trousers",400
          Jek,mrpJek = "Jeans for Girls/Boys",500
          Pk,mrpPk = "Party Wear for Girls/Boys",600
          Jak,mrpJak = "Jackets",700
          Skk,mrpSkk = "Shirts and T - Shirts",650
          print("    Items", "\t \t \t \t \t", "Price")
          print("    -----------------------------------------------------------")
          print("A. ", Tk, "\t \t \t \t Rs.",mrpTk)
          print("B. ", Sk, "\t \t \t \t \t Rs.",mrpSk)
          print("C. ", Jek, "\t \t \t Rs.",mrpJek)
          print("D. ", Pk, "\t \t \t Rs.",mrpPk)
          print("E. ", Jak, "\t \t \t \t \t Rs.",mrpJak)
          print("F. ", Skk, "\t \t \t Rs.",mrpSkk)
          print("\t","There is 20% discount on every kids' wear")
          ans3 = 'y'
          while ans3 == "y" or ans3 == "Y":
               option2 = input("Please select any kids wear: ")
               if option2 == 'A' or option2 == 'B' or option2 == 'C' or option2 == 'D' or option2 == 'E' or option2 == 'F' or option2 == 'a' or option2 == 'b' or option2 == 'c' or option2 == 'd' or option2 == 'e' or option2 == 'f':
                    qty = int(input("Please specify quantity: "))
                    if option2 == "A" or option2 == "a":
                         mrpk = mrpTk
                         option2 = "G-Top    "
                    elif option2 == "B" or option2 =="b":
                         mrpk = mrpSk
                         option2 = "Trsr     "
                    elif option2 == "C" or option2 =="c":
                         mrpk = mrpJek
                         option2 = "G/B-Jns  "
                    elif option2 == "D" or option2 =="d":
                         mrpk = mrpPk
                         option2 = "P-Wr     "
                    elif option2 == "E" or option2 =="e":
                         mrpk = mrpJak
                         option2 = "Jkt      "
                    elif option2 == "F" or option2 =="f":
                         mrpk = mrpSkk
                         option2 = "S/T-Shrt "
                    totalk = (mrpk*qty)
                    disk = mrpk*(20/100)*qty
                    amtk = totalk - disk
                    total += amtk
                    disctotal += disk
                    quantity += qty
                    mrptotal += totalk
                    option = "KW"
                    ctgr = option
                    itm = option2
               else:
                    print("Invalid Entry")
               ans3 = input("Do you want to buy any other kids' wear? (Y/N) : ")
               bill.append([ctgr,itm.upper(),qty,mrpk,disk,amtk])
          else:
               answer = input("Do you want to buy any other item from our Fashion Store? (Y/N): ")
     elif option == '4':
          print("What Accessories would you like to buy?")
          Go,mrpGo = "Trolley Bags",2000
          So,mrpSo = "Ties and Socks",250
          J1,mrpJ1 = "Earrings",100
          J2,mrpJ2 = "Bracelets",150
          J3,mrpJ3 = "Rings",75
          Ho,mrpHo = "Handkerchiefs",150
          Bo,mrpBo = "Handbags and Bagpacks",850
          Co,mrpCo = "Slippers and Gloves",150
          Slo,mrpSlo = "Caps",50
          print("    Items", "\t \t \t \t \t", "Price")
          print("    -----------------------------------------------------------")
          print("A. ", Go, "\t \t \t \t Rs.",mrpGo)
          print("B. ", So, "\t \t \t \t Rs.",mrpSo)
          print("C. ","Jewellery:-","\t \t \t \t \t")
          print("\t","C1. ",J1, "\t \t \t \t Rs.",mrpJ1)
          print("\t","C2. ",J2, "\t \t \t Rs.",mrpJ2)
          print("\t","C3. ",J3, "\t \t \t \t Rs.",mrpJ3)
          print("D. ", Ho, "\t \t \t \t Rs.",mrpHo)
          print("E. ", Bo, "\t \t \t Rs.",mrpBo)
          print("F. ", Co, "\t \t \t Rs.",mrpCo)
          print("G. ", Slo, "\t \t \t \t \t Rs.",mrpSlo)
          print("\t","You have 25% discount on every Accessory")
          ans4 = 'y'
          while ans4 == "y" or ans4 == "Y":
               option2 = input("Please select any Accessory: ")
               if option2 == 'A' or option2 == 'B' or option2 == 'C1' or option2 == 'C2' or option2 == 'C3' or option2 == 'D' or option2 == 'E' or option2 == 'F' or option2 == 'G' or option2 == 'a' or option2 == 'b' or option2 == 'c1' or option2 == 'c2' or option2 == 'c3' or option2 == 'd' or option2 == 'e' or option2 == 'f' or option2 == 'g':
                    qty = int(input("Please specify quantity: "))
                    if option2 == "A" or option2 == "a":
                         mrpa = mrpGo
                         option2 = "Trolley  "
                    elif option2 == "B" or option2 =="b":
                         mrpa = mrpSo
                         option2 = "Tie/Sock "
                    elif option2 == "C1" or option2 =="c1":
                         mrpa = mrpJ1
                         option2 = "E-ring   "
                    elif option2 == "C2" or option2 =="c2":
                         mrpa = mrpJ2
                         option2 = "Brclt    "
                    elif option2 == "C3" or option2 =="c3":
                         mrpa = mrpJ3
                         option2 = "Ring     "
                    elif option2 == "D" or option2 =="d":
                         mrpa = mrpHo
                         option2 = "Hanky    "
                    elif option2 == "E" or option2 =="e":
                         mrpa = mrpBo
                         option2 = "H-bag    "
                    elif option2 == "F" or option2 =="f":
                         mrpa = mrpCo
                         option2 = "Sli/Glov "
                    elif option2 == "G" or option2 =="g":
                         mrpa = mrpSlo
                         option2 = "Cap      "
                    totala = (mrpa*qty)
                    disa = mrpa*(25/100)*qty
                    amta = totala - disa
                    total += amta
                    disctotal += disa
                    quantity += qty
                    mrptotal += totala
                    option="AC"
                    ctgr = option
                    itm = option2
               else:
                    print("Invalid Entry")
               ans4 = input("Do you want to buy any other Accessory? (Y/N) : ")
               bill.append([ctgr,itm.upper(),qty,mrpa,disa,amta])
          else:
               answer = input("Do you want to buy any other item from our Fashion Store? (Y/N): ")
     else:
          print("Invalid Entry")
print("--------------------------------YOUR BILL--------------------------------")
print("Ctgr \t   Itm \t \t   Qty \t   MRP \t   Dis \t \t   Amt")
for i in range(len(bill)):
     for j in range(len(bill[i])):
          print(bill[i][j], end="\t   ")
     print()
print("=======================================================================")
print("Total =","\t \t  ",quantity,"\t  ", mrptotal,"  ", disctotal,"         ", total)
print("=======================================================================")
if total>2000:
     print('''Congratulations !!!!
          You will get extra 20% discount on your shopping of above Rs.2000.''')
     netamt = total - (total*20/100)
     print("Amount payable = Rs. ", netamt)
else:
     print("Amount payable = Rs. ", round(total,0))
print("Thanks for shopping with us...... :-)")