## Overview:
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [General structure](README.md#output)
4. [Comments on time complexity](README.md#output)
5. [Output](README.md#output)


## Problem:

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

This program provides a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

## General Structure:
The main program is saved in src as h1b_counting.py and this will be ran from the run.sh file on the top most level. the input can be found in the input directory and the output generated from h1b_counting.py will be saved in two files that can be found under the output directory. make sure when running that the paths to these files are indeed reflected in the run.sh file.

## Input Datasets: 

Input is to be saved in our top level input directory as h1b_input.csv. If you download any of the raw data, save the file as such and place it in the input directory, then update the run.sh file to have ./input/h1b_input.csv as first argument.

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). 

There are Excel files converted from this into a semicolon separated (";") format and placed them into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). These were used for testing.

## Comments on time complexity:
It is understood that perhaps a stack data structure could be implemented to improve time complexity in som of the areas of the code (for example around lines 84 or 95 where there are double for loops) this could possibly improve time complexity to O(n^2) to O(n) if such a data structure could be implemented. I would like to revisit this project and improve it in this manner. Improving the time efficiency is always best practice.

## Output:

The program creates 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

Each line of the `top_10_occupations.txt` file contains these fields in this order:
1. __`TOP_OCCUPATIONS`__: Use the occupation name associated with an application's Standard Occupational Classification (SOC) code
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that occupation. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to total number of certified applications regardless of occupation. 

The records in the file must be sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__, and in case of a tie, alphabetically by __`TOP_OCCUPATIONS`__.

Each line of the `top_10_states.txt` file contains these fields in this order:
1. __`TOP_STATES`__: State where the work will take place
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work in that state. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total number of certified applications regardless of state.

The records in this file are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__ field, and in case of a tie, alphabetically by __`TOP_STATES`__. 




### The Repo directory structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── your-own-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```
