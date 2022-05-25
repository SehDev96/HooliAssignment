# HooliAssignment

### Steps to install this service 
#### Execute the following commands: 

$ git clone https://github.com/SehDev96/HooliAssignment.git <br />
$ cd HooliAssignment <br />
$ docker build --tag python-docker .  <br />
$ docker run python docker <br />

Use the container's endpoint given in the command line 

![image](https://user-images.githubusercontent.com/97646744/170098077-5bee4050-18a3-4c7e-92b7-3b013ec5d66d.png)


### There are three endpoints in this service 

#### 1. /v1/hooli/message 

- This endpoint is a POST request 
- It takes the following request body: 
-  { "sender":"","receiver":"":"message":""}
- The request body should be sent in raw JSON format
- It returns the AI predicted reply

![image](https://user-images.githubusercontent.com/97646744/170160290-5f76ae95-d056-44ee-bd02-fac72eeead3c.png)



#### 2. /v1/restaurant/{restaurant-id} 

- This endpoint is a PUT request 
- It updatest the restaurant records in database 
- It takes the following request body: 
-  {"name":"","hooli_number":""}

![image](https://user-images.githubusercontent.com/97646744/170160359-0b322cd9-37e3-4781-8c80-f75a03766e84.png)



#### 3. /v1/restaurant/{restaurant-id}
- This endpoint is a GET request 
- It returns restaurant record based on id 
- This endpoint is created to test the execution of "/v1/restaurant/{restaurant-id}" (PUT)  endpoint

![image](https://user-images.githubusercontent.com/97646744/170160415-6c4dc81c-537d-4a7d-b1fc-6a26d2b4d3e4.png)

