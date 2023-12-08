# Requirements 
## Functional Requirements
1. *Create and Save New Notes - Users can create new text notes and save them to their account (Akhil)
2. Starred Notes - Users can star notes to have them display on a different page  (Akhil)
3. Delete Notes  - Users can delete written notes (Akhil)
4. Create an Account - Allowing users to create an account to use the app (Hoang)
5. Log in - Allowing users to log into their account to access the app (Hoang)
6. Log Out - Allowing the user to sign out of their account in the app (Hoang) 
7. Search Function - Allows user to search for a specific note by keyword or title (Gautam)
8. Edit user profile - User will be able to go into their account to see their info (Gautam)
9. File to Folder Organization - Allows the user to organize each note into different folders or organize them by tags(Gautam)
10. Dashboard - This is where the user can user the app features (Steve)
11. Password reset - Allow users to reset their password (Steve)
12. Edit Notes - Allow users to make changes to exisitng notes (Steve)
13. *Insipirational Quotes (External API) - User can see an inspirational qoute upon every navigation to dashboard (Akhil)
14. *Translate Function (Externa1 Google Translate API) (Gautam)
 
## Non-functional Requirements
1. *The website should be operate on all exist operation systems.
2. The website should be able to handle more than 10 users.

## Use Cases 
**1. Create and Save New Notes (Akhil) - Milestone is one week after UI is built out**
- **Pre-condition:** User is logged in and has an account
- **Trigger:** User clicks create a new note button
- **Primary Sequence:**
1. The user is taken to a new page with a blank note
2. The user enters text for the new note
3. User clicks on the "Save" button
4. System saves and confirms that the note is saved to the user
- **Primary Postconditions:** A new note is created and saved to the user's account
- **Alternate Sequence:** 
1. The user does not enter any text and clicks "Save"
2. The system tells users they can not make an empty note

**2. Starred Notes (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in and has notes
- **Trigger:** User navigate to the star notes on dashboard
- **Primary Sequence:**
1. The user clicks "Star" button
2. The system will render the starred note on an important note page
- **Primary Postconditions:** User is able to see the starred note on an important page
- **Alternate Sequence:** 
1. The user did not select the Star checkbox
   
**3. Delete Note (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in to the dashboard
- **Trigger:** User select a note
- **Primary Sequence:**
1. User clicks "delete" button
2. System removes note from database and from viewable screen
- **Primary Postconditions:** Selected note is no longer in database
- **Alternate Sequence:** 
1. The user did not click on delete button


**4. Create an Account (Hoang)** [account](images/Sign_Up.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Create Account" button
- **Primary Sequence:**
1. The user fills in their desired username and password and other information required
2. User then click on the "Create" button
3. The system will confirm the account create
- **Primary Postconditions:** The System will save the account and log the user into their account
- **Alternate Sequence:** 
1. User did not enter an email for the account
2. The system will alert the user to enter the missing field for information

**5. Log in (Hoang)** [log_in](images/Login_Page.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button
- **Primary Sequence:** 
1. User fills in their username and password
2. User click on the "Submit" button to log in
- **Primary Postconditions:** The System will check the account credentials and log into the user account
- **Alternate Sequence:** 
1. The user did not enter the correct username or password

**6. Log Out (Hoang)** [log_out](images/Log_Out.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User log into their account
- **Primary Sequence:**
1. User navigated on the dashboard
2. User select the "Log Out" button on the app 
- **Primary Postconditions:** System will successful sign the user out of their account
- **Alternate Sequence:** 
1. The user did not successfully log into their account

**7. Search Function(Gautam)**
- **Pre-condition** User is logged into the app
- **Trigger:** User navigates to the search bar 
- **Primary Sequence:** 
1. The user types in the title associated with the note
2. The user clicks on the enter button 
3. The system displays the note page related to the title
- **Primary Postconditions:** User is able to view the note 
- **Alternate Sequence:**
1. The system does not display a list of notes due to the keyword/tag not matching 
2. The system displays a message of "No notes were found"
3. The user can exit or try again with a new keyword

**8. Edit user profile(Gautam)**
- **Pre-condition:** User is logged into the app and is on the dashboard
- **Trigger:** User navigates to edit user profile button
- **Primary Sequence:**
1. The user clicks on profile button
2. The system will take the user to a different page
3. User answers the security question
4. User edits account details
- **Primary Postconditions:** The system takes the user to dashboard if everything was correctly inputed
- **Alternate Sequence:**
1. The user did not click on the profile button

**9. File to Folder Organization(Gautam)**
- **Pre-condition:** User is logged into the app 
- **Trigger:** User click on the "Create Folder" button
- **Primary Sequence:** 
1. System displays a text box to name the folder 
2. The user names the folder
3. The system displays the folder in the folder area
- **Primary Postconditions:** The folder that was created contains note files that the user wanted to add and is organized
- **Alternate Sequence:**
1. User clicks the add to folder
2. System displays enter box to input title of folder
3. User enters title and clicks enter
4. System displays note under that folder in the folder area

**10. Dashboard (Steve)** 
- **Pre-condition:** User has log into their account
- **Trigger:** User wants to use one of the app features
- **Primary Sequence:**
1. The user select one of the feature on the dashboard
2. The user clicks on that specific feature button that they want
- **Primary Postconditions:** The system will take the user to that specific feature page
- **Alternate Sequence:** 
1. The user did not sign in with their account

**11. Password reset (Steve)** 
- **Pre-condition:** User has created an account
- **Trigger:** User click on the Login page
- **Primary Sequence:**
1. The user selects reset passsword button
2. The user fill out the required information in the reset password page
3. The user click submit
- **Primary Postconditions:** The system will pop up a window saying that user successfully reset their password
- **Alternate Sequence:** 
1. The user enter the wrong required information

**12. Edit Notes (Steve)** 
- **Pre-condition:** User log into their account
- **Trigger:** User created a notes in the dashboard
- **Primary Sequence:**
1. User select the note
2. User click on the edit button
- **Primary Postconditions:** The system will take the user to that specific note
- **Alternate Sequence:** 
1. The user did not create any new notes
2. The user deleted the note they want to change

**13. Insipirational Quotes (External API) (Akhil) - Milestone is once dashboard page is created**
- **Pre-condition:** User is logged in to the website
- **Trigger:** User navigation to dashboard
- **Primary Sequence:**
1. System queries insipirational quote website and displays quote on dashboard
2. User can choose to read the quote as it will be displayed when they are navigating around
- **Primary Postconditions:** Quote is cleared from memory upon navigation away from dashboard page
- **Alternate Sequence:** 
1. The user is not logged in

**14. Translate Function (DeepTranslator library) (Gautam)**
- **Pre-condition:** User is logged in to the application
- **Trigger:** User navigated to the search bar
- **Primary Sequence:**
1. User look up a specific note
2. User click on the language button
3. System displays a list of language they can convert the text into(i.e hindi, spanish, french, etc)
4. User selects a language
- **Primary Postconditions:** The note will be displayed with the selected language
- **Alternate Sequence:** 
1. User chooses not to translate
2. User search for a note that does not exist

