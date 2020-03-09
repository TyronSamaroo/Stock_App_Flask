```
.
├── Procfile
├── ReadMe.md
├── requirements.txt
├── run.py
└── stockapp
    ├── __init__.py
    ├── database.db
    ├── forms.py
    ├── models.py
    ├── request.py
    ├── routes.py
    ├── static
    │   └── main.css
    └── templates
        ├── account.html
        ├── home.html
        ├── layout.html
        ├── login.html
        ├── main.html
        ├── portfolio.html
        ├── register.html
        └── transaction.html
```
# Project Requirements 

# Essential
Python Version 3.7 or higher

#### On Terminal or Windows Command Prompt follow these instructions 

On macOS and Linux      
`python3 -m venv env`       
On Windows:             
`py -m venv env`      
to make a virtual enviorment specific to the application. This will make sure that everything installed will be only for the project and not your overall system.

# Activate Enviroment 
On macOS and Linux      
`source env/bin/activate `       
On Windows:             
`\env\Scripts\activate.bat`    

# Installing Dependencies 

In main directory run command  
On macOS and Linux      
`pip install -r requirements.txt`

On Windows:                         
`py install -r requirements.txt`


# Run Application

`flask run`

All local environment configuration is located in the .flaskenv file





