*** Settings ***
Documentation    Test expressions with a client
Library    ${CURDIR}/../libs/calc_app_handler.py

*** Variables ***
${SERVER_IP}    192.168.3.6
${SERVER_PORT}    9998

*** Test Cases ***
Expressions
    Given The Process Has Started With    ${SERVER_IP}    ${SERVER_PORT}
    And The Welcome Message Appeared

    # Valid expressions
    # Sum/Sub
    When The Expression Provided Is    1 + 1.2
    Then The Result Should Be Equals To    2.2

    When The Expression Provided Is    -1 + 1
    Then The Result Should Be Equals To    0.0

    When The Expression Provided Is    - 1.1 +5
    Then The Result Should Be Equals To    3.9

    When The Expression Provided Is    -1 - 2.4
    Then The Result Should Be Equals To    -3.4

    # Prod
    When The Expression Provided Is    4 * 8
    Then The Result Should Be Equals To    32.0

    When The Expression Provided Is    -4 * 8.25
    Then The Result Should Be Equals To    -33.0

    When The Expression Provided Is    -4 * 8.25
    Then The Result Should Be Equals To    -33.0

    When The Expression Provided Is    -2.0 * -2.25
    Then The Result Should Be Equals To    4.5

    # Div
    # When The Expression Provided Is    5 / 2
    # Then The Result Should Be Equals To    2.5

    # When The Expression Provided Is    10 / 3
    # Then The Result Should Be Equals To    3.3

    # When The Expression Provided Is    10 / 3
    # Then The Result Should Be Equals To    3.3

    # Invalid expressions
    # When The Expression Provided Is    10 / 0
    # Then The Command Must Be Unsuccessful

    # Invalid syntax
    When The Expression Provided Is    23 + 
    Then The Command Must Be Unsuccessful

    When The Expression Provided Is    - 3
    Then The Command Must Be Unsuccessful

    When The Expression Provided Is    23 ++ 3
    Then The Command Must Be Unsuccessful

    When The Expression Provided Is    23 3
    Then The Command Must Be Unsuccessful

    When The Expression Provided Is    23..0 + 4
    Then The Command Must Be Unsuccessful

    When The Expression Provided Is    -. + 
    Then The Command Must Be Unsuccessful
