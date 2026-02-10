*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Browser    http://localhost:5010    edge     executable_path=C:\Users\Akhila\Desktop\wiprogitcode\Wipro2026\CASE STUDY-4\msedgedriver.exe
Suite Teardown    Close Browser



*** Test Cases ***
Register Patient
    Input Text    name=name    AKASH
    Input Text    name=age     23
    Input Text    name=disease    FEVER
    Input Text    name=doctor     Dr.Smith
    Click Button    Register

Register Multiple Patients
    [Template]    Register Patient Template
    Vijay    22
    Ajay      20

*** Keywords ***
Register Patient Template
    [Arguments]    ${name}    ${age}
    Input Text    name=name    ${name}
    Input Text    name=age     ${age}
    Click Button    Register