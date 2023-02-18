# Stitch.ai - Full Stack AI Healthcare App

Stitch.ai is a story-based social community which helps connect people suffering from similar health conditions using the power of Natural Language Processing.

## CodeJam(XI) Winner
Devpost: [https://devpost.com/software/stitch-ai](https://devpost.com/software/stitch-ai) 

Demo: [https://www.youtube.com/watch?v=HFv41modKwI](https://www.youtube.com/watch?v=HFv41modKwI)

Website: [https://stitch-srsefll6ha-uc.a.run.app/](https://stitch-srsefll6ha-uc.a.run.app/)
 
## Home Page

![https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/854/348/datas/gallery.jpg](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/854/348/datas/gallery.jpg)

## Matching

![https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/854/350/datas/gallery.jpg](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/854/350/datas/gallery.jpg)

## Inspiration

Research says 43.5% of people experiencing severe health conditions often/always feel lonely and struggle to form meaningful connections because people don’t always understand what they’re exactly going through. This leads to loneliness and severe depression which has increased early mortality by 26%.
Our aim at Stitch.ai is to stitch these communication barriers between people facing similar medical conditions and empower them with the magic of AI.

## What it does

Stitch.ai is a social web application tailored towards connecting and empowering people suffering from similar health conditions, so they have someone to talk to and relate to.  A user will enter their story and the Amazon Comprehend NLP Model extracts the medical conditions based on the text. Then, our matching algorithm matches all users having the same medical conditions and the user can see the stories of all other matched users and can connect with them. The user can also share their own story with other people struggling with similar conditions.

## How we built it

To build the front-end, we started off with **Javascript**, but resorted to **Streamlit** due to time constraints. We used **Firebase Realtime Database** for for secure user authentication and storing stories, health conditions etc. For extracting medical entities, we used **Amazon Comprehend Medical API** which uses **Natural Language Processing (NLP)** to extract medical conditions from text (user stories). Finally, we implemented our very own user matching algorithm using **Hash Maps** we learnt in Comp 250, which is pretty fast as well! 

## Challenges we ran into

This was the first time we worked with a database (Firebase), and we had to read a lot of documentation and figure things out by ourselves. We also struggled a bit on developing an algorithm to match users based on medical conditions and we decided to implement our learning of Hash Maps which took a great deal of brainstorming! We also had a tough time setting up the AWS Comprehend API for NLP because we didn't have much experience working with API's before. 

## Accomplishments that we're proud of

We are very proud that we could create something that will actually be of help to so many people and will connect people together. This is the first hackathon for majority of us and we are very happy to **stitch** (no pun intended) all our ideas into an amazing web application!

## What we learned

This project has taught us so much! We learnt how to collaborate together and work in a team. We learnt about different types of databases and also had first-hand experience working in Firebase. We also learnt a great deal about working with APIs too. Moreover, we ourselves learnt more about the importance of making people feel connected with each other to fight mental health issues. 

## What's next for Stitch.ai

We have so many things planned for Stitch.ai. Some ideas are:

**stitChat**: We plan to incorporate chat features to our Stitch.ai. which would enable users to directly contact their matches from the app which we plan to do using React Routing, React Context API and Chat Engine API. 
 
Furthermore, our future prospects include a resource recommender system based on health conditions, analytics and professional support which would connect users to doctors and healthcare professionals.





