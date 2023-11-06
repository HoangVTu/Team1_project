# Requirements 
## Functional Requirements
1. *Create and Save New Notes - Users can create new text notes and save them to their account (Akhil)
2. *Edit Existing Notes - Users can edit the text of their existing notes (Akhil)
3. Note Reminders - Users can get alerted to go back to a specific note; this will show up on their note page (Akhil)
4. Highlight Text - Users can highlight text within a note (Akhil)
6. *Create an Account - Allowing users to create an account to use the app (Hoang)
7. Log in - Allowing users to log into their account to access the app (Hoang)
8. Log Out - Allowing the user to sign out of their account in the app (Hoang) 
9. Search Function - Allows user to search for a specific note by keyword or title (Gautam)
10. Lock File Function - Allows user to lock each file with a password for privacy/security (Gautam)
11. File to Folder Organization - Allows the user to organize each note into different folders or organize them by tags(Gautam)
12. Dark Mode - User can switch to dark mode(inverted colors) based on preference(Gautam)
13. Note Sharing - Allow users to share their notes publicly or privately with other users. (Steve)
14. Note Export - Allow users to export their notes to different formats, such as PDF, Word, or .txt (Steve)
15. Collaboration - Allow users to collaborate on notes with other users (Steve)
16. Insipirational Qoutes (External API) - User can see an inspirational qoute upon every navigation to dashboard (Akhil)
 
## Non-functional Requirements
1. *The website should be responsive and functional on IOS and Macbooks
2. All webpages should load within 3 seconds - will be tested manually on a Macbook

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

**2. Edit Existing Notes (Akhil) - Milestone is one week after UI is built out**
- **Pre-condition:** User is logged in and has saved notes
- **Trigger:** User clicks the edit button on a note
- **Primary Sequence:**
1. User clicks on the "edit" button on a note
2. The user is taken to that note page and can edit that note
3. The user edits the text
4. User clicks on the "Save" button
5. System saves and confirms that the note is saved to the user
- **Primary Postconditions:** A new note is created and saved to the user's account
- **Alternate Sequence:** 
1. The user does not make any changes and clicks "Save"
2. System exits and tells user no changes were made

**3. Note Reminders (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in and has saved notes
- **Trigger:** User clicks the reminder button in a note
- **Primary Sequence:**
1. User navigates to the notes dashboard
2. The user clicks on the note they want to set a reminder for
3. The user clicks "Set Reminder" Button
4. The user selects the date and time they want a reminder for
5. User clicks on the "Save" button
6. The system saves the reminder and tells the user that the reminder has been set
7. The system will notify the user on top of the dashboard to revisit the note when the date and time arrive
- **Primary Postconditions:** User is alerted when the time for reminder comes
- **Alternate Sequence:** 
1. The user does not select a date and clicks "Save"
2. System alerts users that they have to select the date and time for the reminder

**4. Highlight Text (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in to the Note Editor State
- **Trigger:** User wants to highlight text within note
- **Primary Sequence:**
1. User navigates to notes, edit or create page
2. User selects text to highlight
3. User clicks "Highlight" Button
4. System applies highlight to selected text
5. User clicks on the "Save" button
6. The system saves the text and tells the user a message based on whether the user was in edit or create state
- **Primary Postconditions:** Selected text is highlighted in user's note
- **Alternate Sequence:** 
1. The user does not select any text and clicks on the "Highlight" Button
2. System alerts users they have to select text to highlight


**5. Create an Account (Hoang)** [account](images/Sign_Up.jpg)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Create Account" button
- **Primary Sequence:**
1. User nagivate to the app
2. User selects the "Create an Account" button on the app 
3. The user fills in their desired username and password and other information required
4. User then click on the "Create" button
5. The system will confirm the account create
- **Primary Postconditions:** The System will save the account and tell the user whether it was a success or not
- **Alternate Sequence:** 
1. User did not enter an email for the account
2. The system will alert the user to enter the missing field for information

**6. Log in (Hoang)** [log_in](images/Login_Page.jpg)
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

**7. Log Out (Hoang)** [log_out](images/Log_Out.jpg)
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

**8. Search Function(Gautam)**
- **Pre-condition** User is logged into the app
- **Trigger:** User wants to search for a specific note 
- **Primary Sequence:** 
1. User navigates to the Search Bar
2. The user clicks on the Search Bar
3. The user types in the title/tag associated with the note
4. The user clicks on the enter button 
5. The system displays a list of note pages related to the keyword/tag
- **Primary Postconditions:** User is able to choose from the given list of notes 
- **Alternate Sequence:**
1. The system does not display a list of notes due to the keyword/tag not matching 
2. The system displays a message of "No notes were found"
3. The user can exit or try again with a new keyword

**9. Lock File Function(Gautam)**
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

10. File to Folder Organization(Gautam)
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


**11. Dark Mode Function(Gautam)**
- **Pre-condition*:** User is logged into the app 
- **Trigger:** User wants to invert the colors and switch to "dark mode"
- **Primary Sequence:**
1. The user navigates to the settings page 
2. The user clicks on the "Switch to Dark Mode" (Moon symbol) button
3. System inverts the colors of the background, text, and any other elements 
- **Primary Postconditions:** The app is in "Dark Mode"
- **Alternate Sequence:**
1. User chooses not to switch to dark mode
2. User clicks "Revert" button 
3. The system displays a page with regular colors

**12. Note Sharing (Steve)** 
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

**13. Note Export (Steve)** 
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

**14. Collaboration (Steve)** 
- **Pre-condition:** Multiple users have access to a note
- **Trigger:** One user starts editing the note
- **Primary Sequence:**
1. The user's changes are broadcast to all other users in real-time
2. All other users see the changes reflected in the note
3. Users can collaborate on the note in real-time
- **Primary Postconditions:** The note is updated with the collective contributions of all users & all users have a consistent view of the note
- **Alternate Sequence:** 
1. If there is a conflict between changes made by different users, a conflict resolution mechanism will be used to determine which change is accepted

**16. Insipirational Quotes (External API) (Akhil) - Milestone is once dashboard page is created**
- **Pre-condition:** User is logged in to the application
- **Trigger:** User navigation to dashboard
- **Primary Sequence:**
1. User navigates to dashboard
2. System queries insipirational quote website and displays quote on dashboard
3. User can choose to read the quote as it will be displayed when they are navigating around
- **Primary Postconditions:** Quote is cleared from memory upon navigation away from dashboard page
- **Alternate Sequence:** 
1. The user is not logged in and navigates to dashboard, system should not query api
2. 

**17. Translate Function (Externa1 Google Translate API) (Gautam)**
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

