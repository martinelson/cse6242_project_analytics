# Decision Making solution for ride sharing drivers

## DESCRIPTION

This package is the project by team 150 from CSE 6242 @ Georgia Tech. The project is about “Decision Making solution for ride sharing drivers”. The package has files for each of the step Data preparation, model creation and visualization. 

## Background

Ridesharing services have become a staple in moderntransportation life. A ride to the desired destination is afew clicks away on a mobile device, which is an idea thathas attracted millions of riders and drivers. Companiessuch as Uber and Lyft have amassed remarkable value[1]. These companies use large scale data from cars, dri-vers, traffic lights, maps to come up with sophisticatedalgorithms for pricing, supply and demands forecast.These companies leverage all this information to maxi-mize customer satisfaction and their profits, sometimesat the expense of the drivers. This leaves the driversmore on their own with limited information and /orskills to be more effective [2]. Some studies point thatmost drivers do worse than their opportunity cost (min-imum wage), one of them concludes that 74% of driversearn less than the minimum wage and 30% loss moneyonce all expenses are included [3,4]. In this project, weaim to give drivers valuable information curated to eachdriver’s specific needs. With flexibility in mind, everydriver has different goals that could vary by the day,and our goal is to project earnings and offer data pointsto help them make informed driving choices while theyare offering their labor to the ridesharing economy [5].



### Note: This app live demo can be accessed through the online hosted version http://smart-drive-app.herokuapp.com/

## How to run the app locally.

* Copy the contents of D3_Dashboard folder to your machine
* Navigate to the folder and run any web live server inside the folder (you can use Python http.server package or node.js live-server)
* open the home.html file to load the web interface for the app.
* Hover over different community areas to see the predicted revenue, tip and COVID-19 effect.


### Folder Structure
    .
    ├── CODE
    │   ├── D3_Dashboard          # Final version of web interface (d3 viz with the predicted data)
    │   └── Project_Code          # All the code base used to acquire, clean, process and present the data.
    │       ├── Analytics         # Python codebase used to analyse and test differnet models of the data
    │       └── data_prep         # Pyspark and python codes used to ingest, aggregate and clean the data
    ├── DOC 
    │   ├── team150report.pdf     # Final project writeup
    │   └── team150poster.pdf     # Final project poster
    └── README.txt





