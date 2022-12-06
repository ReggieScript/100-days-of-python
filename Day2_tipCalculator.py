print("Welcome to the tip calculator.")
print("What was the total bill?")
bill= float(input("$"))
print("How many people will split the bill?")
split= int(input())
print("What tip percentage would you like to give?")
tip=int(input())/100

if split == 0:
    tip_mon=(bill*tip)#Individual Tip
    total=bill+tip_mon#Total Bill
    print("Tip $"+str(round(tip_mon,2)))
    print("Total bill including tip $"+str(round(total,2)))
else:
    tip_mon=(bill*tip)/split #Individual Tip
    total=bill+tip_mon*split #Total Bill
    total_per=(bill/split)+tip_mon #individual Pay

    print("Individual Tip $"+str(round(tip_mon,2)))
    print("Total bill per person $"+str(round(total_per,2)))
    print("Total bill including tip $"+str(round(total,2)))
