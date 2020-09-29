# Small_Wheater_Project
## This program makes it possible to consume a weather API, which allows you to collect data from a city and do some treatments, and in addition, you can also get graphs.

#### Here you will find, a guide with all the procedures to make this little climate program. 

Below are the procedures, which are arranged in 3 stages.

***1. Stage) register an account on the RapidAPI website***

   1. You need to register an account on the RapidAPI website to get an API key

   <img src="RapidAPI.png"  width=600>

   2. Go to API Marketplace on navbar and digit **Open Weather Map** on search text area

   <img src="RapidAPI_2.png" width=600>

   3. Now that you have the Key API, choose the Historical Weather Data option
    
   <img src="RapidAPI_3.png" width=600>
   
   4. Grab the code and copy to your editor 
    
   <img src="RapidAPI_4.png" width=600>
    
    
:fire: For more information visit the [How to use an API with Python (Beginner’s Guide)](https://rapidapi.com/blog/how-to-use-an-api-with-python/) on RapidAPI website! :fire:


***2. Stage) Build the program*** 

Below, you can see all the functionalities in my program and its corresponding functions, with all the packages that you need to install 

   * to grap informations that the API gives (def Weather_City) \
```pip install requests``` \
```pip install pprintpp```
   * to convert Timestamp to human date (def Epoch_to_Datetime) \
```pip install DateTime```   
   * to place the data of a chosen weather feature in a list or dictionary (def Hourly_features)
   * to get the average of a chosen weather feature (def Average)
   * to get the maximum value of a chosen weather feature (def Max)
   * to get the minimum value of a chosen weather feature (def Min)
   * to get graphic of a chosen weather feature (def Graphics) \
```pip install matplotlib```

:exclamation: you don´t need to do exatly how i did, you can do in your own way

***3. Stage) Inputs to use the program*** 
   > Choose a city \
   > Get the latidude of the chosen city \
   > Get the longitude of the chosen city \
   > Get the Dt (timestamp) of the chosen city 
