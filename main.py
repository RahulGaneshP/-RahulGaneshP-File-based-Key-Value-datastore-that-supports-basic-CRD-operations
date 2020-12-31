import threading                                                        #for python version 3.0 and above
import key_value_datastore as KVS                                       #importing module as a library 
import json


flag=1
while(flag):
    print("Choose an operation to be performed on the datastore")       #operation to be performed on the datastore
    print("1.Create\n2.Read\n3.Delete\n4.Exit")                         
    opt=int(input("enter the option number:"))
    if opt==1:
        key=input("enter the key:")
        print("Enter value in Json object format - {key:value}")
        json_string=input("enter the json object:" )                    #Json string
        value = json.loads(json_string)                                 #value as Json Object
        #print("type of value:",type(value))
        ttl=int(input("enter time-to-live:"))                           #enter 0 if there's no time to live property
        t1=threading.Thread(target=(KVS.create),args=(key,value,ttl))   #creating a key-value in the datastore
        t1.start()
        t1.join()
    elif opt==2:
        key=input("enter key:")
        t2=threading.Thread(target=(KVS.read),args=(key,))              #reading a key-value from the datastore
        t2.start()
        t2.join()
    elif opt==3:
        key=input("enter key:")
        t3=threading.Thread(target=(KVS.delete),args=(key,))            #deleting a key-value pair
        t3.start()
        t3.join()
    elif opt==4:                                                         
        flag=0
        print("Exited")
    else:
        print("invalid option")
        
        
        
        
