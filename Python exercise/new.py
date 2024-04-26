hours = input("Enter hours rendered: ")
h = float(hours)

rate = input("Enter rate per hour: ")
x = float(rate)

if h <= 48:
    net_pay = h * x
    
    #rates
    sss_rate = 0.11
    philhealth_rate = 0.0275
    pagibig_rate = 0.02

    #deduct
    sss_deduction = net_pay * sss_rate
    philhealth_deduction = net_pay * philhealth_rate
    pagibig_deduction = net_pay * pagibig_rate

    # Compute for gross pay
    gross_pay = net_pay - sss_deduction - philhealth_deduction - pagibig_deduction

    print("Net Pay: ", net_pay)
    print("SSS Deduction: ", sss_deduction)
    print("PhilHealth Deduction: ", philhealth_deduction)
    print("Pag-IBIG Deduction: ", pagibig_deduction)
    print("Gross Pay: ", gross_pay)
else:
    print("Wrong input")
