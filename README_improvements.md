# Objective document
The actual solution written in Python can still be changed or improved in many ways. 
Find below some possible improvements.

- [Objective document](#objective-document)
- [I. General](#i-general)
- [II. Specific](#ii-specific)
  - [Input](#input)
  - [Parsing](#parsing)
  - [Processing](#processing)
  - [Output](#output)
  - [Unit tests](#unit-tests)
  - [Non-functional requirements](#non-functional-requirements)
- [III. Maintenance to add / remove a department](#iii-maintenance-to-add--remove-a-department)

 
# I. General
- Improve folder structure: 
  - Split up the module and test file into different files & create different folders for modules and tests 
  - Complete file setup.py, ..
- Create a commnand line application
- Add better configuration to be independent from: directories used, environment,..
  - Solve error with virtual environment (regarding "Activate.ps1')


# II. Specific

## Input
- Read a file with a more generic name from a predefined input: a directory, prompt, API,..
- Put the processed data in a small DB for further handling

## Parsing
- During parsing create immediately parcel class objects for the shipment, and not put the parcels first in a data structure
- Store Shipment ID and date for future usage: e.g. in a global variable, in the return parameter of the parser function, ..
- Parse the xml at once into a directory, e.g. with a library as xmltodict (problem: duplicate parcels)
- House number could become an integer (not a string), if we can assume it will never contain a housenr extension

## Processing
- Regarding OOP:
  - Add separate classes for recipient & recipient address
  - Create a class for parsing of XML
  - *Check if technically possible*: For the 3 handling departments have one conditional test & call to handling_done method, independent of department

## Output
- Show output in a simple UI application
- Logging: 
  - add handlers and formatters (e.g. for console), a separate logging configuration file,..
  - logging in JSON-format to have more meaningful format for monitoring tools (e.g. Kibana)

## Unit tests
- Improve unit test coverage: especially for methods of classes and main function
  - main function is tested manual: using different XML input files validate console en logfile output
- Use preconfigured (or synthetic) test data 

## Non-functional requirements
- Add exception handling: e.g. validation of input values in XML, cover more use cases for the unhappy flow, ..
- - Verify performance, e.g. for:
  - Parsing XML file
  - Check code for performance bottlenecks with time profiling & larger data sets 

 
# III. Maintenance to add / remove a department
- Change only 3 lines in the main function
  - Add/remove initialisation of department. For handling/checking department is called a different class method.
  - Add/remove in the for-loop the parcels the condition related to department 
