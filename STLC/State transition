## ATM State Transition Testing

States:

1. Start
2. Enter PIN
3. Error
4. Access Granted
5. Card Retained
6. End

Events / Transitions:

1. Start → Enter PIN: The ATM displays the PIN entry screen.
2. Enter PIN → Access Granted: The user enters the correct PIN.
3. Enter PIN → Error: The user enters an incorrect PIN.
4. Error → Enter PIN: The user has made fewer than 3 incorrect attempts and can try again.
5. Error → Card Retained: The user has reached 3 incorrect attempts.
6. Card Retained → End: The ATM retains the card and ends the session.

Note: The ATM maintains an incorrect-attempt counter. It increases after every incorrect PIN. This allows the same states to be reused without creating a separate state for every attempt.

### State transition table

|  | Event 1: Start session | Event 2: Correct PIN | Event 3: Incorrect PIN | Event 4: Attempts below 3 | Event 5: 3 attempts reached | Event 6: End session |
| --- | --- | --- | --- | --- | --- | --- |
| S1: Start | S2 | — | — | — | — | — |
| S2: Enter PIN | — | S4 | S3 | — | — | — |
| S3: Error | — | — | — | S2 | S5 | — |
| S4: Access Granted | — | — | — | — | — | — |
| S5: Card Retained | — | — | — | — | — | S6 |
| S6: End | — | — | — | — | — | — |
