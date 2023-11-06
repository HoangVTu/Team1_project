# Requirements 
## Functional Requirements
1. Create and Save New Notes - Users can create new text notes and save them to their account (Akhil)
2. Edit Existing Notes - Users can edit the text of their existing notes (Akhil)
3. Note Reminders - Users can get alerted to go back to a specific note; this will show up on their note page (Akhil)
4. Highlight Text - Users can highlight text within a note
5. Create an Account - Allowing users to create an account to use the app (Hoang)
6. Log in - Allowing users to log into their account to access the app (Hoang)
7. Passwords Reset - Allowing the user to reset their password in the app (Hoang) 
8. Search Function - Allows user to search for a specific note by keyword or title (Gautam)
9. Lock File Function - Allows user to lock each file with a password for privacy/security (Gautam)
10. File to Folder Organization - Allows the user to organize each note into different folders or organize them by tags(Gautam)
11. Dark Mode - User can switch to dark mode(inverted colors) based on preference(Gautam)
12. Note Sharing - Allow users to share their notes publicly or privately with other users. (Steve)
13. Note Export - Allow users to export their notes to different formats, such as PDF, Word, or .txt (Steve)
14. Collaboration - Allow users to collaborate on notes with other users (Steve)

[sketch](images/sketch.jpg) 

## Non-functional Requirements
1. The website should be responsive and functional on IOS and Macbooks
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

**5. Create an Account (Hoang)**
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

**6. Log in (Hoang)**
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

**7. Passwords Reset (Hoang)**
- **Pre-condition:** User must go to the app
- **Trigger:** User clicks on the "Log In" button and chooses the option "Password Reset"
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Log In" button on the app 
3. User select the "Password Reset" option
4. The user fills in their new desired username and password with other information
5. The user clicks on the "Submit" button to reset the password
6. The system will process the information and save the account credential
- **Primary Postconditions:** System will say password reset is successful to user
- **Alternate Sequence:** 
1. The user did not enter the new password correctly in the field "Re-type new password"

**8. Search Function (Gautam)**
- **Pre-condition:** User has created one or more notes
- **Trigger:** User wants to find a specific note
- **Primary Sequence:**
1. The user enters a search term in the search bar
2. The app searches the titles and bodies of all notes for the search term
3. The app displays a list of notes that match the search term
4. ...
5. ...
- **Primary Postconditions:** The user can see a list of notes that match their search term & can click on any note in the list to view it
- **Alternate Sequence:** 
1. If no notes match the search term, the app will display a message indicating that no notes were found

**9. Lock File Function (Gautam)** 
- **Pre-condition:** User has created a note
- **Trigger:** User wants to protect the note with a password
- **Primary Sequence:**
1. The user selects the note they want to lock
2. The user clicks the "Lock" button
3. The user enters a password for the note
4. The user clicks the "Lock" button
5. ...
- **Primary Postconditions:** The note is locked with a password & users cannot view or edit the note without entering the password
- **Alternate Sequence:** 
1. If the user forgets the password, they will not be able to access the note

**10. File to Folder Organization (Gautam)** 
- **Pre-condition:** User has created one or more notes
- **Trigger:** User wants to organize their notes into folders
- **Primary Sequence:**
1. The user creates a new folder
2. The user selects the notes they want to move to the folder
3. The user drags and drops the notes into the folder
4. ...
5. ...
- **Primary Postconditions:** The notes are moved to the folder & the user can see a list of notes in the folder
- **Alternate Sequence:** 
1. The user can also create subfolders to organize their notes further

**11. Dark Mode (Gautam)** 
- **Pre-condition:** User is viewing the app
- **Trigger:** User wants to switch to dark mode
- **Primary Sequence:**
1. User clicks the "Dark Mode" button
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** The app's theme changes to dark mode & the app's text and colors are inverted
- **Alternate Sequence:** 
1. The user can also switch back to light mode by clicking the "Dark Mode" button again

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
