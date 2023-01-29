*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}      Chrome
${Url}          https://www.saucedemo.com/
${name}         standard_user
${pass}         secret_sauce


*** Test Cases ***
Login saucedemo
    open page
    Login


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Login
    Input Text    xpath=/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input    ${name}
    Input Text    xpath=/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input    ${pass}
    Click Element    xpath=/html/body/div/div/div[2]/div[1]/div[1]/div/form/input
    Close Browser
