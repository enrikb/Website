## Revision History
Date | Version | Description | Author
--- | --- | --- | ---
21.4.20 | 1.0 | First release of the UC | Zeno Berkhan

## Table of Contents
- [1. Use Case Messages](#1-use-case-messages)
  - [1.1 Brief Description](#11-brief-description)
- [2. Flow of Events](#2-flow-of-events)
  - [2.1 Basic Flow](#21-basic-flow)
  - [2.2 Alternative Flows](#22-alternative-flows)
- [3. Sepcial Requirements](#3-special-requirements)
- [4. Preconditions](#4-preconditions)
- [5. Postconditions](#5-postconditions)
- [6. Extension Points](#6-extension-points)

## 1. Use-Case Messages
### 1.1 Brief Description
This use case allows users to communicate with each other in order to make agreements for products.
This includes:
- write messages
- delete messages
- read messages
- restore deleted messages
## 2. Flow of Events
### 2.1 Basic Flow
#### 2.1.1 Write Message
- User visits page of an item
- User clicks "write message"
- User writes message and hits "send"
##### 2.1.1.1 Activity Diagram
![WriteMessageUseCase](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/uc/WriteMessageUseCase.PNG)
##### 2.1.1.2 Mock up
![WriteMessageMockup](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/mockups/WriteMessageMockup.PNG)


#### 2.1.2 Delete Message
- User visits message page
- User clicks "delete message"
##### 2.1.2.1 Activity Diagram
![DeleteMessageUseCase](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/uc/DeleteMessageUseCase.PNG)
##### 2.1.2.2 Mock up
![DeleteMessageMockup](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/mockups/DeleteMessageMockup.PNG)



#### 2.1.3 Read Message
- User visits message page
- User clicks on a message
##### 2.1.3.1 Activity Diagram
![ReadMessageUseCase](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/uc/ReadMessageUseCase.PNG)
##### 2.1.3.2 Mock up
![ReadMessageMockup](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/mockups/ReadMessageMockup.PNG)


#### 2.1.4 Restore Deleted Message
- User visits message page
- User clicks on "trash"
- User clicks on "actins" from wanted message
- User clicks "restore message"
##### 2.1.4.1 Activity Diagram
![RestoreMessageUseCase](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/uc/RestoreMessageUseCase.PNG)
##### 2.1.4.2 Mock up
![RestoreMessageMockup](https://raw.githubusercontent.com/GreenClothaWay/Website/master/doc/mockups/RestoreMessageMockup.PNG)



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
