#Temperature conversion
while True:
    unit=input("Enter the temperature format Celsius/Fahrenheit/Kelvin (C/F/K):").upper()
    temp=float(input("Enter the temperature:"))
    


    if(unit=="C"):
        F1=round((9*temp) /5 + 32,1)
        print(f"The temperature in fahrenheit is:{F1}°f")
        K1=round(temp+273.15,1)
        print(f"The temperature in kelvin is:{K1}k")
        

    elif(unit=="F"):
        C1=round((temp-32)/1.80,1)
        print(f"The temperature in celsius is:{C1}°c")
        K2=round((temp-32) * 5/9 + 273.15,1)
        print(f"The temperature in kelvin is:{K2}k")
        

    elif(unit=="K"):
        C2=round(temp-273.15,1)
        print(f"The temperature in celsius is:{C2}°c")
        F2=round(1.8*(temp-273)+32,1)
        print(f"The temperature in Fahrenheit is:{F2}°f")
        

    else:
        print(f" The {unit} is invalid")
        break


    
    

    
        
