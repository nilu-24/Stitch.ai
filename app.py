#importing necessary libraries
from json import load
import pyrebase
import streamlit as st
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
import boto3


#firebase config
firebaseConfig = {
  'apiKey': "********************************",
  'authDomain': "********************************",
  'projectId': "********************************",
  'storageBucket': "********************************",
  'messagingSenderId': "********************************",
  'appId': "********************************",
  'measurementId': "********************************",
  'databaseURL': "********************************"
}

#Firebase Auth
firebase = pyrebase.initialize_app(firebaseConfig) #initializing the firebase app

#Initiazing auth, db, storage

authentication = firebase.auth()
database = firebase.database()
storage = firebase.storage()

#Fetching AI for detecting medical key terms and conditions

def detectEntities(inputText):

  if inputText=="":
    return ["No Medical Condition Detected"]

  medComprehend = boto3.client(service_name='comprehendmedical', region_name='ca-central-1')
  entities= medComprehend.detect_entities(Text = inputText)
  conditions = []
  for entity in entities["Entities"]: #looping through all entities
    if entity["Category"]=="MEDICAL_CONDITION": #if it is a medical condition
      conditions.append(entity["Text"]) #add it to list of conditions

  if len(conditions)==0:
    return ["No Medical Condition Detected"]

  return conditions

#function to fetch the lottie animation
def load_lottie_url(url:str):
  x = requests.get(url)
  if x.status_code != 200:
    return None
  return x.json()


#Lottie Animations
medical = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_pk5mpw6j.json")
support = load_lottie_url("https://assets4.lottiefiles.com/private_files/lf30_wwq2op12.json")
penguin = load_lottie_url("https://assets4.lottiefiles.com/private_files/lf30_ttgwkuhd.json")
feeds_logo = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_5e7wgehs.json")

c1,c2 = st.columns(2)
with c1:
  st.title("Stitch.ai")
  st.subheader("A Story Driven Community")
  st.write("Empowering people facing health challenges with the magic of AI.")
with c2:
 st_lottie(support,
height=200,
width=200)


# Creating the Login Page
st.sidebar.title("Get Started 📖")
sidebar = st.sidebar.radio("Log In / Sign Up",["Log In","Sign Up"])
email = st.sidebar.text_input("Email: ")
password = st.sidebar.text_input("Password: ",type="password")


#Login and auth and web app functionality
if sidebar=="Log In":
  login_check = st.sidebar.checkbox("Log In")

  with st.sidebar:
    st_lottie(medical)

 
  if login_check:
    user = authentication.sign_in_with_email_and_password(email,password)
    navbar = st.radio('Page Navigation',('Home 🏠','Feed 📃', 'Resources 😃','Profile 🐧'))
    if navbar=="Home 🏠":
      cl1,cl2 = st.columns(2)
      with cl1:
        st.header("Welcome, "+database.child(user['localId']).child("Name").get().val()+"!")
        st.subheader("You Matter. Your Story Matters. Share Your Story:  ")
      with cl2:
        st_lottie(penguin, height=180,width=180)
      
      inputText = st.text_area('Start Away...') #text is stored in this variable
      extract = st.button("Share")
    
      if extract:
        st.subheader("Medical Conditions Extracted: ")
        database.child(user['localId']).child("Story").set(inputText)

        med_conditions = detectEntities(inputText)

        for i in range(len(med_conditions)): #converting to upercase
          med_conditions[i]=med_conditions[i].upper()

        hash_map = {} #using hashmap to store the condition : name pair

        for med_con in med_conditions:
          hash_map[med_con] = database.child(user['localId']).child("Name").get().val()
        
        database.child(user['localId']).child("Conditions").set(hash_map)
        


        for condition in med_conditions:
          st.write(condition)

  
    if navbar=="Feed 📃":
      st.header("Welcome to your Feed!")
     
      #showing posts 
      all_names = []
      all_maps = []
      total_users = database.get()

      for conditions in total_users.each():
        all_maps.append(conditions.val()["Conditions"])

      common_users = []
      
      for i in range(len(all_maps)):
        for key in database.child(user['localId']).child("Conditions").get().val(): #first is the main users hashtable
          if key in all_maps[i]:
            common_users.append(list(all_maps[i].items())[0][1])

      common_users = list(set(common_users)) #converting to a hashset to remove duplicate names
      common_users.remove(database.child(user['localId']).child("Name").get().val()) #remove yourself
      if len(common_users)==0:
          st.subheader("Sorry, we were unable to find a match for you right now 😢")
      if len(common_users)>0:

        st.subheader("You've matched with: ")


        for x in common_users:
            st.success(x)
    
        m,n = st.columns(2)
        with m:
          st.header("Similar Journeys")
          st.subheader("Connect with people who have been in your shoes...")
        with n:
           st_lottie(feeds_logo,height=200,width=200)

        all_stories = database.child(user['localId']).child("Story").get().val()

        for i in total_users.each():
            if(i.val()["Name"] in common_users):
                st.subheader(i.val()["Name"]+"'s "+"Story: ")
                st.info(i.val()["Story"])
                st.write("Reach out to "+i.val()["Name"]+ " at: "+ i.val()["Email"])

     
    if navbar=="Profile 🐧":
      story_text = database.child(user['localId']).child("Story").get().val()


      st.header("Your Profile: ")
      st.subheader("Your Story:")
      st.success(story_text)

      medi = st.button("Show Detected Medical Conditions")
      d =  database.child(user['localId']).child("Conditions").get().val()

      if medi:
        for condition in d:
          st.info(condition)



    if navbar=="Resources 😃":

      st.header("You're not Alone.")
      st.subheader("Here are some resources to support you:")

      one,two,three = st.columns(3)
      with one:
        st.subheader("keep.meSAFE")
        st.write("keep.meSAFE’s innovative Student Support Program (SSP) helps students by promoting early intervention and 24/7 access to mental health support")
        st.write("https://www.keepmesafe.org")

      with two:
        st.subheader("McGill Wellness Hub")
        st.write("The Hub provides McGill students access to health and wellness services. Whether you want to build your wellness community, access a clinician, learn a new skill, or relax in our space, the Student Wellness Hub is here for you! https://www.mcgill.ca/wellness-hub/")

      with three:
        st.subheader("The Canada Suicide Prevention Service")
        st.write("If you’re thinking about suicide, are worried about a friend or loved one, the Canada Suicide Prevention Service is available 24/7 for voice and 4pm to 12am ET for text.")
        st.write("https://www.crisisservicescanada.ca/en/")





# For signing in the new user and authentication

if sidebar =="Sign Up":
  name = st.sidebar.text_input("User Name: ")
  submit = st.sidebar.button("Create Account")
  with st.sidebar:
    st_lottie(medical)

  if submit:    
    #create the user
    user = authentication.create_user_with_email_and_password(email,password)
    st.balloons()
    #database structure
    database.child(user['localId']).child("Name").set(name)
    database.child(user['localId']).child("ID").set(user["localId"])
    database.child(user['localId']).child("Email").set(email)

    st.title("Welcome, "+name+"!")
    st.success("Success! You can now login to your account!")



