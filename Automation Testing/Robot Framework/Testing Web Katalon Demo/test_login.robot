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
Valid Login
    open page
    Valid Login

Invalid username
    open page
    Invalid username

Invalid password
    open page
    Invalid password

Invalid username and password
    open page
    Invalid username and password


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Valid Login
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[3]/a
    Input Text    id=txt-username    ${name}
    Input Text    id=txt-password    ${pass}
    Click Element    id=btn-login
    Title Should Be    CURA Healthcare Service
    Close Browser

Invalid username
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[3]/a
    Input Text    id=txt-username    ${invalid_name}
    Input Text    id=txt-password    ${pass}
    Click Element    id=btn-login
    Page Should Contain    ${error}
    Close Browser

Invalid password
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[3]/a
    Input Text    id=txt-username    ${name}
    Input Text    id=txt-password    ${invalid_pass}
    Click Element    id=btn-login
    Page Should Contain    ${error}
    Close Browser

Invalid username and password
    Click Element    id=menu-toggle
    Click Element    xpath=/html/body/nav/ul/li[3]/a
    Input Text    id=txt-username    ${invalid_name}
    Input Text    id=txt-password    ${invalid_pass}
    Click Element    id=btn-login
    Page Should Contain    ${error}
    Close Browser
