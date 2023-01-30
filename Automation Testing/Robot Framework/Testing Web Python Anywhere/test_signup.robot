*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}      Chrome
${Url}          http://barru.pythonanywhere.com/daftar
${name}         bankjago
${email}        bankjago@gmail.com
${pass}         jago123


*** Test Cases ***
Valid SignUp
    open page
    Valid SignUp


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Valid SignUp
    Click Element    id=signUp
    Input Text    id=name_register    ${name}
    Input Text    id=email_register    ${email}
    Input Text    id=password_register    ${pass}
    Click Element    id=signup_register
    Page Should Contain    Berhasil
    Close Browser
