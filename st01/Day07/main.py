for y in range(6):
    for x in range(6):
        if x==0 or x==5 or y==0 or y==5:
            print("O", end="")
        else:
            print(" ", end="")
    print()