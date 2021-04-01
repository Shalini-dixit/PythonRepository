def loadingBar(load):
    done_status = int(load/10)
    pending_status = 10-done_status
    
    if(pending_status>0):
        print("{}% [{}{}]".format(load,done_status*'%',pending_status*'.'))
        print("Still loading...")
    else:
        print("{}% Complete!".format(load))
        print("[{}] ".format(done_status*'%'))

#loadingBar(30)
#loadingBar(50)
#loadingBar(100)
load=int(input("Enter a number"))
loadingBar(load)