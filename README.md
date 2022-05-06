# dummyProject-SprintVotingApp
Used to Conduct voting after Sprint Run
Sprint Voting App.

Why-
First of all let's Know about Sprint,  A Sprint in Scrum is a short period of time wherein a development team works to complete a task,milestone and then deliver.After the Deployment of the project ,we all discuss how the thing goes,what we can improve,what goes as per the plan.After that we can take voting from all the members of team regardings others,so that we can know in which field a member is strong or weak and then we can work on the result we get.
So, for Automating the process of Voting we can use the Sprint Voting App.Its  very user friendly way to help each other to get better then before.


API Overviews-
First let's discuss the flow we need to achieve to get the things done.We need to add some users in the database. Which will work as Members of a specific team.Secondly, we need to create a Sprint with the specific  arguments like duration ,sprint name etc.Then the member which we created earlier can login into the application and Click on the sprint which are available at that time.Then a form will get shown which will take Vote of logged in user .

Number of API -
User
Sprint
Vote

1)User API
User api will be responsible for creating ,modifying, getting and deleting the user from the user table.User API provides operations to manage users in organization.Let's discuss what we can do with these API.
Create User or Registration-
	By using this API we can create new users and insert them into the database.
	Requests-
GET -GET request will be used to get the details of all the users present in the organization.
POST-For creating a new user or adding a user to the database.Parameters which we need to give as POST request are Detail of user i.e. username,password,first name,last name,email address,age etc.
Response-1)Registration Successfully
	      2)Registration Unsuccessful
Delete- For deleting the user from the existing user Table.Parameter required -username
Response-1)Delete Successfully
	      2)Deletion Unsuccessful


Login or Authentication-
By using this API we can login or authenticate the user credentials.After Login we will get some token to carry which we can use for further requests.



Requests-
1)POST-For authenticating or logging in we will use this api.Parameter required-username,password.
Response-
	1)Login  Successfully-if the username and password matches .
	2)Login Unsuccessful-If the username and  password is invalid.

2)Sprint API-

Sprint API will be used for creating a new sprint or Updating the Existing sprint .We can also Delete the existing Sprint.After successful  Login we will be able to reach an Active Sprint.

Requests-
GET- By this we can get all the Spirit which is active.No parameter is required.
POST-For creating a new Sprint.Parameter Required- Sprint Start date,Sprint Last Date,Sprint Name,is active or not,
PUT-Will be used for Updating the Existing Sprint.Parameter required-Existing active Sprint id and data which we need to update.
DELETE-For Deleting the Existing Sprint .Parameter required-Sprint id.

3)Vote Parameter API-

Vote Parameter API will be used to create ,update or delete the Vote parameter Involved in the Voting process.
Request-
GET-By this we can get all the Parameter which we will use for parameter
POST- Used to create a new Parameter for voting.Parameter required-Parameter Name.
PUT-Used to Modify the Existing Parameter.


4)Vote API-
Vote API will be used for taking the Vote From the logged in user regarding the other members of the team.Here we will have certain attributes like Productivity,Help,Innovation etc which will act as constraint on which voting will happen.
Some points to be noticed are-
a)One member of a team can vote for anybody other than himself.
b)One can give vote to others in one or more fields like I can vote to anybody in Productivity and Help both.
c)If somebody doesn't want to vote anybody, the Null value will be assigned at that place.


Requests-
1)POST-For Vote of a person regarding other members of the team. Parameter required-voted_by,voted_to,sprint_id,parameter_id
2)PUT-Used for editing the vote done before.Parameter required-user_id of voter,new voted_to and new parameter_id.
3)DELETE-For Deleting existing votes from the Table.

	



