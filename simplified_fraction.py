def sort_list(ls):
  b = 1
  while b:
    b = 0
    for a in range(0,len(ls)-1):
      if ls[a] > ls[a+1]:
        ls[a], ls[a+1] = ls[a+1], ls[a]
        b = 1
  return ls

def get_factors(x):
    i=1
    r=[]
    while (i <= x//i):
        if (x%i == 0):
            r.append(i)
            (i != x//i) and r.append(x//i)
        i+=1
    return r

# params (f) a fraction represented as a string e.g. "3/12"
def simplified_fraction(f):
    n = int(f.split("/")[0])
    d = int(f.split("/")[1])
    d_factors = get_factors(d)
    d_factors_sorted = sort_list(d_factors)
    lcd = 1
    for factor in d_factors_sorted:
        if n % factor == 0:
            lcd = factor
    return str(int(n/lcd)) + "/" + str(int(d/lcd))

# ------------------------- test -------------------------

a = ["2/4", "3/12", "24/6", "3/17", "42/56", "98/265", "238/6584", "33423/658236", "83183840/23985", "-5/5", "-32/912", "-124/548"]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n\nsimplified_fraction: " + str(simplified_fraction(i)))
input()