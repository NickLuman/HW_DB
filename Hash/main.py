from hash_functions import hasher, rehasher
from hash import Hash


if __name__ == '__main__':
    hash_table = Hash()

    ### ADDING ### 
    hash_table['hwefng'] = 14
    hash_table[1414] = '6mtgrmfeq'
    hash_table[['yhrteg', 'rg', 414, 4]] = ['424r', 'y46', 43]
    hash_table[1.653] = 31524
    hash_table[100.001] = ['tegrweqfrv', 524, 14.5]
    hash_table['tgw'] = 14.00000001


    ### SEARCHING ###
    print(hash_table['hwefng'], hash_table[1414], hash_table[['yhrteg', 'rg', 414, 4]])
    print(hash_table['gbe']) # nonexistent key

    ### REMOVAL ### 
    hash_table.delete(1414)
    hash_table.delete(['yhrteg', 'rg', 414, 4])
    print(hash_table['hwefng'], hash_table[1414], hash_table[['yhrteg', 'rg', 414, 4]])
    


