# GithubAPI567
Homework 04a - Develop with the Perspective of the Tester in mind

**Write a description of what you thought about when you were designing the code.  What did *you* think was important to do to make it easy to test the program.  What are some of the challenges that you faced when testing this assignment.**

When designing the code, I thought about the sequence of writing my function, since getting the commit history was dependent on getting the repository name. This is because the GET request for the commits requires the name of the repo in the url.

In order to make it easy to test the program, I had a few sample inputs I tried while creating my program to make sure that what I was doing was working. For instance, for the GitHub Repository and Commit History GET requests, I used my GitHub URL as well as that of my friends' in order to make sure I was receiving valid input. 

Some of the challenges I faced when testing this assignment include the fact that you can only have a certain amount of requests to the GitHub API in a certain amount of time. I had exceeded that, and my code stopped worked. I got concerned for a second, but then realized this is an issue I was warned of and just need to wait. I also struggled with the format of the GET request, and jsonifying it helped make the data manageable to parse. 
