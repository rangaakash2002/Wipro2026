*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://practicetestautomation.com/practice-test-login/
${BROWSER}        chrome
${USERNAME}       student
${PASSWORD}       Password123

*** Test Cases ***
Verify Successful Login
    [Documentation]    Test case to login with valid credentials.
    [Tags]             Regression    Login

    Open Browser To Login Page

    # Inputting credentials into text boxes
    Input Text       id=username    ${USERNAME}
    Input Text       id=password    ${PASSWORD}

    # Clicking the login button
    Click Button     id=submit

    # Validation using BuiltIn keywords
    Wait Until Page Contains    Logged In Successfully    timeout=5s
    Element Should Be Visible    link=Log out

    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window