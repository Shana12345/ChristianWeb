# Christian Web
## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Construction](#construction)
   * [Orignial ERD](#erd)
   * [Final ERD](#Final_ERD)
   * [Risk Assessment](#risk_assessment)	
   * [Risk Assessment Table](#risk_table)
	* [User Stories](#userstories)

[Sprints & Planning](#spr1)
   * [Trello Board Sprint 1.0](#spr1) 
   * [Trello Board Completion Stage](#sprcompletion)
	
[Testing](#testing)
   * [Report](#report)

     
[Deployment](#depl)
   * [Technologies Used](#tech)
     
[Front End Design](#FE)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
## The Brief
The aim is to create an OOP based application using CRUD method. Here the incorporation of tools methods and technologies was implemented.  The application must be able to control and alter data via at two tables via the functionality of CRUD.

<a name="solution"></a>
### Solution
I choice to make a Christian website through Flask. The purpose of the website was for customers to be able to add information such as a motivation quote and they would be redirected to the home page, from there they would be able to see and read their quote.
This intended to cover the CR in CRUD. Next the customer would have the ability to enter in an author and if it is one the database, 
then they can see all the authors information such as famous quotes, books, and songs they have either written or have used in the church in their daily life. 
The reason for this part of so that the user can updated the website. They can update information based on the authors, so like a Christian Wikipedia website where people can find out random information related to Christianity except they cannot edit another information. This was implemented for the customer to cover the UD in CRUD. Whereby the customer can update and delete. 
<a name="construction"></a>
## Construction
<a name="erd"></a>
### ERD
#### Starting Plan
The original ERD consisted of just 2 tables, bother of which never had foreign keys. While it would have had all the requirements of CRUD it was bit too simple for one’s liking, also with the aim to enhance CRUD by adding foreign keys. 

![Initial ERD](/images/Original.PNG)


#### Delivered solution
<a name="Final_ERD"></a>
The origin plan for the ERD consisted of less tables and entities than were produced in the final application. The reason for the extra table was to add more functionality to the application.
Furthermore, to better see and understand how foreign keys worked on a website.  As shown in the image, a colour code of each element of the tables and their entities represent what was a priority, and what could be held in a queue of 'things to do'.
Also showing what was added and wasn't part of the original design. The elements in green represent all things part of the original design, and what was a must. The ones in green short the what was a must to meet CRUD.
The colours in purple, represented things that were not part of the original plan but was add to the final application. Lastly, the ones in pink represent things that had not yet been made,
and was the least a priority, reason either being the main table for that entity may not have been created or simply because they were optional.

![Final ERD](/images/Final.PNG)


<a name="risk_assessment"></a>
## Risk Assessment
# Requirements / Product Backlog
Here, is where all the requirments of the project are listed, though it isn't coloured coded here to show the list of priorties, as it was preferred to colour code the actually ERD diagram as it was a better way of prioritising. 

![Requirements4Light](/images/requirementsProductBacklog.PNG)

<a name="risk_table"></a>
Here, the risk assessment is analysing potential actions that can have a negative impact towards individuals, or the surrounding.

## Risk Assessment Table
![Risk Assessment Table1](/images/risktable1.PNG)

![Risk Assessment Table2](/images/risktable2.PNG)

<a name="userstories"></a>
## User Stories (Users and Developers)
To create the user stories, Trello was used, there was listed all the use-cases for the product in the terms of a ‘user’ and ‘developer’.

![UserStories](/images/userdev.PNG)


<a name="spr1"></a>
## Trello Board (Sprint)
Each entry represents a sprint. Each sprint was roughly 4 days, however each need to be met. 

![Sprint](/images/sprint.PNG)

![Sprints](/images/sprints.PNG)



<a name="sprcompletion"></a>
## Trello to completion
The project is now in the completion stage, where all are moved to the 'Done' as all tasks was complete along with other optional features and functionality, futhermore, other feature (un-needed) features were not implemented such as the search function because of time limitations.

![Completed..](/images/Done.PNG)

![Complete..](/images/Done2.PNG)

![Completed2..](/images/thingsAddedandCancelled.PNG)

<a name="testing"></a>
### Testing
## URL Testing
Here was the creation of testing in order to test. Code to test was being created in python for each area of the application. Firstly, the code to test the application’s URL was created. Once it was made it was they pushed up to GitHub, to invoke Jenkins, once Jenkins was triggered the results could be seen on Jenkins console to see whether it was a success or not. 

![Initial ERD](/images/URL.PNG)

<a name="report"></a>
### Report
## Database Testing and full coverage report
Test coverage for the coverage report passed at 39%.

![Initial ERD](/images/coverageReport.PNG)

<a name="depl"></a>
## Deployment
The automated build, test and deployment process was done by Jenkins, via a webhook to GitHub which was triggered with every push event. This website can be deployed both locally as well as externally by a virtual machine. 

### Technologies Used
* GCP Database Engine - Database
* Python - Logic
* Jenkins - CI Server
* [Git](https://github.com/Shana12345/ChristianWeb.git) - VCS
* [Trello](https://trello.com/b/rRkFyIuR/la-projecto-de-shana-charlery) - Project Tracking


<a name="visrep"></a>
### Front End Visual Representation of my Solution

### Home
![HomePage](/images/Home.PNG)


### About
![AboutPage](/images/About.PNG)


### CreateandRecieve
![CRPage](/images/CreateandRecieve.PNG)


### EnterQuote
![EnterQuotePage](/images/EnterQuote.PNG)


![EnterQuotePage2](/images/DeleteandUpdate.PNG)


### De que se trata (spanish page)
![SpanishPage](/images/Desetrata.PNG)


## Registering and requesting a future author
![fa](/images/requestingFuture.PNG)


## Requested author added
![ad](/images/requestedauthoradded.PNG)


## Entering a quote
![enter](/images/toenteraquote.PNG)


## Quote added (redirected to Homepage)
![qa](/images/quoteadded.PNG)


## Updating my quote
![upq](/images/toupdatequote.PNG)


## Update added
![upa](/images/quoteupdated.PNG)


## Delete my quote
![dq](/images/Deletemyquote.PNG)


## Quote deleted
![qd](/images/quotedeleted.PNG)


<a name="improve"></a>
## Improvements for the Future
The improvement that needed to be made would be adding the extra functionality. The 'things cancelled' on the kanban board. In addition, adding a search function to enhance usability. 

<a name="auth"></a>
## Authors

Shana Charlery

<a name="ack"></a>
## Acknowledgements

* QA consulting and our fantastic instructors
* The rest of our wonderful cohort on the programme


