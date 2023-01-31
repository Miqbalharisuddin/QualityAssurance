*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}          Chrome
${Url}              https://katalon-demo-cura.herokuapp.com/
${name}             John Doe
${invalid_name}     yanto
${pass}             ThisIsNotAPassword
${invalid_pass}     yanto123
${error}            Login failed! Please ensure the username and password are valid.


*** Test Cases ***
Logout
    open page
    Logout


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Logout
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[3]/a
    Input Text    id=txt-username    ${name}
    Input Text    id=txt-password    ${pass}
    Click Element    id=btn-login
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[5]/a
    Close Browser
