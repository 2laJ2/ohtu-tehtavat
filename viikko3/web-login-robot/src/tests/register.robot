*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Reset
    Set Username  pa
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Registration
    Registration Should Fail With Message  Username minimum length 3 characters

Register With Valid Username And Too Short Password
    Reset
    Set Username  paavo
    Set Password  pavo123
    Set Password Confirmation  pavo123
    Submit Registration
    Registration Should Fail With Message  Password minimum length 8 characters
    
Register With Nonmatching Password And Password Confirmation
    Reset
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation   pekka321
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Reset
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Set Username  paavo
    Set Password  paavo123
    Submit Credentials 
    Main Page Should Be Open    

Login After Failed Registration
    Reset
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  peka123
    Submit Registration
    Registration Should Fail With Message  Passwords do not match
    Go To Login Page
    Set Username  pekka
    Set Password  pekka123
    Submit Credentials 
    Login Should Fail With Message  Invalid username or password   

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
