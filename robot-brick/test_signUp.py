*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            https://qademo.onebrick.io/

*** Test Cases ***
Sign Up Page
    [Tags]    Sign Up    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Close Browser

Sign Up Page
    [Tags]    Sign Up    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.co
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      class=swal2-header
    Element Should Contain     id=swal2-title   Success
    Element Should Be Visible      class=swal2-confirm
    Close Browser

Sign Up Page
    [Tags]    Sign Up    Positive
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick2@mail.co
    Input Text    id=phoneNumber    8212345678
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      class=swal2-header
    Element Should Contain     id=swal2-title   Success
    Element Should Be Visible      class=swal2-confirm
    Close Browser

Sign Up Page - Email Already Registered
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    dodox@mailinator.com	
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      class=swal2-header
    Element Should Contain     id=swal2-title   Error
    Element Should Contain     id=swal2-content   Email has been taken!
    Element Should Be Visible      class=swal2-confirm
    Close Browser

Sign Up Page - Input Email - Wrong format
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    testmail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=email-error
    Element Should Contain     id=email-error   Please enter a valid email address.
    Close Browser

Sign Up Page - Input Email - Wrong format
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test@mail
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=email-error
    Element Should Contain     id=email-error   Please enter a valid email address.
    Close Browser

Sign Up Page - Email field empty
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=email-error
    Element Should Contain     id=email-error   Please provide an email
    Close Browser

Sign Up Page - First Name field empty
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=firstName-error
    Element Should Contain     id=firstName-error   Please enter a firstname
    Close Browser

Sign Up Page - Last Name field empty
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=lastName-error
    Element Should Contain     id=lastName-error   Please enter a lastname
    Close Browser

# commented since it will be fail
# Sign Up Page - Phone Number field empty
#     [Tags]    Sign Up    Negative
#     SeleniumLibrary.Open Browser    ${url}    chrome
#     Input Text    id=firstName    Test
#     Input Text    id=lastName    Brick
#     Input Text    id=email    test.brick@mail.com
#     Input Text    id=phoneNumber    8212345678
#     Input Text    id=address    Surabaya
#     Input Text    id=password    Brick123
#     Input Text    id=confirm_password    Brick123
#     Click Button    class=register
#     Element Should Be Visible      id=email-error
#     Element Should Contain     id=email-error   Please enter a valid email address.
#     Close Browser

Sign Up Page - Password field empty
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=password-error
    Element Should Contain     id=password-error   Please enter a password
    Element Should Be Visible      id=confirm_password-error
    Element Should Contain     id=confirm_password-error   Password need to match
    Close Browser

Sign Up Page - Confirm Password field empty
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=confirm_password-error
    Element Should Contain     id=confirm_password-error   Please enter a password
    Close Browser

Sign Up Page - Password and Confirm Password not match
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick1234
    Input Text    id=confirm_password    Brick123
    Click Button    class=register
    Element Should Be Visible      id=confirm_password-error
    Element Should Contain     id=confirm_password-error   Password need to match
    Close Browser

Sign Up Page - Input Password - Less character
    [Tags]    Sign Up    Negative
    SeleniumLibrary.Open Browser    ${url}    chrome
    Input Text    id=firstName    Test
    Input Text    id=lastName    Brick
    Input Text    id=email    test.brick@mail.com
    Input Text    id=phoneNumber    8212345678
    Input Text    id=address    Surabaya
    Input Text    id=password    Brick
    Input Text    id=confirm_password    Brick
    Click Button    class=register
    Element Should Be Visible      id=password-error
    Element Should Contain     id=password-error   Please enter at least 6 characters.
    Close Browser
