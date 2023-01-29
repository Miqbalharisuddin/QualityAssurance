*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}          Chrome
${Url}              https://www.saucedemo.com/
${name}             standard_user
${wrong_name}       yanto
${pass}             secret_sauce
${wrong_pass}       yanto123


*** Test Cases ***
Success Login saucedemo
    open page
    Success Login

Failed Login saucedemo
    open page
    Failed Login


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Success Login
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Close Browser

Failed Login
    Input Text    id=user-name    ${wrong_name}
    Input Text    id=password    ${wrong_pass}
    Click Element    id=login-button
    Close Browser
