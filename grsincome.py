grsincome= float(input("Enter gross income(in $):"))
if grsincome < 20000 :
    print("No need of income tax")
else:
    dep=int(input("Enter number of dependents:"))
    taxinc=(grsincome - 10000 -(dep*3000))
    print("Total taxable income=",taxinc)
    tax=taxinc*(8.8/100)
    print("Total income tax=",tax)
