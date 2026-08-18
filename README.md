# Technical assessment

## Short description
At a parcel delivery company should be automated the internal handling of parcels coming in. 
The parcels are coming in at the distribution centre and need to be handled by different departments based on their weight and value.
Currently management is making plans that could lead to the adding or removal of departments in the future.

## Features

### Feature 1
The current business rules are as follows:
- Parcels with a weight up to 1 kg are handled by the "Mail" department.
- Parcels with a weight up to 10 kg are handled by the "Regular" department.
- Parcels with a weight over 10 kg are handled by the "Heavy" department.

### Feature 2
Parcels with a value of over € 1000,- need to be signed off by the "Insurance" department, before being processed by the other departments.

## Actions to do
- Parse the XML file (Container_68465468.xml)
- Build a working application
- Unit tests
- Presentation (maybe some UI / Console app - here only in log file)


# Solution
## Code
See parcelhandling.py
- tests: test_parcelhandling.py
- logfile: Log_parserhandling.log

## Possible improvements
For improvements of existing code, see README_improvements.md
