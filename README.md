# Decision Making solution for ride sharing drivers

## DESCRIPTION

This package is the project by team 150 from CSE 6242 @ Georgia Tech. The project is about “Decision Making solution for ride sharing drivers”. The package has files for each of the step Data preparation, model creation and visualization. 

### Note: This app live demo can be accessed through the online hosted version http://smart-drive-app.herokuapp.com/

## How to run the app locally.

* Copy the contents of D3_Dashboard folder to your machine
* Navigate to the folder and run any web live server inside the folder (you can use Python http.server package or node.js live-server)
* open the home.html file to load the web interface for the app.
* Hover over different community areas to see the predicted revenue, tip and COVID-19 effect.


### Folder Structure
    .
    ├── CODE
    │   ├── D3_Dashboard          # The final version of the project web interface (d3 viz with the predicted data)
    │   └── Project_Code          # All the code base used to acquire, clean, process and present the data.
    ├── DOC 
    │   ├── team150report.pdf     # Final project writeup
    │   └── team150poster.pdf     # Final project poster
    └── README.txt




## Project Implementation Code

### Data preparation
Data_Prep folder has ipynb code to extract the data using API & generate aggregated results, Spark code to generate aggregated results directly from uploaded CSV and cleansed and aggregated output datafile to be used by model. 
### Model Creation
Python code package for model creation, training model and predicting the results in csv file.Contains both code as well as static output CSV file. 
### Visualization  
.html file with d3.js code for visualization.   

------



## INSTALLATION 

### Create virtual environemnt for python and install required libraries (for windows)  
Install python 3.7 
Create new directory for the project and run the following command  : python -m venv newenv
Activate the newly created enviroment : newenv\Scripts\activate
Install required libraries using requirement.txt , (copy requirement.txt file to project directory) : pip install -r requirement.txt
To Deactivate virtural enviroment: Deactivate

#### Data Preparation
Install SQLlite3 and Jupiter notebook for data preparation step.Use created virtrual enviroment for python in jupiter notebook.

#### Model 
No seperate installation is needed for model execution except python 3.7 and required libraries in requirement.txt 

#### Visualization
No seperate installation is needed for visualization

## EXECUTION

### Data preparation 
Option1 : For preparing the data, run ipynnb to prepare the aggregated output csv file for model input. 

Chicago_pub.ipynb: To get the data we use the Site API (Socrata link) iterating through all the months in the dataset and modifying the API request to get one month at a time to avoid RAM saturation. Also, information was aggregated month by month to reduce the space needed (~55GB vs less than 5GB).

Option2 : Another way to prepare the aggregated data is using AWS cloud platform services. Upload all datafiles to AWS S3 storage bucket account, change S3 input and output bucket name in  data_prep_pyspark.py and run the notebook on AWS glue as Spark job. 
Output file will be generated in S3 storage bucket. No installation is required but upload all the datafiles to S3 is time consuming process. 

### Model Creation

Utilizing the output csv from the data preparation, save the csv in the 2. Output for Viz folder and name the file "trips_summary_covid_pub.csv" (or rename the file to whatever you'd prefer and update the csv name in main_poisson.py on line 8 and in the main_multi.py file on line 6).

Run file main_poisson.py from virtual evniroment to generate prediction output CSV file. 

### Visualization

### Execution of code/application: 

DEMO LINK: 







