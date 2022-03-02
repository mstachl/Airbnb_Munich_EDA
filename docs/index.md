# Staying in Munich - an AirBnB study

![image](https://user-images.githubusercontent.com/8439378/155898926-44037c38-630d-4cfb-89f4-5ebc7fd79d8a.png)

## Introduction

I am an avid traveller and often end up at AirBnBs when looking for cheap and individual accommodation during my trips. As I am fairly familiar with what to look for when am I go abroad to other countries, but never use them in my own backyard, I want to dive into AirBnB data in my own hometown, Munich. For this project I use data collected via [http://insideairbnb.com/munich](http://insideairbnb.com/munich/) to better understand:

  1. How is the overall price level for staying in Munich?
  2. What neighborhoods are the most expensive/cheapest?
  3. During what time is the trip to Munich most/least expensive?
  4. What are the most common amenities and are they influencing the overall price level?

> InsideAirbnb is a mission driven activist project with the objective to: Provide data that quantifies the impact of short-term rentals on housing and residential communities; and also provides a platform to support advocacy for policies to protect our cities from the impacts of short-term rentals.
>
> -- <cite>Inside Airbnb</cite>

The dataset gathered was scraped on 24.12.2021 and contains 4641 AirBnB listings - meaning lodgings and housings - including several features offered including but not limited to Wifi, security features, hygienic conveniences and other amenities. The dataset also contains prices for 2022 that were set in advance by the host for the listings.

## Part 1: How is the overall price level for staying in Munich?

The data contained heavy outliers (>5000 $ per night per listing). I excluded listings using the [Inter Quartile Rule](https://en.wikipedia.org/wiki/Interquartile_range). 

From the dataset we can spot that rounded prices (30$, 40$, 50$ etc.) seem to be present above average. This might indicate that hosts prefer rounded prices instead of "uneven" prices. Besided that, the data seems to be right-skewed with a mean of around 38$ per night per person (see dashed line). The median is even lower at 35$ per night per person.

![image](https://user-images.githubusercontent.com/8439378/156415719-b770df08-d632-4636-9cba-305390a0b1ba.png)


## Part 2: What neighborhoods are the most expensive/cheapest?

Let us now dive in and see the price distribution in different districts in Munich. This comes handy when tourists are planning to visit Munich e.g. on a budget. So in that case, where would they go? Can I give any recommendations for areas they might look at?
In the map below we see the distribution of AirBnB listings on a map of Munich.

![image](https://user-images.githubusercontent.com/8439378/156416890-0ace4860-68d3-4119-9db2-6809533fad82.png)

From the color coding it does not seem obvious right away that one district is in general more expensive than another one. So let us now have a closer look at the average price per person per district.

![image](https://user-images.githubusercontent.com/8439378/156255520-5331b2af-2879-4731-8bed-defc4425ac89.png)

That is interesting. The most expensive areas in Munich seem to be

- Altstadt-Lehel (48$ on avg.),
- Ludwigsvorstadt-Isarvorstadt (44$),
- Maxvorstadt (41$) and
- Schwanthalerhöhe (40$).

Least expensive are

- Sendling-Westpark,
- Aubing-Lochhausen and
- Feldmoching-Hasenbergl (all around 30$).

This aligns well with the typical assumption that the city-center is more expensive than the suburbs. Another reason might be that those regions tend to be close to the Oktoberfest area.
Now we know that there in fact is some gradient between the different city districts. This indicates that the neighbourhood in fact is a factor in terms of determining housing prices.

## Part 3: During what time is the trip to Munich most/least expensive?

The next question I asked myself is, if there might be a time where Munich in general is more expensive than at other times. In fact from hearsay I got to know that during the time of Oktoberfest (end of September, beginning of Oktober) Munich is generally overpriced. So let us have a look at the time curve for the average listing price.
![image](https://user-images.githubusercontent.com/8439378/156264291-baca2c16-7fdf-4278-8417-7b7b1b9edd91.png)

Plotting the data we see the following:

- We observe a **positive trend over the year**, meaning increasing prices. In fact we have a general yearly increase of ~2.8%, presumably accounting for inflation.
- There is asharp increases end of September until beginning of October. This time frame matches exactly with the famous Oktoberfest, unterlining the previous guess. It's Bierzelt-time!
- The sharp peak at the end of Oktober was surprising to me at first, but after some research my educated guess is it's accounted to the [BAUMA](https://bauma.de/en/), the world's leading exposition for construction machinery.
- We also see some kind of seasonality. A closer look suggests that housing prices in Munich **are lower on average by 2$ on Friday and Saturday compared to the remaining weekdays**, which is really surprising.

## Part 4: What are the most common amenities and are they influencing the overall price level?

Seeing the graph below, the most frequent amenities offered in a listing are Wifi, a kitchen, heating and other essentials. 
![image](https://user-images.githubusercontent.com/8439378/156413012-d4e0580c-e6c8-4fd9-bab8-52c9699ae23d.png)

From the host's side of view, it is intiguing to know, if adding some "goodies" can actually positively influence the askable price for the host's listing. So let us have a look at the correlation coefficients between price and the most influencial amenities.
![image](https://user-images.githubusercontent.com/8439378/156413350-5c2cf6b0-8be9-4c35-8acf-8543141e239f.png)

From the graph above we see that people tend to favor safe houses (security camera, aafe) and well-equiped homes (elevator, gym, HDTV, air conditioning etc.) and also tend to pay a little extra for these conveniences. Nevertheless these conclusions need to be treated with care, as none of the amenities seem to have a statisticallly significant effect on the price.

## Conclusion:

In this article, I took a look at housing prices from AirBnB using data gathered by insideAirBnB in Dezember 2021.

- The average **price per person per night is 38 \$**. Typically hosts tend to ask for "rounded" prices (30 \$, 40 \$, 50 \$ etc.). The average **price per housing is 95 \$**.
- The **most expensive areas in Munich** seem to be Altstadt-Lehel (48 \$ on avg.), Ludwigsvorstadt-Isarvorstadt (44 \$), Maxvorstadt (41 \$) and Schwanthalerhöhe (40 \$).
- **Least expensive** seem to be Sendling-Westpark, Aubing-Lochhausen and Feldmoching-Hasenbergl (30 \$).
- Price per night seems to **increase by ~2.8% in 2022**, aligning well with inflation.
- Stays are **especially expensive during Oktoberfest (~160 \$** per day and accommodation from 17.09.-04.10.2022) **and during the BAUMA (~164 \$ per day and accommodation from 23.10.-28.10.2022)**. BAUMA is the world's leading exposition for construction machinery.
- Most offered amenities are **Wifi, kitchen, smoke alarm and hair dryer**, but amenities in general don't seem to have a huge impact on the asked price.

The findings here are observational, not the result of a formal study. So the real question remains:

#### *Are you going to visit Munich in 2022 and if yes, do you plan to use AirBnB?*

Cheers,

![image](https://user-images.githubusercontent.com/8439378/156263912-e4a7a342-3409-47cd-ac5b-5552f22849fa.png)
