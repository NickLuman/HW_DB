def hasher(key, length) -> int:
    if type(key).__name__ == 'int':
        if key < 0:
            key %= length
        key <<= 2 
        bin_key = bin(key)[2:]
        hash_value = sum(list(map(lambda x: (int(x)<<1) + 1, bin_key)))
        return hash_value % length        
    elif type(key).__name__ == 'float':
        return (int(key) + hasher(str(key - int(key))[2:], length)) % length
    elif type(key).__name__ == 'str':
        return sum(list(map(lambda x: hasher(ord(x), length), list(key)))) % length
    elif type(key).__name__ == 'list':
        return sum(list(map(lambda x: hasher(x, length), key))) % length
    else: 
        print('Unfortunately, type: {} impossible to process by hasher'.format(type(key).__name__))


def rehasher(old_hash, length) -> int:
    return (old_hash + 1) % length
