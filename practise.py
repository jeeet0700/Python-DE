import random

def id_gen():
    return random.randint(1,10)

def name_gen():
    a=['janvi','sumit','amit','rohit','mohit']
    return random.choice(a)

def pos_gen():
    b=['sde','sde1','sde2','sde3']
    return random.choice(b)

def ver_gen():
    c=['v1','v2','v3']
    return random.choice(c)

for i in range(1,10):
    id=id_gen()
    name=name_gen()
    pos=pos_gen()
    ver=ver_gen()
    print(f"Insert into emp (id,name,position,version) values ({id},'{name}','{pos}','{ver}');")