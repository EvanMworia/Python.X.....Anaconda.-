while(True):
    try:
        fraction = input("Fraction: ")
        num = fraction.split("/")
        numerator = int(num[0])
        denominator = int(num[1])
        if(numerator <= denominator) and (denominator != 0):
            
            result = (numerator / denominator) * 100
            roundedResult = round(result)           
            if(roundedResult <= 1):
                print("E")
            elif (roundedResult >= 99):
                print("F")
            else:
                print(f"{roundedResult}%")      
            
            break
        else:
            print("Denomintor should not be zero or lesser than the numerator")
    except ValueError:
        print("Cannot convert your input to an integer")
