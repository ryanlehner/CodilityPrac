def toBinary(N):
    start = 1
    while start*2 <= N:
        start = start*2

    binary = ''
    while start >= 1:
        if start <= N:
            N = N - start
            start = start / 2
            binary += '1'
        else:
            start = start / 2
            binary += '0'
    
    return binary

def binaryGap(binary):
    binaryList = binary.split('1')
    #print(binaryList)
    gaps = [0]
    for i in range(len(binaryList)-1):
        if '0' in binaryList[i] and len(binaryList) > i+1:
            if binaryList[i-1] == '':
                gaps.append(len(binaryList[i]))
                #print(gaps)
    
    return max(gaps)


for i in range(0, 20):
    print(binaryGap(toBinary(i)), toBinary(i), i)