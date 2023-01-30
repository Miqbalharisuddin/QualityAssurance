*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}              Chrome
${Url}                  http://barru.pythonanywhere.com/daftar
${email}                jaya@gamail.com
${invalid_email}        yanto@gmail.com
${pass}                 jaya123
${invalid_pass}         jaya123
${passed_massage}
${error_massage}        User's not found


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
    Input Text    id=email    ${email}
    Input Text    id=password    ${pass}
    Click Element    id=signin_login
    Title Should Be    ${passed_massage}
    Close Browser

Invalid username
    Input Text    id=email    ${invalid_email}
    Input Text    id=password    ${pass}
    Click Element    id=signin_login
    Page Should Contain    ${error_massage}
    Close Browser

Invalid password
    Input Text    id=email    ${email}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=signin_login
    Page Should Contain    ${error_massage}
    Close Browser

Invalid username and password
    Input Text    id=email    ${invalid_email}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=signin_login
    Page Should Contain    ${error_massage}
    Close Browser
