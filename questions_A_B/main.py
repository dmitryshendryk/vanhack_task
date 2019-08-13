import argparse


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
    
    if a > b: print(str(a) + ' > ' + str(b))
    elif a < b: print(str(a) + ' < ' + str(b))
    elif a == b: print(str(a) + ' == ' + str(b))
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
       description='Questions ')
    
    parser.add_argument('command',
                    metavar='<command>')

    args = parser.parse_args()

    if args.command == 'overlap':
        d = input('Write four numbers with spaces > ')
        data = [int(x) for x in d.split(' ')]
        assert len(data) == 4, '4 number should be inputed'

        if is_overlap((data[0],data[1]),(data[2],data[3])):
            print("x1,x2 and x3,x4 are ovelaping")
        else:
            print("x1,x2 and x3,x4 are NOT ovelaping")
    
    if args.command == 'version_compare':
        d = input('Write 2 numbers with spaces > ')
        data = [x for x in d.split(' ')]
        assert len(data) == 2, '2 number should be inputed'
        
        version_compare(data[0],data[1])

