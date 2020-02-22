

if __name__ == "__main__":
    test1 = ['trek', 'cannonale', 'redline', 'specialized']
    print (test1)

    for test in test1:
        print (test)

    print (test1[-1])
    print (test1[-2])

    test1.insert(0, 'trekking')
    print (test1)

    del test1[0]
    print (test1)

    test1.append('10')
    
    print (sorted(test1))
    test1.reverse()
    print (test1)
    test1.pop()
    print(len(test1))
