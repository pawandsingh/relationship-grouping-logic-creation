# relationship-grouping-logic-creation
This is a process we can use to create n number of files in Input folder specified which has all the files that need to aggregate relationships based on parents defined in the input file.


If facing problem, add add python path to Environment variable for python location( it is usually like: C:\Users{username}\AppData\Local\Programs\Python\Python37-32 for instance)
After getting python installed for windows machines on your cmd type python and it should work.
Next we need to run each of the below mentioned Pip commands on cmd to install required libraries;They are as:

pip install pandas

pip install datetime

pip install os

pip install logging

pip install sys


Identify default path as well by running following comming python: import os; os.getcwd() and we may need to place code files in a Bin folder there and change default path of home directory by using command os.chdir('{path}').
For example if scripts are at path : 'C:\Users{username}\Bin' just run os.chdir('Bin') to change it from 'C:\Users{username}' to 'C:\Users{username}\Bin'
Specify input folder path as well as ouput folder path where you are placing input files and want output files respectively in the confif.txt file which is also placed in Bin folder.
Also created a Logs folder as we created Bin folder at same location. This will capture logs for every execution.
In order to run python code nowwe just simply need to excute following from cmd while in home directory(C:\Users{username}): python Relaionship_Python_Script.py

If successfully completed, we would see a message on command prompt saying: "Processing Done".
This process satisfies the requirements, has logging mechanism, dynamic parametrization, can process multiply files in a loop and code can be modified to scale requirements.
