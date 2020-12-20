#EXERCISE--5, Health Management System
#ques-->3 clients- harry,rohan,hammad
# write a function that when executed takes as input client name
try:
   list=["harryfood.txt","harryEXR.txt","rohanfood.txt","rohanEXR.txt","hammadfood.txt","hammadEXR.txt"]
   for item in list:
      f=open(item,"x")
      f.close()
except Exception as e:
              print("\n")
def getdate():
    import datetime
    return datetime.datetime.now()
actiontime=getdate()
while(1):
    print("For which person you want details\nPRESS-\n1 for Harry\n2 for Rohan\n3 for Hammad")
    candidateinp = int(input())
    if candidateinp == 1:
        print("Which file you want to modify for Harry \n PRESS-\n 1 for FOOD\t\t\t\t 2 for EXCERCISE")
        fileinp = int(input())
        if fileinp == 1:
            print("Enter food Harry had eaten-->")
            foodinp = input()
            f = open("harryfood.txt", "a")
            strtime=str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(foodinp)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("harryfood.txt", "r")
            print(f.read())
            f.close()
        elif fileinp < 1 or fileinp > 2:
            print("invalid input")
        else:
            print("Enter exercise Harry performed")
            exercise = input()
            f = open("harryEXR.txt", "r+")
            strtime = str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(exercise)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("harryEXR.txt", "r")
            print(f.read())
            f.close()
    if candidateinp == 2:
        print("Which file you want to modify for Rohan \n PRESS-\n 1 for FOOD\t\t\t\t 2 for EXCERCISE")
        fileinp = int(input())
        if fileinp == 1:
            print("Enter food Rohan had eaten-->")
            foodinp = input()
            f = open("rohanfood.txt", "a")
            strtime = str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(foodinp)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("rohanfood.txt", "r")
            print(f.read())
            f.close()
        elif fileinp < 1 or fileinp > 2:
            print("invalid input")
        else:
            print("Enter exercise Rohan performed")
            exercise = input()
            f = open("rohanEXR.txt", "r+")
            strtime = str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(exercise)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("rohanEXR.txt", "r")
            print(f.read())
            f.close()
    if candidateinp == 3:
        print("Which file you want to modify for Hammad \n PRESS-\n 1 for FOOD\t\t\t\t 2 for EXCERCISE")
        fileinp = int(input())
        if fileinp == 1:
            print("Enter food Hammad had eaten-->")
            foodinp = input()
            f = open("hammadfood.txt", "a")
            strtime = str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(foodinp)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("hammadfood.txt", "r")
            print(f.read())
            f.close()
        elif fileinp < 1 or fileinp > 2:
            print("invalid input")
        else:
            print("Enter exercise Hammad performed")
            exercise = input()
            f = open("hammadEXR.txt", "r+")
            strtime = str(actiontime)
            f.write(strtime)
            f.write("\t\t\t")
            f.write(exercise)
            f.close()
            print("Database modified success fully\n Changes made are shown below in the file")
            f = open("hammadEXR.txt", "r")
            print(f.read())
            f.close()
    print("Do want to again add any entry Press\n Y to add again\t\t\t N to exit ")
    again=input()
    if again=="y" or again=="Y":
        print("OK add again")
    else:
        break









