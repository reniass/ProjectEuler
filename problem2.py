def evenFiboSum():
    seq1 = 1
    seq2 = 2
    seq3 = 0
    sum = 2
    maximum = 4000000
    while seq3 < maximum:
        seq3 = seq1 + seq2
        seq1 = seq2
        seq2 = seq3

        print(seq3)
        print('\n')
        if seq3 % 2 == 0: #and seq2 < maximum:
            #print(seq2)
            print(str(sum) + '+' + str(seq3) + '=' + str(sum + seq3))
            sum += seq3


    return sum


print(evenFiboSum())


