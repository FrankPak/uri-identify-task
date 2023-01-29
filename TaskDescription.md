Visma Solutions - programming task

Problem:
Visma Solutions Oy is developing an application for identity management. With the application, users can login to integrated applications, confirm payments and sign documents. Identity management is a mobile application, and other apps can call its services through deep linking. When this is used, the identity management application would open automatically from the right in-app location. In this assignment, you will be implementing a part of this logic.

Read all the instructions carefully before you begin. Your submission for this assignment is only used for evaluating your competence towards the position. 

Task:
Your task is to design and implement a class which is responsible for identifying what kind of requests it receives. Other apps can call the identity app using the scheme visma-identity.

A uri consists of three parts:
Example: visma-identity://login?source=severa
Scheme: visma-identity
Path: login
Parameters: source=severa

The class needs to satisfy the following requirements:
1. It takes the following information as input
    URI (type: string)
    Example: visma-identity://login?source=severa

2. It has to parse and validate that:
    Used URI scheme is right: visma-identity
    Path is one of the allowed: login, confirm or sign

3. All parameters for a path are valid

4. Requirements for the parameters:
      - Path login:
      source(type:string)
      Example: visma-identity://login?source=severa
      - Path confirm:
      source(type:string)
      payment number(type:integer)
      Example: visma-identity://confirm?source=netvisor&paymentnumber=102226
      - Path sign:
     source(type: string)
     documentid(type:string)
     Example: visma-identity://sign?source=vismasign&documentid=105ab44

5. Class returns:
     Path
     Parameters as key value pairs

6. Is designed using the practises of object-oriented programming

7. Implementation needs to have a client, which uses the new class. You can for example implement the client as another class that uses the relevant methods.