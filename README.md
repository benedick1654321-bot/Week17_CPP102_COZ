   # Simulated Device Monitoring and Alert System

   **Student Name:** (your full name)
   **Student Number:** (your student number)
   **Section:** (your section)

   ## Project Description
   This program monitors simulated device temperature readings. It stores the readings in a list, accepts new valid readings, and classifies each reading as NORMAL, WARNING, or CRITICAL. It also prints a numerical summary and an overall status. The limits are for a classroom simulation only and are not real device-safety standards.

   ## Features
   - View all stored temperature readings
   - Add a new reading (whole numbers from 0 to 100 only)
   - Classify every reading (below 30 = NORMAL, 30 to 35 = WARNING, above 35 = CRITICAL)
   - Generate a numerical summary: count, total, average, minimum, maximum, category counts and percentages, and overall status
   - Reject invalid menu choices and invalid readings without crashing

   ## Requirements
   - Python 3 (no external packages)

   ## How to Run
   1. Open a terminal inside the Week17 folder.
   2. Type: `python device_monitor.py`
      (On macOS or Linux, type: `python3 device_monitor.py`)

   ## Sample Output
   ```
   MONITORING SUMMARY
   ------------------
   Number of readings  : 6
   Total of readings   : 193
   Average temperature : 32.17 °C
   Minimum temperature : 28 °C
   Maximum temperature : 37 °C

   NORMAL   : 2 (33.33%)
   WARNING  : 3 (50.00%)
   CRITICAL : 1 (16.67%)

   Overall Status: ATTENTION REQUIRED
   ```

   ## Test Cases
   I performed 16 tests (the 10 required tests plus 6 extra validation and boundary tests). 16 passed and 0 failed. Full details are in [test_cases.md](test_cases.md).

   ## Known Limitations
   - Readings are lost when the program closes, because file handling is not used.
   - A reading cannot be edited or deleted once it is added.
   - Only one reading can be added per use of menu option 2.
   - The classification limits (30 and 35) are fixed in the program, not chosen by the user.

   ## Reflection
   (Write 3 to 5 sentences in your own words. What was the hardest part? Which bug did you fix and how? What would you improve next?)
