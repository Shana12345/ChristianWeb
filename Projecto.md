# Personal yoga application

In fulfilment of the solo project assignment due Monday week 7 at QA consulting.

## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Construction](#construction)
   * [Entity Relationship Diagrams](#erd)
   * [ERD](#mla)
	
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
The aim is to create an OOP based application using CRUD method.
Here the incooporation of tools methods and technologies was implemente. 
The application must be able to control and alter data via at two tables via the functionality of CRUD.



<a name="solution"></a>
### Solution
I choice to make a Christian ebsite through Flask. The purpose of the website was for customers to be able to add information such 
as a motivation quote and they would be redirected to the home page, from there they would be able to see and read the their quote.
This intended to cover the CR in CRUD. Next the customer would have ghe ablity to enter in an author and if it is one the database, 
then they can see all the authors informations such as famous quotes, books, and songs they have either written or have used in the church in their daily life. 
The reason for this part of so that the user can updated the website. They can update informtion based on the authors, so like a christian wikipedia website. This 
was implemented for the customer to cover the UD in CRUD. Whereby the customer can update and delete. 


<a name="construction"></a>
## Construction
<a name="erd"></a>
### ERD
#### Starting Plan
![Initial ERD](/fotos4projecto/original.jpg)
The original ERD consisted of just 2 tables, bother of which never had foreign keys. While it would have had all the requirements of CRUD it was bit too simple for ones liking, 
also to enhance CRUD by adding foreign keys. 

#### Delivered solution
![Final ERD](/fotos4projecto/ERD_Final.jpg)
The origin plan for the ERD consisted of less tables and entities than were produced in the final application. The reason for the extra table was to add more functionailty to the application.
Futhermore, to better see and understand how foriegn keys worked on a website.  
As shown in the the image, a colour code of each element of the tables and their entities represent what was a priorties, and what could be held in a queue of 'things to do'.
Also showing what was added and wasn't part of the original design. The elements in green represent all things part of the orignal design, and what was a must. The ones in green short the what was a must to meet CRUD.
The colours in purple, represented things that where not part of the original plan but was add to the final appliation. Lastly, the ones in pink represent things that had not yet been made,
and was the least a priorty, reason either being the main table for that entity may not have been created or simply because they was optional.


<a name="testing"></a>
## Testing

code for testing
python URL assert 
database testing assert
see the results on jenkins


<a name="report"></a>
### Report

[Link to Final Surefire Report](/Documentation/Surefire_Report.pdf)

Test coverage for the backend is at 84%, there are as of yet no working Selenium tests but hope to get these running soon.
The SonarQube static report shows 9 code smells remaining, 0 bugs, 0 duplications and 0 vulnerabilities.

<a name="depl"></a>
## Deployment

The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event

This application can be deployed both locally and externally through a virtual machine. The constants.js file has commented out options to switch from an external to local IP address.

![Deployment Pipeline](/Documentation/CI_pipeline.jpg)
<a name="tech"></a>
### Technologies Used

* H2 Database Engine - Database
* Java - Logic
* Wildfly - Deployment
* Jenkins - CI Server
* Maven - Dependency Management
* Jacoco, EclEmma, Surefire - Test Reporting
* SonarQube - Static Testing
* [Git](https://github.com/ayshamarty/SoloProject.git) - VCS
* [Trello](https://trello.com/qasoloproject) - Project Tracking
* GCP - Live Environment

<a name="FE"></a>
## Front End Design
### Wireframes
Poses
![Poses Wireframe](/Documentation/Poses_Wireframe.png)
Routines
![Routines Wireframe](/Documentation/Routines_Wireframe.png)
### Final Appearance

<a name="improve"></a>
## Improvements for the Future

Currently, IDs are required to update poses and routines, and to add or remove poses from routines. In my next sprint, I would like to create buttons in the front end which allow this functionality without the need for IDs, which would allow the object IDs to be hidden from the user.

In later sprints, I would also like create a health-benefit entity which would have a many to many relationship with poses, so that users can create routines based on their focus for their practice. After this, I would add the capability to create different user accounts. At this point, I would remove the functionality for the user to add and remove poses themselves in the front end. These would instead be hard coded into the database, which the user could manipulate only for adding and removing them from their own routines.

<a name="auth"></a>
## Authors

Aysha Marty

<a name="ack"></a>
## Acknowledgements

* QA consulting and our fantastic instructors
* The rest of our wonderful cohort on the programme


