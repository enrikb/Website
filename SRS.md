# GreenClothaWay - Software Requirements Specification

## Table of Contents

-   [GreenClothaWay - Software Requirements Specification](#GreenClothaWay---software-requirements-specification)

    -   [Table of Contents](#table-of-contents)

    -   [1. Introduction](#1-introduction)

        -   [1.1 Purpose](#11-purpose)
        -   [1.2 Scope](#12-scope)
        -   [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
        -   [1.4 References](#14-references)
        -   [1.5 Overview](#15-overview)

    -   [2. Overall Description](#2-overall-description)

        -   [2.1 Vision](#21-vision)

    -   [2.2 Product perspective](#22-product-perspective)

        -   [2.3 User characteristics](#23-user-characteristics)
        -   [2.4 Dependencies](#24-dependencies)

    -   [3. Specific Requirements](#3-specific-requirements)

        -   [3.1 Functionality – Data Backend](#31-functionality--data-backend)

            -   [3.1.1 Read data given over API endpoints](#311-read-data-given-over-api-endpoints)
            -   [3.1.2 Parse data](#312-parse-data)
            -   [3.1.3 Provide data](#313-provide-data)

        -   [3.2 Functionality – User Interface](#32-functionality--user-interface)

            -   [3.2.1 User system](#321-user-system)
            -   [3.2.3 Flashcard boxes](#323-flashcard-boxes)
            -   [3.2.4 Flashcards](#324-flashcards)
            -   [3.2.5 Statistics](#325-statistics)

        -   [3.3 Usability](#33-usability)

        -   [3.4 Reliability](#34-reliability)

            -   [3.4.1 Availability](#341-availability)
            -   [3.4.2 MTBF, MTTR](#342-mtbf-mttr)
            -   [3.4.3 Accuracy](#343-accuracy)
            -   [3.4.4 Bug classes](#344-bug-classes)

        -   [3.5 Performance](#35-performance)

            -   [3.5.1 Response time](#351-response-time)
            -   [3.5.2 Throughput](#352-throughput)
            -   [3.5.3 Capacity](#353-capacity)
            -   [3.5.4 Resource utilization](#354-resource-utilization)

        -   [3.6 Supportability](#36-supportability)

        -   [3.7 Design Constraints](#37-design-constraints)

            -   [3.7.1 Development tools](#371-development-tools)
            -   [3.7.2 Spring Boot](#372-spring-boot)
            -   [3.7.3 ReactJS](#373-reactjs)
            -   [3.7.4 Supported Platforms](#374-supported-platforms)

        -   [3.8 Online User Documentation and Help System Requirements](#38-online-user-documentation-and-help-system-requirements)

        -   [3.9 Purchased Components](#39-purchased-components)

        -   [3.10 Interfaces](#310-interfaces)

            -   [3.10.1 User Interfaces](#3101-user-interfaces)
            -   [3.10.2 Hardware Interfaces](#3102-hardware-interfaces)
            -   [3.10.3 Software Interfaces](#3103-software-interfaces)
            -   [3.10.4 Communications Interfaces](#3104-communications-interfaces)

        -   [3.11 Licensing Requirements](#311-licensing-requirements)

        -   [3.12 Legal, Copyright and other Notices](#312-legal-copyright-and-other-notices)

        -   [3.13 Applicable Standards](#313-applicable-standards)

    -   [4. Supporting Information](#4-supporting-information)

## 1. Introduction

### 1.1 Purpose

This document gives a general description of the GreenClothaWay Project. It explains our vision and all features of the product. 
Also it offers insights into the back- and frontend, the interfaces in both ends for communication and the constraints of the product.

### 1.2 Scope

This document is designed for internal use only and will outline the development process of the project.

### 1.3 Definitions, Acronyms and Abbreviations

| Term     |                                     |
| -------- | ----------------------------------- |
| **SRS**  | Software Requirements Specification |
| **JSON** | JavaScript Object Notation          |
| **API**  | Application Programming Interface   |
| **HTTP** | Hypertext Transfer Protocol         |
| **FAQ**  | Frequently Asked Questions          |

### 1.4 References

| Title                                                                                                 | Date       |
| ----------------------------------------------------------------------------------------------------- | ---------- |
| [Blog](https://blog.greenclothaway.eu/)                                                               | 14/10/2019 |
| [GitHub](https://github.com/GreenClothaWay/Website)                                                   | 14/10/2019 |
| [YoutTrack](https://youtrack.greenclothaway.eu)                                                       | 19/10/2019 |
| [Django](https://djangoproject.com/)                                                                  | 19/10/2019 |
| [Bootstrap](https://getbootstrap.com/)                                                                | 21/10/2019 |

### 1.5 Overview

The next chapters provide information about our vision based on the use case diagram as well as more detailed software requirements.

## 2. Overall Description

### 2.1 Vision

The goal of GreenClothaWay is to create an online trading marketplace for clothes which were offered for free.
Users can offer their old clothes that they don´t like anymore. Other users can take these clothes for free. 
They have only to pay shipping costs or if it´s possible they can pick up the clothes.

## 2.2 Product perspective

Our Use-Case-Diagram

![UsecaseDiagram](GCW_UML.png)

### 2.3 User characteristics

Our main target group consists of people who want to protect our planet. 
Also people who don't have enough money to buy new clothes all the time could be interested in our model.

### 2.4 Dependencies

GreenClothaWay´s Marketplace depends on a database where all inserted clothes are stored. 
This Marketplace also requires a database where all user information are stored.

## 3. Specific Requirements

### 3.1 Functionality – Data Backend

The backend is needed to store, filter and get data for every single product. Also it has to store and create data for new customers. 
It verifies that each user has own login credentials and own personal information such as country, city, address attached to them.
Furthermore it is very important that this data is stored safely.

#### 3.1.1 Communication between frontend and backend

Django will facilitate the communication between frontend and backend a lot. 
Django API can present information from the frontend to the backend easily. 
It automatically  formats and sends data to the backend where django also administers the data. 
Maybe it will be necessery to use JSON in similar parts.


#### 3.1.2 Store and get data

After data is processed from the backend it will be stored in a PostgreSQL Database.
A Database allows to filter data, what is important for customers, in order to filter all products by size, colour, etc.

### 3.2 Functionality – User Interface

The frontend provides a user interface for the marketplace. This user interface includes a product overview with filter options, a shopping cart, user information and communication with other members. 
The product overview includes filter options which allows customers to filter products by colour, size, type, etc.
Furthermore the product overview implements a Tinder-like filter mode which implements swiping. 
Clothes on which a user swiped yes will be added to a seperate overview.

#### 3.2.1 User system

At registration, the data provided by the user is stored in the backend. After registration users can order and insert clothes.

Sign Up:
-   [Sign UP](https://greenclothaway.eu/.....)
Log In:
-   [Log In](https://greenclothaway.eu/.....)

#### 3.2.3 Insert clothes 

Inserting clothes is very easy. Take some pictures from your garment and fill in the product description form. 
The product description form includes information about size, form, colour, condition, etc.
-   [Insert clothes](https://greenclothaway.eu/....)


#### 3.2.4 Buy clothes


#### 3.2.5 Shopping cart


### 3.3 Usability

We will build the user interface intuitive, so that a new user does not necessarily need an explanation. Most users will be comfortable with the UI right away because they are used to webshops allready.

### 3.4 Reliability

In the following we describe the availability, MTBF and MTTR, accuracy and bug classes we strive for.

#### 3.4.1 Availability


#### 3.4.2 Bug classes

We classify bugs like the following:

-   **Critical bug**: A critical bug occurs when the database starts dropping data without intention, secret user information, like passwords, are open to the public or users are not able to use the application at all.
-   **Non critical bug**: A non critical bug appears when the user still can use the application but it appears glitched and the user experience is slightly influenced.

### 3.5 Performance


#### 3.5.1 Response time


#### 3.5.2 Throughput


#### 3.5.3 Capacity


#### 3.5.4 Resource utilization


### 3.6 Supportability


### 3.7 Design Constraints


#### 3.7.1 Development tools

-   Git: version control system
-   JetBrains PyCharm: Python/Django backend development
-   Bootstrap Studio: Frontend development
-   YouTrack: Project planning tool


#### 3.7.4 Supported Platforms

Since FlashCardCommunity will be a web application the user only needs a modern web browser and a stable internet connection. The current versions of Mozilla Firefox, Google Chrome, Opera, Edge and even IE down to version 9 will be supported!

### 3.8 Online User Documentation and Help System Requirements


### 3.9 Purchased Components

-   N\\A

### 3.10 Interfaces

#### 3.10.1 User Interfaces

Our User Interface will provide one page for each implemented functionality.
To navigate between these sites the user will find a menu bar at the top.

Since we are using the Bootstrap framework the application will be accessible from either desktop or mobile browsers.

#### 3.10.2 Hardware Interfaces

-   N\\A

#### 3.10.3 Software Interfaces


#### 3.10.4 Communications Interfaces


### 3.11 Licensing Requirements


### 3.12 Legal, Copyright and other Notices

-   N\\A

### 3.13 Applicable Standards

-   N\\A

## 4. Supporting Information

