# Backend-TodoList
Django Backend for TodoList App. The backend is built entirely using Django RestFramework. Following are the features present in the backend. <br/><br/>
1.)The Backend provides RestFull service to the angular frontend.<br/><br/>
2.)Basic Crud operation are supported.<br/><br/>
3.)The security to the Application is provided by using JWT Tokens with the help of "simple-jwt" package.<br/><br/>
4.)There is a Forgot password feature where in  a user can reset his password through a password reset link sent to their E-Mail and the link would be valid for 5 minutes(customizable).<br/><br/>
5.)For security purposes a user will not be able to reset his password for a time of 5 minutes(customizable) from the previous link generated.<br/><br/>
6.)The Email link Generated will be only one time usable as the the token for password reset will be blacklisted after one time use.<br/><br/>
7.)the project also includes a Custom User Model for storing user email and password<br/><br/>
Each class in the project has a further explanation of the code.
