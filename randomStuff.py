from random import randint
#Throw a dice
def dice():
    return randint(1,6)

#Toss a coin
def coin():
    output=['heads','tails']
    return "It's "+output[randint(0,1)]

#check Net connection
def connectionStatus():
    import socket
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == "127.0.0.1":
        return False
    else:
        return True


from notify import notify
#Brightness Control
def changeBrightness(n):
    from subprocess import call
    try:
        call(["./brightness", str(n / 100)])
    except:
        notify(message="Failed to change brightness")

#Volume Control
def changeVolume(n):
    from subprocess import getoutput
    getoutput("osascript -e 'set Volume "+str(n)+"'")
