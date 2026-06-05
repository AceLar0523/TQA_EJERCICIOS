*** Settings ***
Resource    ../resources/keywords.robot

Suite Setup       Abrir Sitio
Suite Teardown    Cerrar Navegador

*** Variables ***
${EMAIL}       falso@test.com
${PASSWORD}    123456

*** Test Cases ***
Login Incorrecto
    Ir A Login

    Input Text
    ...    xpath=//input[@data-qa='login-email']
    ...    ${EMAIL}

    Input Password
    ...    xpath=//input[@data-qa='login-password']
    ...    ${PASSWORD}

    Click Button
    ...    xpath=//button[@data-qa='login-button']

    Page Should Contain
    ...    Your email or password is incorrect!

    Captura Evidencia    login_incorrecto