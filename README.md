# Backend Test - Response  

Answer response for [backend-test](https://github.com/tribehired-devs/backend-test)  

## Installation  
1. Use preferred method for creating virtual environment, (eg. venv, pipenv, pipenv)  
2. Install packages required  
> pip install -r requirements.txt  

## Usage  
1. Run the following command to open endpoints on localhost  
> python3 main.py  
2. Access available endpoints via browser or through requests. Default is [http://127.0.0.1:5000](http://127.0.0.1:5000)  

## Answers  
- Fill (domain) with localhost or custom IP/Port settings. Default is [http://127.0.0.1:5000](http://127.0.0.1:5000)    
1. Question 1    
    - returns top posts ordered by `total_number_of_comments`  

> [GET] [http://(domain)/top](http://127.0.0.1:5000/top)  

2. Question 2  
    - returns list of comments based on filters set in query parameters  
    - query parameter keys based on raw column names, can be added if more columns returned by [comments](https://jsonplaceholder.typicode.com/comments) endpoint    
        - `body`  
        - `name`  
        - `email`  
        - `id`  
        - `postId`  
    - if empty query, returns all comments from [comments](https://jsonplaceholder.typicode.com/comments) endpoint  
  
> [GET] [http://(domain)/search](http://127.0.0.1:5000/search)  
> [GET] [http://(domain)/search?postId=5](http://127.0.0.1:5000/search?postId=5)  
> [GET] [http://(domain)/search?postId=5&body=labor](http://127.0.0.1:5000/search?postId=5&body=labor)  
> [GET] [http://(domain)/search?postId=5&email=co](http://127.0.0.1:5000/search?postId=5&email=co)  