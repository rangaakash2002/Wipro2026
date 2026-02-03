*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Sleep       5s
    Maximize Browser Window

*** Test Cases ***
DAY-13-q1.robot
    Open Application
    Title Should Be    Google
    capture page screenshot
    Close Browser