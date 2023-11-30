# Requirements 
## Functional Requirements
1. *Create and Save New Notes - Users can create new text notes and save them to their account (Akhil)
2. Starred Notes - Users can star notes to have them display on a different page  (Akhil)
3. *Delete Notes  - Users can delete written notes (Akhil)
4. *Create an Account - Allowing users to create an account to use the app (Hoang)
5. Log in - Allowing users to log into their account to access the app (Hoang)
6. Log Out - Allowing the user to sign out of their account in the app (Hoang) 
7. Search Function - Allows user to search for a specific note by keyword or title (Gautam)
8. Lock File Function - Allows user to lock each file with a password for privacy/security (Gautam)
9. File to Folder Organization - Allows the user to organize each note into different folders or organize them by tags(Gautam)
10. Note Sharing - Allow users to share their notes publicly or privately with other users. (Steve)
11. Note Export - Allow users to export their notes to different formats, such as PDF, Word, or .txt (Steve)
12. Collaboration - Allow users to collaborate on notes with other users (Steve)
13. Insipirational Qoutes (External API) - User can see an inspirational qoute upon every navigation to dashboard (Akhil)
14. Translate Function (Externa1 Google Translate API) (Gautam)
 
## Non-functional Requirements
1. *The website should be operate on all exist operation systems.
2. The website should be able to handle more than 10 users.

## Use Cases 
**1. Create and Save New Notes (Akhil) - Milestone is one week after UI is built out**
- **Pre-condition:** User is logged in and has an account
- **Trigger:** User clicks create a new note button
- **Primary Sequence:**
1. The user clicks on the "Create Note" Button
2. The user is taken to a new page with a blank note
3. The user enters text for the new note
4. User clicks on the "Save" button
5. System saves and confirms that the note is saved to the user
- **Primary Postconditions:** A new note is created and saved to the user's account
- **Alternate Sequence:** 
1. The user does not enter any text and clicks "Save"
2. The system tells users they can not make an empty note

