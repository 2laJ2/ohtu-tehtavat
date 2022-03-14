*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  12345678
    Output should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username minimum length 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  matti  ma123
    Output Should Contain  Password minimum length 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattimatti
    Output Should Contain  Password must not contain letters only

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123 
    Input New Command
