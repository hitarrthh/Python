def toh(n,frompeg,topeg,auxpeg):
    if n==1:
        print("THE DISK IS MOVED FROM {} TO {}".format(frompeg,topeg))
        return
    toh(n-1,frompeg,auxpeg,topeg)
    print("THE DISK {} IS MOVED FROM {} TO {}".format(n,frompeg,auxpeg))
    toh(n-1,auxpeg,topeg,frompeg)

n = int(input("ENTER NUMBER OF DISK"))
toh(n,"A","B","C")