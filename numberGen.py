import time
import os
from lib import *

options =("\nEnter the state code to create phone_number wordlist\n"
                  "\nstate codes : \n"
                  "\t code : 'AP'  -  state : AndhraPradesh&Telangana\n"
                  "\t code : 'AS'  -  state : Assam\n"
                  "\t code : 'BR'  -  state : Bihar&Jharkhand \n"
                  "\t code : 'DL'  -  state : Delhi\n"
                  "\t code : 'GJ'  -  state : Gujarat\n"
                  "\t code : 'HP'  -  state : HimachalPradesh\n"
                  "\t code : 'HR'  -  state : haryana\n"
                  "\t code : 'JK'  -  state : Jammu&Kashmir\n"
                  "\t code : 'KL'  -  state : Kerala&Lakshadweep\n"
                  "\t code : 'KA'  -  state : Karnataka\n"
                  "\t code : 'KO'  -  state : Kolkata\n"
                  "\t code : 'MH'  -  state : Maharashtra&Goa\n"
                  "\t code : 'MP'  -  state : MadhyaPradesh&Chhattisgarh\n"
                  "\t code : 'MU'  -  state : Mumbai\n"
                  "\t code : 'NE'  -  state : NortEast\n"
                  "\t code : 'OR'  -  state : Odisha\n"
                  "\t code : 'PB'  -  state : Punjab\n"
                  "\t code : 'RJ'  -  state : Rajasthan\n"
                  "\t code : 'TN'  -  state : TamilNadu\n"
                  "\t code : 'UE'  -  state : UPEast\n"
                  "\t code : 'UW'  -  state : UPWest\n"
                  "\t code : 'WB'  -  state : WestBengal\n"
          "  Make sure the code is in 'UpperCase' \n"
          "  Enter code  : "
          )




def generator(f,f1):

    print("\npreparing to generator wodllist\n")
    time.sleep(0.5)

    print("\t please wait\n")

    time.sleep(0.2)

    print("\t please wait.\n")

    time.sleep(0.2)

    print("\t please wait..\n")

    time.sleep(0.2)

    print("\t please wait...\n")

    time.sleep(0.5)

    lines = f.readlines()
    totalLines = len(lines)

    j = 0
    l = 1

    for i in lines:

        for j in range(100000, 999999):

           f1.write(str(i).strip() + str(j) + "\n")

           print(str(i).strip() + str(j) + "         Number Codes Left =" + str(totalLines - l))



def main():

    stateCode = input(options)

    if stateCode == 'AP':

        f = open('lib/AP_AndhraPradesh&Telangana.txt')

        f1 = open("AP_TS_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'AS':

        f = open('lib/AS_Assam.txt')

        f1 = open("AS_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")


    elif stateCode == 'BR':

        f = open('lib/BR_Bihar&Jharkhand.txt')

        f1 = open("BR_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'GJ':

        f = open('lib/GJ_Gujarat.txt')

        f1 = open("GJ_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'HP':

        f = open('lib/HP_HimachalPradesh.txt')

        f1 = open("HP_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'HR':

        f = open('lib/HR_Haryana.txt')

        f1 = open("HR_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'JK':

        f = open('lib/JK_Jammu&Kashmir.txt')

        f1 = open("JK_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'KL':

        f = open('lib/KL_Kerala&Lakshadweep.txt')

        f1 = open("KL_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'KA':

        f = open('lib/KA_Karnataka.txt')

        f1 = open("KA_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'KO':

        f = open('lib/KO_Kolkata.txt')

        f1 = open("KO_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'AS':

        f = open('lib/AS_Assam.txt')

        f1 = open("AS_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'MH':

        f = open('lib/MH_Maharashtra&Goa.txt')

        f1 = open("MH_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'MP':

        f = open('lib/MP_MadhyaPradesh&Chhattisgarh.txt')

        f1 = open("MP_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")


    elif stateCode == 'MU':
        f = open('lib/MU_Mumbai.txt')

        f1 = open("MU_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")


    elif stateCode == 'NE':

        f = open('lib/NE_NortEast.txt')

        f1 = open("NE_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'OR':

        f = open('lib/OR_Odisha.txt')

        f1 = open("OR_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'PB':

        f = open('lib/PB_Punjab.txt')

        f1 = open("PB_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'RJ':

        f = open('lib/RJ_Rajasthan.txt')

        f1 = open("RJ_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'TN':

        f = open('lib/TN_TamilNadu.txt')

        f1 = open("TN_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'UE':

        f = open('lib/UE_UPEast.txt')

        f1 = open("UE_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")


    elif stateCode == 'UW':

        f = open('lib/UW_UPWest.txt')

        f1 = open("UW_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    elif stateCode == 'WB':

        f = open('lib/WB_WestBengal.txt')

        f1 = open("WB_wordlist.txt", 'w')

        generator(f,f1)

        print("wordlist successfully created")

    else:


        print("\nError, Please check the state code and try again\n\n ")

        input("Press Any key  to continue...")

        main()


main()










