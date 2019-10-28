## Revision History
Date | Version | Description | Author
--- | --- | --- | ---
26.10.19 | 1.0 | First release of the UC | Nico Diefenbacher

## Table of Contents
- [1. Use Case Create Account](#1-use-case-create-account)
  - [1.1 Brief Description](#11-brief-description)
- [2. Flow of Events](#2-flow-of-events)
  - [2.1 Basic Flow](#21-basic-flow)
  - [2.2 Alternative Flows](#22-alternative-flows)
- [3. Sepcial Requirements](#3-special-requirements)
- [4. Preconditions](#4-preconditions)
- [5. Postconditions](#5-postconditions)
- [6. Extension Points](#6-extension-points)

## 1. Use-Case Create Account
### 1.1 Brief Description
This use case allows the user to create an account. For the creation following credentials must be provided:
- mail
- password

## 2. Flow of Events
### 2.1 Basic Flow
- User enters mail
- User enters password two times
- User hits register
#### 2.1.1 Activity Diagram
![CreateAccountUseCase](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/uc/CreateAccountUseCase.PNG)
#### 2.1.2 Mock up
##### Register
![CreateAccountMockup](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/mockups/CreateAccountMockup.jpeg)
### 2.2 Alternative Flows
n/a

## 3. Special Requirements
n/a

## 4. Preconditions
n/a

## 5. Postconditions
If a user completes this workflow, the users profile must have been created on the server. 

## 6. Extension Points
n/a
