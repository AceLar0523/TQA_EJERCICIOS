*** Settings ***
Resource    ../resources/keywords.robot

Suite Setup       Abrir Sitio
Suite Teardown    Cerrar Navegador

*** Variables ***
${PRODUCTO}    Blue Top

*** Test Cases ***
Busqueda De Productos

    Click Element
    ...    xpath=//a[contains(text(),'Products')]

    Wait Until Element Is Visible
    ...    id=search_product

    Input Text
    ...    id=search_product
    ...    ${PRODUCTO}

    Click Element
    ...    id=submit_search

    Page Should Contain
    ...    Searched Products

    Page Should Contain
    ...    ${PRODUCTO}

    Captura Evidencia    busqueda_producto