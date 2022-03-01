# Introduction

![image](https://user-images.githubusercontent.com/8439378/155898926-44037c38-630d-4cfb-89f4-5ebc7fd79d8a.png)

I am an avid traveller and often end up at AirBnBs when looking for cheap and individual accommodation during my trips. As I am fairly familiar with what to look for when am I go abroad to other countries but never you them in my own backyard, I want to dive into AirBnB data in my own hometown, Munich. For this project use data collected via [http://insideairbnb.com/munich](http://insideairbnb.com/munich/) to better understand:

  1. How is the overall price level for staying in Munich?
  2. What neighborhoods are the most expensive/cheapest?
  3. During what time is the trip to Munich most/least expensive?
  4. What are the most common amenities and are they influencing the overall price level?

>Inside Airbnb is a mission driven activist project with the objective to: Provide data that quantifies the impact of short-term rentals on housing and residential communities; >and also provides a platform to support advocacy for policies to protect our >cities from the impacts of short-term rentals.
>
> -- <cite>Inside Airbnb</cite>

The dataset gathered was scraped on 24.12.2021 and contains 4641 AirBnB listings - meaning lodgings and housings - including several features offered including but not limited to Wifi, security features, hygienic conveniences and other amenities. The dataset also contains prices for 2022 that were set in advance by the host for the listings.

## Part 1: How is the overall price level for staying in Munich?

The data contained heavy outliers (>5000 $ per night per listing). I excluded listings using the [Inter Quartile Rule](https://en.wikipedia.org/wiki/Interquartile_range).

## Part 2: What neighborhoods are the most expensive/cheapest?
## Conclustion:

In this article, I took a look at housing prices from AirBnB using data gathered by insideAirBnB in Dezember 2021.

- The average **price per person per night is 38 \$**. Typically hosts tend to ask for "rounded" prices (30 \$, 40 \$, 50 \$ etc.). The average **price per housing is 95 \$**.
- The **most expensive areas in Munich** seem to be Altstadt-Lehel (48 \$ on avg.), Ludwigsvorstadt-Isarvorstadt (44 \$), Maxvorstadt (41 \$) and Schwanthalerhöhe (40 \$).
- **Least expensive** seem to be Sendling-Westpark, Aubing-Lochhausen and Feldmoching-Hasenbergl (30 \$).
- Price per night seems to **increase by ~2.8% in 2022**, aligning well with inflation.
- Stays are **especially expensive during Oktoberfest (~160 \$** per day and accommodation from 17.09.-04.10.2022) **and during the BAUMA (~164 \$ per day and accommodation from 23.10.-28.10.2022)**. BAUMA is the world's leading exposition for construction machinery.
- Most offered amenities are **Wifi, kitchen, smoke alarm and hair dryer**, but amenities in general don't seem to have a huge impact on the asked price.

The findings here are observational, not the result of a formal study. So the real question remains:

*<font size="4">*Are you going to visit Munich in 2022 and if yes, do you plan to use AirBnB?*</font>
