import time
import sys
import json


def create(k,v,ttl=0):
    flag=1
    file_path=input("enter optional filepath or press enter for default location:")or"datastore.txt"   #press enter for default location
    f=open(file_path,"a+")
    f.seek(0)
    fr=f.read().split("\n")
    for i in fr:
        kv=(i.split(":",1))
        k1=kv[0]
        if k1==k:
            flag=0
            break
    if flag==0:
        print("error - key already exists\n")   #error,if the given key already exists
    else:
        if(k.isalpha()):
            x=1024*1024*1024    #1GB
            y=16*1024           #16KB
            z=sys.getsizeof(f)                                     
            a=len(k)
            c=sys.getsizeof(v)
            if z<x and c<=y:    #checks whether file sizes doesn't exceed 1GB and json object value size doesn't exceed 16KB
                if ttl==0:
                    value,et=v,ttl
                else:
                    value,et=v,time.time()+ttl
                if a<=32: 
                    kvt=str(k)+":"+str(value)+","+str(et)
                    f.write(kvt)
                    f.write("\n")
                    print("key created\n")
                else:
                    print("error - invalid key format more than 32 chars")    #error,key is more than 32 chars
            else:
                print("error - Memory limit exceeded\n")     #error,violated file and value size limits
        else:
            print("error - Invalind key_name\n")             #error,invalid key formats
    f.close()
            
def read(k):
    try:
        flag=0
        file_path=input("enter the filepath of the datastore:")or"datastore.txt"   #enter the location of the datastore or press enter if its default location
        f = open(file_path, "r")
        fr=f.read().split("\n")
        for i in fr:
            kv=(i.split(":",1))
            k1=kv[0]
            if k1==k:
                vet=kv[1].rsplit(",",1)
                v1=(vet[0]).replace("'", '"')
                v=json.loads(v1)           #value as json object
                #print("type of value:",type(v))
                et=float(vet[1])
                if et!=0:
                    if time.time()<et:
                        print(str(k)+":",v,"\n")
                        flag=1
                        break
                    else:
                        print("key -",k,"has expired\n")     #if the time-to-live of the key has expired          
                        delete_expkey(k,file_path)
                        flag=1
                        break
                else:
                    print(str(k)+":",v,"\n")
                    flag=1
                    break
        if flag==0:
            print("error - key does not exist\n")     #error,the key is present in the datastore,either mis-spelt or deleted from the datastore    
        f.close()
    except IOError:
        print('Exception - file not found')

def delete(k):
    try:
        flag=0
        file_path=input("enter the filepath of the datastore:")or"datastore.txt"    #enter the location of the datastore or press enter if its default location
        f = open(file_path, "r")
        d = f.readlines()
        f = open(file_path, "w")
        for i in d:
            i=i.strip('\n')
            e=(i.split(":",1))[0]
            if e!=k:
                f.write(i)
                f.write("\n")
            else:
                vet=((i.split(":",1))[1]).rsplit(",",1)
                v=(vet[0])
                et=float(vet[1])
                if et!=0:
                    if time.time()<et:
                        print("key successfully deleted\n")
                        flag=1
                    else:
                        print("key-",k,"has expired\n")     #if the time-to-live of the key has expired
                        delete_expkey(k,file_path)
                        flag=1
                else:
                    print("key successfully deleted\n")
                    flag=1
        if flag==0:
            print("error - key does not exist\n")     #error,the key is present in the datastore
        f.close()
    except IOError:
        print('Exception - file not found')

def delete_expkey(k,filepath):       #deleting expired key-value pairs
    f = open(filepath, "r")
    d = f.readlines()
    f = open(filepath, "w")
    for i in d:
        i=i.strip('\n')
        e=(i.split(":",1))[0]
        if e!=k:
            f.write(i)
            f.write("\n")
    f.close()
        
        
