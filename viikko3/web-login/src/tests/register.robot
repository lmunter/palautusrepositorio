*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kale
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kale
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kale
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kale
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Go To Register Page
    Go To  ${REGISTER_URL}

Register Page Should Be Open
  Title Should Be  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page