# Test Cases – Simulated Device Monitoring and Alert System

Tested by: (your name)        Date: (date of testing)

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Showed Reading 1 to 5: 28, 31, 35, 37, 29 °C | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully." | Showed "Reading added successfully."; View then listed 33 °C as Reading 6 | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | "Invalid input. Enter a whole number only."; View still showed 5 readings | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | "Invalid reading. Enter a value from 0 to 100."; View still showed 5 readings | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | "Invalid reading. Enter a value from 0 to 100."; View still showed 5 readings | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | Added 30; classification listed "30 °C -> WARNING" | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | Listed "35 °C -> WARNING" (37 °C -> CRITICAL) | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Total 160, Average 32.00 °C, Min 28 °C, Max 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), ATTENTION REQUIRED | Pass |
| TC09 | Enter 9 | Error message; menu shown again | "Invalid choice. Please enter a number from 1 to 5." and the menu appeared again | Pass |
| TC10 | Choose 5 | Exit message; program ends | "Thank you for using the Device Monitoring System." and the program ended normally | Pass |

## Additional Tests

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC11 | Choose 2, press Enter only | Rejected | "Invalid input. The reading cannot be empty." | Pass |
| TC12 | Choose 2, enter 3.5 | Rejected | "Invalid input. Enter a whole number only." | Pass |
| TC13 | Choose 2, enter 0 | Accepted (lower boundary) | "Reading added successfully." | Pass |
| TC14 | Choose 2, enter 100 | Accepted (upper boundary) | "Reading added successfully." | Pass |
| TC15 | Choose 2, enter 101 | Rejected | "Invalid reading. Enter a value from 0 to 100." | Pass |
| TC16 | Add 33, then choose 4 | Total 193, Avg 32.17, WARNING 3 (50.00%) | Number 6, Total 193, Average 32.17 °C, NORMAL 2 (33.33%), WARNING 3 (50.00%), CRITICAL 1 (16.67%), ATTENTION REQUIRED | Pass |

## Bugs Found and Fixed

- (Write your own here. Describe a bug you found while testing and how you fixed it.
  If you found none, write the test that was hardest to pass.)
