#Calculates the distance lightning is from a bystander
#by Matthew Tichenor

def main():
    print("This program determines how distant lightning is")
    sec = input("How long did it take (in sec) to hear the thunder? ")
    sec = float(sec)
    sound = 1100
    mile = 5280
    distance = sec * sound / mile
    print("The lightning strike was",distance,"miles away")

main()
