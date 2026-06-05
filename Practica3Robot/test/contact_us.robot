*** Settings ***
Resource    ../resources/keywords.robot

Suite Setup       Abrir Sitio
Suite Teardown    Cerrar Navegador

*** Variables ***
${NOMBRE}     Alex
${EMAIL}      alex@test.com
${ASUNTO}     Prueba Robot Framework
${MENSAJE}    Mensaje enviado desde Robot Framework

*** Test Cases ***
Formulario Contact Us

    Click Element
    ...    xpath=//a[contains(text(),'Contact us')]

    Input Text
    ...    xpath=//input[@data-qa='name']
    ...    ${NOMBRE}

    Input Text
    ...    xpath=//input[@data-qa='email']
    ...    ${EMAIL}

    Input Text
    ...    xpath=//input[@data-qa='subject']
    ...    ${ASUNTO}

    Input Text
    ...    xpath=//textarea[@data-qa='message']
    ...    ${MENSAJE}

    Choose File
    ...    xpath=//input[@type='file']
    ...    /home/alexdev/Documentos/qaeje/Practica3Robot/archivos/prueba.txt 

    Captura Evidencia    formulario_completo

    Click Button
    ...    xpath=//input[@data-qa='submit-button']

    Handle Alert    ACCEPT

    Page Should Contain
    ...    Success! Your details have been submitted successfully.

    Captura Evidencia    contacto_exitoso