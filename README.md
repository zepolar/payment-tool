# Payment Tool

Payment Tool is a CLI tool that it allows to make the obtain the total value of the hour-worker of an employee.

The tool receives three mandatory options:

|                | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
| --input or -i. | File to be process by the tool. It should introduce the full path                                         |
| --output or -o | File to save with the results.                                                                            |
| --format or -o | Format of the file that it will process by the tool. At the moment, only it is supported to regex format. |

## Input a file
The file should have the next format:
```
Pepe=MO10:00-12:00,TU10:00-12:00,SA01:00-02:00
```
where 
```
MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday
```


## Project Structure
```
.
└── payment-tool/
    ├── src
    ├── test
    ├── tox.ini
    ├── setup.py
    ├── readme.md
    ├── requeriments.txt
    └── setup.py
```
- src folder, source code
- test folder, set of test 
- tox.ini, config file to run tox command
- setup.py
- readme.md, contains information about the tool
- requirements.txt, set of the libraries needed to run the tool.

## Running test
Execute whatever of the next options:
### First Option
Get inside the project and running the command:
```
pytest
```
Having as result:
```
======================================== test session starts ===========================================================
platform darwin -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0
rootdir: /home/zepolar/workspace/payment-tool
collected 16 items
plugins: anyio-3.5.0

test/test_files.py ......                                                                                         [ 37%]
test/test_utils.py ...                                                                                            [ 56%]
test/unit/test_formats.py ..                                                                                      [ 68%]
test/unit/test_payment.py .....                                                                                   [100%]

========================================================================================================================
```
### Second Option
```
 python3 -m unittest discover
```
Having as result:
```
----------------------------------------------------------------------
Ran 16 tests in 0.002s
OK
```
### Third Option
```
tox
```
Having as result:
```
_________________________________________________________________________________summary_____________________________________________________________________
  py39: commands succeeded
  congratulations :)
```

## Running the tool
To carry out the application, it should execute
```
python3 src/main.py -i test/validFile.txt -o output.txt -f regex
```
The tool receive three parameters which ones are mandatory. In the case, the tool does not receive any parameters,
the one show a little help.