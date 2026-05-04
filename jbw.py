def bread(func):
    def wrapper(*args, **kargs):
        print('✡✡✡✡✡✡✡✡✡')
        func(*args, **kargs)
        print('☪☪☪☪☪☪☪☪☪')
    
    return wrapper

def ingria(func):
    def wrapper(*args, **kargs):
        print('◼◼◼◼◼◼◼◼◼')
        func(*args, **kargs)
        print('🐮🐮🐮🐮')
    return wrapper

@bread
@ingria
def sandwitch(meat):
    print(meat)

sandwitch('🐷🐷🐷🐷')