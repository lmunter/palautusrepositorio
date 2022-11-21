*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Output Should Contain  Ok

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Create User  kalle  pelle123
    Output Should Contain  Virheellinen

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Virheellinen

Register With Valid Username And Too Short Password
    Create User  kalle  kalle12
    Output Should Contain  Virheellinen

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  kalle  kallekalle
    Output Should Contain  Virheellinen
