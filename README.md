# Exercise 34: Publisher Report

Chapter 10 capstone: answer four questions about the video game industry using a table of video game sales (`data/vgsales.csv`).

## Research questions

| # | Research question | Function | Returns | Look back at |
|---|---|---|---|---|
| 1 | After filling missing publishers with `"Unknown"`, which games have an Unknown publisher? | `unknown_publisher_games(df)` | a table | Part 2 |
| 2 | On which Platform did Nintendo sell the most copies worldwide? | `nintendo_best_platform(df)` | a name | Parts 4 and 5 |
| 3 | In which year did Shooter games sell the most copies worldwide? | `best_shooter_year(df)` | a year | Parts 4 and 5 |
| 4 | How many copies were sold worldwide in each decade? | `sales_by_decade(df)` | a Series | Parts 2 and 5 |

## How to run

- See your findings: run `src/publisher_report.py` (or `python src/publisher_report.py` in the terminal).
- Run the tests from the Testing panel (beaker icon), or with `python -m unittest discover` in the terminal.

## If tests won't run

- Select the Anaconda (conda) interpreter: Ctrl/Cmd+Shift+P → "Python: Select Interpreter".
- If you have the old **Python Test Explorer** extension, uninstall it (`code --uninstall-extension littlefoxteam.vscode-python-test-adapter`). It ignores your interpreter.
- `pip install -r requirements.txt` if pandas is missing.