**2. Starred Notes (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in and has notes
- **Trigger:** User clicks the starred button on a note
- **Primary Sequence:**
1. User navigates to the notes dashboard
2. The user clicks "Star" checkbox
6. The system will render the starred note on an important note page
- **Primary Postconditions:** User is able to see the starred note on an important page
- **Alternate Sequence:** 
1. The user did not select the Star checkbox
   
**3. Delete Note (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in to the dashboard
- **Trigger:** User click the delete note button on a note
- **Primary Sequence:**
1. User navigates to dashboard
2. User clicks "delete" button
4. System removes note from database and from viewable screen
- **Primary Postconditions:** Selected note is no longer in database
- **Alternate Sequence:** 
1. The user did not click on delete button


**4. Create an Account (Hoang)** [account](images/Sign_Up.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Create Account" button
- **Primary Sequence:**
1. User selects the "Create an Account" button on the app 
2. The user fills in their desired username and password and other information required
3. User then click on the "Create" button
4. The system will confirm the account create
- **Primary Postconditions:** The System will save the account and tell the user whether it was a success or not
- **Alternate Sequence:** 
1. User did not enter an email for the account
2. The system will alert the user to enter the missing field for information

**5. Log in (Hoang)** [log_in](images/Login_Page.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Log In" button on the app 
3. User fills in their username and password
4. User click on the "Submit" button to log in
- **Primary Postconditions:** The System will check the account credentials and log into the user account
- **Alternate Sequence:** 
1. The user did not enter the correct username or password

**6. Log Out (Hoang)** [log_out](images/Log_Out.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User finish logging in and chooses the option "Log Out"
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Log In" button on the app 
3. User must successfully log into their account
4. The user chose the option "Log Out"
- **Primary Postconditions:** System will successful sign the user out of their account
- **Alternate Sequence:** 
1. The user did not successfully log into their account

**7. Search Function(Gautam)**
- **Pre-condition** User is logged into the app
- **Trigger:** User wants to search for a specific note 
- **Primary Sequence:** 
1. User navigates to the Search Bar
2. The user types in the title/tag associated with the note
3. The user clicks on the enter button 
4. The system displays a list of note pages related to the keyword/tag
- **Primary Postconditions:** User is able to choose from the given list of notes 
- **Alternate Sequence:**
1. The system does not display a list of notes due to the keyword/tag not matching 
2. The system displays a message of "No notes were found"
3. The user can exit or try again with a new keyword

**8. Lock File Function(Gautam)**
- **Pre-condition*:** User is logged into the app and is on a specific note page
- **Trigger:** User wants to lock a note file for privacy
- **Primary Sequence:**
1. The user navigates to the Lock File button in the top right corner 
2. The user clicks on the Lock File Button
3. The system displays a box asking the user to input their account password 
4. The system displays a text message saying, "Note has been locked"
- **Primary Postconditions:** The note is locked and cannot be accessed unless a password is entered
- **Alternate Sequence:**
1. The user is not able to lock the file due to an incorrect password or forgotten password
2. System displays incorrect password message
3. The system displays a "try again" button and a "forgot password" button
4. The user clicks on either one

**9. File to Folder Organization(Gautam)**
- **Pre-condition*:** User is logged into the app 
- **Trigger:** User wants to organize a note to a specific folder
- **Primary Sequence:**
1. User navigates to the "Create Folder" button 
2. The user clicks on the "Create Folder" Button
3. System displays a text box to name the folder 
4. The user names the folder
5. The system displays a list of note files that the user can add 
- **Primary Postconditions:** The folder that was created contains note files that the user wanted to add and is organized
- **Alternate Sequence:**
1. The user chooses to add a subfolder within the folder
2. System displays add a new folder button
3. The user clicks the button
4. System displays a text box to name the folder
5. The system displays a list of note files that the user can add

**10. Note Sharing (Steve)** 
- **Pre-condition:** User has created a note
- **Trigger:** User wants to share the note with another user
- **Primary Sequence:**
1. The user selects the note they want to share
2. The user clicks the "Share" button
3. The user enters the email address of the user they want to share the note with
4. The user selects the desired access level (read or write) for the shared user
5. The user clicks the "Share" button
- **Primary Postconditions:** The shared user receives an email with a link to the note & can access the note with the specified access level
- **Alternate Sequence:** 
1. If the shared user does not have an account, they will be prompted to create one

**11. Note Export (Steve)** 
- **Pre-condition:** User has created a note
- **Trigger:** User wants to export the note to a different format
- **Primary Sequence:**
1. The user selects the note they want to export
2. User clicks the "Export" button
3. The user selects the desired export format
4. User clicks the "Export" button
- **Primary Postconditions:** The note is exported to the selected format & saved to the user's computer
- **Alternate Sequence:** 
1. If the user does not have the required software to open the exported file, they will be prompted to download it

**12. Collaboration (Steve)** 
- **Pre-condition:** Multiple users have access to a note
- **Trigger:** One user starts editing the note
- **Primary Sequence:**
1. The user's changes are broadcast to all other users in real-time
2. All other users see the changes reflected in the note
3. Users can collaborate on the note in real-time
- **Primary Postconditions:** The note is updated with the collective contributions of all users & all users have a consistent view of the note
- **Alternate Sequence:** 
1. If there is a conflict between changes made by different users, a conflict resolution mechanism will be used to determine which change is accepted

**13. Insipirational Quotes (External API) (Akhil) - Milestone is once dashboard page is created**
- **Pre-condition:** User is logged in to the application
- **Trigger:** User navigation to dashboard
- **Primary Sequence:**
1. User navigates to dashboard
2. System queries insipirational quote website and displays quote on dashboard
3. User can choose to read the quote as it will be displayed when they are navigating around
- **Primary Postconditions:** Quote is cleared from memory upon navigation away from dashboard page
- **Alternate Sequence:** 
1. The user is not logged in and navigates to dashboard, system should not query api

**14. Translate Function (Externa1 Google Translate API) (Gautam)**
- **Pre-condition:** User is logged in to the application
- **Trigger:** User starts adding notes to a note files
- **Primary Sequence:**
1. User navigates to Translate button 
2. User clicks on translate button
3. System displays a list of language they can convert the text into using API
4. User selects a language
5. System displays text into the language that was chosen
- **Primary Postconditions:** The note is updated with a new language
- **Alternate Sequence:** 
1. The user chooses not to translate
2. User clicks on "Revert Translation"
3. System displays the text in the original language

