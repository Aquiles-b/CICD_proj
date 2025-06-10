Feature: Test expressions with a client

  Background: The client has connected with the server
    Given The Connection Has Been Established With The Server

  Scenario Outline: Correct expressions
    When The Expression Provided Is <expression>
    Then The Result Should Be Equals To <result>

    Examples:
      | expression     | result  |
      # Sum
      | "1 + 1.2"      | "2.2"   |
      | "-1 + 1"       | "0.0"   |
      | "- 1.1 +5"     | "3.9"   |
      | "-1 - 2.4"     | "-3.4"  |
      # Prod
      | "4 * 8"        | "32.0"  |
      | "-4 * 8.25"    | "-33.0" |
      | "-4 * 8.25"    | "-33.0" |
      | "-2.0 * -2.25" | "4.5"   |
      # Div
      | "5 / 2"        | "2.5"   |
      | "10 / 3"       | "3.3"   |
      | "10 / 3"       | "3.3"   |

  Scenario Outline: Invalid expressions
    When The Expression Provided Is <expression>
    Then The Command Must Be Unsuccessful

    Examples:
      | expression  |
      | "10 / 0"    |
      | "23 + "     |
      | "- 3"       |
      | "23 ++ 3"   |
      | "23 3"      |
      | "23..0 + 4" |
      | "-. + "     |
