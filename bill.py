amount=float (input ())
if amount>=5000:
   dis=(amount*10)/100
   tax=(amount*18)/100
    Print ("u r tax amount for the items"tax)
   Print ("u r discount is",dis)
   Print ("u have to pay is ", (amount-dis)+tax)
   Print ("visit again")
elif amount>=3000:
   dis=(amount*8)/100
   tax=(amount*10)/100
    Print ("u r tax amount for the items"tax)
   Print ("u r discount is",dis)
   Print ("u have to pay is ",( amount-dis)+tax)
   Print ("visit again")
elif amount>=2000:
    dis=(amount*5)/100
    tax=(amount*18)/100
    Print ("u r tax amount for the items"tax)
   Print ("u r discount is",dis)
   Print ("u have to pay is ", (amount-dis)-tax)
   Print ("visit again")
elif amount>=1000:
   dis=(amount*3)/100
    tax=(amount*18)/100
    Print ("u r tax amount for the items"tax)
   Print ("u r discount is",dis)
   Print ("u have to pay is ", amount-dis)
   Print ("visit again")
Else :
     tax=(amount*18)/100
    Print ("u r tax amount for the items"tax)
    Print ("no discount sry!!! Visit again! Bill is",tax+amount)
