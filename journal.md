2022-09-27

Concept of the project determined:
Generate synthetic data of renewable energy input (wind/solar) for energy system modeling
The data is idealy a complicated spatio-temparol time-series. Not yet sure whether daily or houly


2022-09-29
Added references about:
1. Why not adding hydrogen predictions along with solar/wind
2. GANs the most mature and sucessful model so far
3. Diffusion model the current edge research direction, no publication so far

Data aquired from previous publications: daily data for Texas.

2020-10-10
Added code and Excel about how to fetch weather data 
(including temperature data) from public database.
Confirmed that although the data time series resolution is suitable for the study
it need extra spatial resolution and processing

2020-20-14
Confirmed source code for GANs model.
The previous work on this front can use Gan to do:
1. time series scenario generations
2. spatially correlated time series generations (maintain spatial correlation only, can add noise)
3. conditional time series scenario generation (by labeling input training data)

Further investigation of the methodology shows that GAN can also be used for scenario forecast.
But subjected to many uncertainties.

Next steps:
testing the GANs code downloaded from Github, make sure to reproduce the results first
Then try to run the single time-series generation with longer data input.

Thinkings:
Do we have better ways to incoperate the spatial correlation??
What are the computational load limits??


