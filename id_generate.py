from random import *

def generate():
    alpha = choice(range(26))
    ret = [choice([1,2])] + sample(range(10),7)
    chk = [ v*(8-i) for i,v in enumerate(ret) ]
    chk = int("10987654932210898765431320"[alpha]) + sum(chk)
    chk = (10-chk%10) % 10
    return chr(alpha+ord("A")) + ''.join(map(str,ret)) + str(chk)

if __name__ == '__main__':
    d = {}
    for i in range(0, 1000000):
        id_ = generate()[-4:]
        if id_ in d:
            d[id_] += 1
        else:
            d[id_] = 1
            
    print d
        
