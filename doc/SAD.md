# GreenClothaWay - Software Architecture Document

## Table of Contents
- [1. Introduction](#1-introduction)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Scope](#12-scope)
    - [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    - [1.4 References](#14-references)
    - [1.5 Overview](#15-overview)
- [2. Architectural Representation](#2-architectural-representation)
    - [2.1 Technologies used](#21-technologies-used)
- [3. Architectural Goals and Constraints](#3-architectural-goals-and-constraints)
- [4. Use-Case View](#4-use-case-view)
    - [4.1 Use-Case Realizations](#41-use-case-realizations)
- [5. Logical View](#5-logical-view)
    - [5.1 Overview](#51-overview)
- [6. Process View](#6-process-view)
- [7. Deployment View](#7-deployment-view)
- [8. Implementation View](#8-implementation-view)
    - [8.1 Overview](#81-overview)
    - [8.2 Layers](#82-layers)
- [9. Data View](#9-data-view)
- [10. Size and Performance](#10-size-and-performance)
- [11. Quality](#11-quality)

## 1. Introduction
### 1.1 Purpose
This document provides an architectural overview of the system, using a number of different architectural views.
### 1.2 Scope
The scope of this SAD is to show the overall architecture of the GreenClothaWay project. Use-Cases, classes used in the backend and the database structure.
### 1.3 Definitions, Acronyms and Abbreviations
Abbreviation | |
--- | --- 
IDE | Integrated Development Environment
MVC | Model View Controller
SAD | Software Architecture Document
SRS | Software Requirements Specification
tbd | to be determined
tba | to be added
UC | Use Case

Definition | |  
--- | ---  
Software Architecture Document | The Software Architecture Document provides a comprehensive architectural overview of the system, using a number of different architectural views to depict different aspects of the system.
### 1.4 References
| Title                                                                                                 | Date       |
| ----------------------------------------------------------------------------------------------------- | ---------- |
| [Blog](https://blog.greenclothaway.eu/)                                                               | 14/10/2019 |
| [GitHub](https://github.com/GreenClothaWay/Website)                                                   | 14/10/2019 |
| [YoutTrack](https://youtrack.greenclothaway.eu)                                                       | 19/10/2019 |
| [Django](https://djangoproject.com/)                                                                  | 19/10/2019 |
| [Bootstrap](https://getbootstrap.com/)                                                                | 21/10/2019 |
### 1.5 Overview
This document contains the architectural representation, goals and constraints.

## 2. Architectural Representation
Our application is build using Django in the backend and HTML and Bootstrap in the Frontend. 
Django does not work with an MVC architecture. It uses a MTV architecture instead. We had make a few adjustments to our documentation because of that.
### 2.1 Technologies used
IDEs:
- Frontend: Botstrapstudio/PyCharm
- Backend: JetBrains PyCharm

Languages:
- Frontend: HTML
- Backend: Python
- Database: PostgreSQL
- Testing: Python (behave)

## 3. Architectural Goals and Constraints
n/a

## 4. Use-Case View
![Use Case Diagram](/doc/GCW_UML.png)
### 4.1 Use-Case Realizations
Specified in diagram.

## 5. Logical View
The following graphic describes the overall class organization of the backend.  
![Class-Diagram](/doc/db_model.png)
### 5.1 Overview

## 6. Process View
tba

## 7. Deployment View  
tba

## 8. Implementation View
tba
### 8.1 Overview
tba
### 8.2 Layers
tba

## 9. Data Viewtba

## 10. Size and Performance
tbd

## 11. Quality
tbd
