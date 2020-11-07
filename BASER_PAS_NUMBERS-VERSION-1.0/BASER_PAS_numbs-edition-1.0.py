logo = '''
                            ██████╗  █████╗ ███████╗███████╗██████╗ 
                            ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
                            ██████╔╝███████║███████╗█████╗  ██████╔╝
                            ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔══██╗
                            ██████╔╝██║  ██║███████║███████╗██║  ██║
                            ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
   
                                      author: MearWix
                              version:BASER_PAS_numbs-edition_1.0


 #######################################################################################################
 |                                          WARNING!                                                   |
 |              THE RESULT WILL BE SAVED TO THE FOLDER WHERE IS THAT PROGRAM!                          |
 |              AUTHOR IS NOT RESPONSIBLE FOR HOW THIS PROGRAMM WILL BE USED!                          |
 |                                         GOOD LUCK!                                                  |
 #######################################################################################################

'''
print(logo)

pas = input("Enter your final number to make a base for brut: ")
first_num = 0
intPas = int(pas)
strPas = str(pas)
if (len(strPas) > 5):
    print("Sorry, we will not output generation of base here because this will freeze the process. \n")
print("Your base is generating now...")
if (len(strPas) > 5):
    print("It will take some time...")
f = open('base.txt', 'w')
while first_num <= intPas:
    strNum = str(first_num)
    strPas = str(pas)
    if (len(strNum) < len(strPas)):
        strNum = '0'*(len(strPas)-len(strNum)) + strNum
    if (len(strPas) <= 5):
        print(strNum)
    f.write(strNum+"\n")
    first_num = first_num + 1
f.close()
print("\n\nWell done! Your base for brut was saved to the file 'base.txt'. Good afternoon!")