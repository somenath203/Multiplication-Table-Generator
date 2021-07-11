
while(True):
    num = int(input("Enter a number whose multiplication table you want to see => "))
    limit = int(input("Enter the limit up to which you want to see the multiplication table => "))
    filename = input("enter the name of your txt file where the table will be inserted :- ")

    print("\n")

    print("Multiplication table of",num,"up to limit",limit,"is inserted inside the text file '"+filename+"'")

    with open(f"{filename}.txt",'w') as f:
        i = 1
        while(i<limit+1):
            f.write(f"{num} X {i} = {num*i}")
            if i!=limit:
                f.write("\n")
            i = i + 1
    
    print("Do you wan to generate one more multiplication table.? Press 'y' or 'Y' for YES or press any other key for NO.")
    choice = input()
    if(choice=='y' or choice=='Y'):
        continue
    else:
        print("Thanks for using our software. ALl the best for your carrer. We hope to see you again. Take care.")
        break
    