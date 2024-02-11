Project encouraging street cleanups through a reward based system

## Inspiration
Far too often, we pass by streets crowded with litter. One example of this is on UGA game days. If only there were a way to encourage your everyday citizen to pick up a little trash... Of course, this would need to have an incentive. And finding locations for trash would be hard. And it might be too time consuming.
## What it does
Each issue above is solved with our web application **StreetCleanr**

StreetCleanr uses an user-trained AI model that sifts through images of potentially littered streets (perhaps pictures retrieved from a traveling vehicle) and classifies them as 'clean' or 'dirty'. If an image is dirty, our web app takes the images and its location, and marks it as dirty on the map. Then, users will be able to click 'Find A Route'. Upon providing their location, the app automatically gives the user optimal routes to the nearest locations marked with 'dirty'. 

When using this app, users can log in to track their stats and number of "cans". Cans are the built-in currency that users use to redeem rewards. Redeemable rewards range from giftcards, paw points, community service/volunteer hours, or maybe even merch!

Cans are collected by going to the upload tab and providing an image of the location before cleaning, and an image after cleaning. In the future, functionality aiming towards validity would be in place!

Built-in functionality includes:
Reward System: Users redeem rewards using app currency "cans"
Testing AI Model: Users can test the accuracy of the model
Help Us Train: Users can voluntarily contribute to this project by labeling heaps of images as "clean", "dirty", or "unclear"
Find A Route: Users are provided the most optimal routes to 5 nearest 'dirty' locations using Google's Maps API and Distance API
## How we built it

## Challenges we ran into
Where do I start...
Constructing the AI model using tensorflow had adequate documentation, so the setup was manageable. The issues arose when training this model. Specifically, the training data. There's no public dataset of littered or non littered photos, so we decided to get images from google. This was problematic because queries such as 'clean streets' yielded results for dirty streets as well. Even more specific queries had diverse results, which sucks because our hardware capabilities aren't able to scale a dataset large enough to making such results work towards our model. So, the most viable option was manually sifting through data and filtering it out. We built this into our app so that users can assist! Luckily, users can filter 200+ images in only 5 minutes!



## Accomplishments that we're proud of
We're proud of building an AI model for the first time! Also, building such a large scale app with just us two.

## What we learned
We learned a lot about AI models and using tensorflow. Also web development with flask. Also, good time management through projects is a must!

## What's next for StreetCleanr!

We plan to incorporate an actual vehicle to retrieve these images.
Fully functional reward system
Heat map for nearby locations
Government and/or University collaboration

