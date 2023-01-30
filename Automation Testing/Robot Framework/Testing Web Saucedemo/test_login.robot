*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}          Chrome
${Url}              https://www.saucedemo.com/
${UrlDashboard}     https://www.saucedemo.com/inventory.html
${name}             standard_user
${invalid_name}     yanto
${pass}             secret_sauce
${invalid_pass}     yanto123
${error}            Epic sadface: Username and password do not match any user in this service


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
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Title Should Be    Swag Labs
    Close Browser

Invalid username
    Input Text    id=user-name    ${invalid_name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Page Should Contain    ${error}
    Close Browser

Invalid password
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=login-button
    Page Should Contain    ${error}
    Close Browser

Invalid username and password
    Input Text    id=user-name    ${invalid_name}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=login-button
    Page Should Contain    ${error}
    Close Browser
