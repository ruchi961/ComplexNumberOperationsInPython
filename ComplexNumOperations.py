
import sys
import matplotlib.pyplot as plt

S={1+1j}
S1={2+3j,4+5j}
while True:
    
    print("Menu\n1. Addition of complex Number\n2. Conjugate of a complex number\n3. Plotting a complex numbers\n4. Translaing a complex Number\n5. Rotating complex number by a degree for eg :-  90, 180, 270\n6. Scaling by a complex number  by float number\n7. Exit")
    opt=int(input("Enter the operation you want to perform : "))
    if opt==1:
        no1=complex(input("Enter the first complex Number : " ))
        no2=complex(input("Enter the Second complex Number : " ))
        v_sum=no1+no2
        print("The sum of the complex Numbers ",no1," and ",no2," is ",v_sum)
    elif opt==2:
        no1=complex(input("Enter a complex Number : " ))
        conju=no1.conjugate()
        print("The conjugate of the complex Numbers ",no1," is ",conju)

    elif opt==3:
        X=[x.real for x in S1]
        Y=[y.imag for y in S1]
        plt.plot(X,Y,"gs")
        plt.axis([-7,+7,-7,+7])
        plt.show()
    elif opt==4:
        t=complex(input("Enter complex number : "))
        plot=[x+t for x in S1]
        print(plot)
        X=[x.real for x in plot]
        Y=[y.imag for y in plot]
        plt.plot(X,Y,"ro")
        plt.axis([-6,+6,-6,+6])
        plt.show()
    elif opt==5:
        d=int(input("Enter the degree to rotate eg : - 90, 180,270 : "))
        if d==90:
            plot=[x*1j for x in S]
            print(plot)
        elif d==180:
            plot=[x*-1 for x in S]
            print(plot)
        elif d==270:
            plot=[x*-1j for x in S]
            print(plot)
        X=[x.real for x in plot]
        Y=[y.imag for y in plot]
        plt.plot(X,Y,"ro")
        plt.axis([+3,-3,+3,-3])
        plt.show()
    elif opt==6:
        scaled=float(input("Enter scaling factor: "))
        plot={x*scaled for x in S1}
        print(plot)
        X=[x.real for x in plot]
        Y=[y.imag for y in plot]
        plt.plot(X,Y,"ro")
        plt.axis([-6,+6,-6,+6])
        plt.show()

    elif opt==7:
        print("Exiting......")
        sys.exit()

    else:
        print("Please enter appropriate option ")
    conti=input("Do you want to continue y/n : ")
    if conti!="y" and conti!="Y":
        break
    
