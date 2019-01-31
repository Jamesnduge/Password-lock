## Password-Lock  🔒
### CREATED BY  James Mwangi Nduge

----------------------------------------------------------------------

## Project Objectives
The objective of this project is to create an application, that allows the user to create an account where they are able to see, create and save credentials.
----------------------------------------------------------------------

## Technologies used
Python
Atom Text Editor




-----------------------------------------------------------------------------

## Behaviour driven Development (BDD)
|Behaviour         |  Input |  Output  |       
|------------------|---------|-----------|
|Ask user for credentials| username,password | Welcome message with inputted name|
| Ask user to continue into account created               | "ok" or else | Prompt user to select a short-code |
|Navigate through app options | short-code "new" | prompt user to enter account-name and username for that account|
|Generate password| Keyword 'generate'| A randomly compiled 8-character password|
|| short-code "disp" | All created credentials(credentials list) |
|| short-code "ex" | Exit message |

---------------------------------------------------------------------------------
|             Pseudocode                            |
|---------------------------------------------------|
|* create passwordLocker.py file
|* create locker_test.py
|*  use _ __init__ _ to define parameters of the objects
|* Test initialisation using  test_init(self)  method
|* add save_user() method and test it using test_save_user(self)
|* add save_account() method and test it using test_save_account(self)
|* add display_accounts() method and test it using test_display_all_accounts(self)
|* add generate_password() method and test it using test_gen_password()   


---------------------------------------------------------------------------------

## User Requirements.
To use the application on the web follow the outlined steps:
1. Visit the following page https://github.com/Jamesnduge/Password-lock.git
2. clone the repository
3. make sure you install the python requirements and then run "./run.py" command

---------------------------------------------------------------------

## Known bugs
There are no Known bugs. If any bug seen, report to, james_mwangi@aol.com

## Support or contribution instructions
If you may require to help improve the application, contact the author at: james_mwangi@aol.com


## Contact information
For any questions or suggestions contact me through james_mwangi@aol.com


-----------------------------------------------------------------------------
## Copyright and license information

MIT License

Copyright (c) [2019] [James Mwangi Nduge]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
