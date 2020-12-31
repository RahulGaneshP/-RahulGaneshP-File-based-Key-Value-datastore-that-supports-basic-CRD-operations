#File-based-Key-Value-datastore-that-supports-basic-CRD-operations

a file-based key-value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop. The data store must be exposed as a library to users that can instantiate and works with the data store.

The data store will support the following:

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a default location on the laptop. 

2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.

3. If Create is invoked for an existing key, an appropriate error will be returned. 

4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object. 

5. A Delete operation can be performed by providing the key. 

6. Every key supports setting a Time-To-Live property when it is created. This property is optional if you don't wan't this property set time-to-live as 0. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired,the key will no longer be available for Read or Delete operations. 

7. Appropriate error responses will always be returned to the user if it uses the data store in unexpected ways or breaches any limits.

8. The size of the file storing data must never exceed 1GB. 

9. More than one client process cannot be allowed to use the same file as a data store at any given time. The data store is thread-safe.

10. The client will bear as little memory costs as possible to use this data .


Usage:


1.place both the key_value_datastore.py and mainn.py file in the same directory.

2.Use python version 3.0 and above. 

3.Run the main.py file. 

4.select an operation to be performed on the data store. 

5.Enter optional file path Or choose the default location of the key-value datastore. 

6.Enter the Key,Value and Time-to-Live property values and thus the operations are performed. 

7.Choose Exit option to terminate the program. 


Languages:

Python

Code is accompanied with sample input and output test cases,please go through sample ip_op.pdf and the comments for the same and to know how the code works and how to perform operations. is accompanied with sample input and output test cases done ,please go through sample ip_op.pdf and the comments for the same and to know how the code works and how to perform operations.

The key_value_datastore.py module is imported as library and used in the main.py file, both the files should be in the same directory.







