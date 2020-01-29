"""Given a string representing a simple fraction "x/y", function returns a string 
   representing the corresponding mixed fraction in the following format:

   [sign]a b/c

   Provide [sign] only if negative (and non zero) and only at the beginning of the number."""

def nwd(a,b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a
        
def mixed_fraction(s):
    x =  [int(z) for z in s.split("/")]
    minus = "-" if x[0]/x[1] < 0 else  ""
    
    ab = [abs(k) for k in x]
    integ = "" if int(ab[0]/ab[1]) == 0 else (minus + str(int(ab[0]/ab[1])))
    nww = nwd(ab[0],ab[1])
    rest = ab[0]%ab[1]

    if rest == 0:
        return integ if integ != "" else "0"
    elif integ == "" and nww != 0:
        return minus+str(int(rest/nww))+"/"+str(int(ab[1]/nww))
    elif nww == 0:
        return  integ+" "+str(rest)+"/"+str(int(ab[1]))
    else: 
        return integ+" "+str(int(rest/nww))+"/"+str(int(ab[1]/nww))
