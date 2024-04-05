*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            https://qademo.onebrick.io/
${email}          tester.brick@mail.com
${password}       Brick123

*** Test Cases ***
Login Page
    [Tags]    Login    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Close Browser

# Login using existing account, not from the Sign Up script
Login Page
    [Tags]    Login    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Input Text    id=your_email    ${email}
    Input Text    id=password    ${password}
    Click Button    class=register
    Wait Until Element Is Visible      class=swal2-header   100
    Element Should Contain     id=swal2-title   Success
    Element Should Contain     id=swal2-content   Welcome Back
    Element Should Be Visible      class=swal2-confirm
    Click Button    class=swal2-confirm
    # logout
    Wait Until Element Is Visible       xpath=//a[@href="/logout"]   100
    Click Link    xpath=//a[@href="/logout"]
    Close Browser

Login Page - Go to Sign Up
    [Tags]    Login    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Click Link    xpath=//a[@href="/"]
    Element Should Be Visible      id=myform
    Close Browser

Login Page - Forgot Password
    [Tags]    Login    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Click Link    xpath=//a[@href="/forgot"]
    # no assertion since the Forgot Password page is not found
    Close Browser

Login Page - Wrong/Unregistered Email
    [Tags]    Login    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Input Text    id=your_email    unregistered_tester.brick@mail.com
    Input Text    id=password    ${password}
    Click Button    class=register
    Element Should Be Visible      class=swal2-header
    Element Should Contain     id=swal2-title   Error
    Element Should Contain     id=swal2-content   Wrong email or password
    Element Should Be Visible      class=swal2-confirm
    Close Browser

Login Page - Wrong Password
    [Tags]    Login    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Click Link    xpath=//a[@href="/login"]
    Input Text    id=your_email    ${email}
    Input Text    id=password    Brick123456
    Click Button    class=register
    Element Should Be Visible      class=swal2-header
    Element Should Contain     id=swal2-title   Error
    Element Should Contain     id=swal2-content   Wrong email or password
    Element Should Be Visible      class=swal2-confirm
    Close Browser
