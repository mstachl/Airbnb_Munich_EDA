# # Staying in Munich: an AirBnB study

![image](https://user-images.githubusercontent.com/8439378/155898926-44037c38-630d-4cfb-89f4-5ebc7fd79d8a.png)

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

I am an avid traveller and often end up at AirBnBs when looking for cheap and individual accommodation during my trips. As I am fairly familiar with what to look for when am I go abroad to other countries but never you them in my own backyard, I want to dive into AirBnB data in my own hometown, Munich. 
For this project use data collected via http://insideairbnb.com/munich/ to better understand:

1. How is the overall price level for staying in Munich?
2. What neighborhoods are the most expensive/cheapest?
3. During what time is the trip to Munich most/least expensive?
4. What are the most common amenities and are they influencing the overall price level?

>Inside Airbnb is a mission driven activist project with the objective to:
>Provide data that quantifies the impact of short-term rentals on housing and residential communities; and also provides a platform to support advocacy for policies to protect our >cities from the impacts of short-term rentals.
> -- <cite>Inside Airbnb</cite>

## File Descriptions <a name="files"></a>

There is a notebook available here focused on data retreival, data cleaning and exploratory data analysis.

## Results<a name="results"></a>

- The average price per person per night is 38\\$. Typically hosts tend to ask for "rounded" prices (30\\$, 40\\$, 50\\$ etc.).
- The most expensive areas in Munich seem to be Altstadt-Lehel (48\\$ on avg.), Ludwigsvorstadt-Isarvorstadt (44\\$), Maxvorstadt (41\\$) and Schwanthalerhöhe (40\\$).
- Least expensive seem to be Sendling-Westpark, Aubing-Lochhausen and Feldmoching-Hasenbergl (30\\$).
- Price per night seems to increase by ~2.8% in 2022, aligning well with inflation.
- Stays are especially expensive during Oktoberfest (~160\\$ per day and accommodation from 17.09.-04.10.2022) and during the BAUMA (~164\\$ per day and accommodation from 23.10.-28.10.2022). BAUMA is the world's leading exposition for construction machinery.
- Most offered amenities are Wifi, kitchen, smoke alarm and hair dryer, but amenities in general don't seem to have a huge impact on the asked price.

## Licensing, Authors, and Acknowledgements<a name="licensing"></a>
<b>Packages</b>: Pandas, Matplotlib, GeoPandas, json

I want to thank http://insideairbnb.com/munich/ for providing up-to-date scrapes of AirBnB listings for worldwide cities.
I also want to thank http://opendatalab.de/projects/geojson-utilities/ for their efforts to provide access to geodata of Germany.
