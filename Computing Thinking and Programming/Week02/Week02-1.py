def rev_str(str):
    if len(str) <= 1:
        return str
    else:
        return rev_str(str[1:]) + str[0]
    
if __name__ == '__main__':
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))