

if __name__ == '__main__':

    #comprehension
    a = [ab for ab in range(10) if ab %2 == 0]
    print a


    #enumerate
    t = ["a","b","c"]

    x = [ (index,value) for index,value in enumerate(t)]
    print x
