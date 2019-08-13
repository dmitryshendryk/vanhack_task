
def is_overlap(a,b):
    x1,x2 = a
    x3,x4 = b 
    return not (x2 < x3 or x4 < x1) 

def version_compare(a,b):
    assert a != "" and b != "", "Parameters cannot be empty"
    if len(a.split('.')) == 2:
        a = float(a)
    else:
        a = int(a)
    if len(b.split('.')) == 2:
        b = float(b)
    else:
        b = int(b)
    
    if a > b: print("a > b")
    elif a < b: print("a < b")
    elif a == b: print("a == b")
    


if __name__ == "__main__":
    print(is_overlap((1,5),(6,7)))
    version_compare('','2')

