*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${BROWSER}    Chrome

*** Keywords ***
Abrir Sitio
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Cerrar Navegador
    Close Browser

Captura Evidencia
    [Arguments]    ${nombre}
    Capture Page Screenshot    evidencias/${nombre}.png

Ir A Login
    Click Element    xpath=//a[contains(text(),'Signup / Login')]

Validar Texto
    [Arguments]    ${texto}
    Page Should Contain    ${texto}