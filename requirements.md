# Requirements 
## Functional Requirements
1. Create and Save New Notes - Users can create new text notes and save them to their account (Akhil)
2. Edit Existing Notes - Users can edit the text of their existing notes (Akhil)
3. Note Reminders - Users can get alerted to go back to a specific note this will show up on their note page (Akhil)
4. Highlight Text - Users can highlight text within a note
5. Create an Account - Allowing users to create an account to used the app (Hoang)
6. Log in - Allowing users to log into their account to access the app (Hoang)
7. Passwords Reset - Allowing user to reset their password in the app (Hoang) 
8. Search Function - Allows user to search for a specific note by keyword or title (Gautam)
9. Lock File Function - Allows user to lock each file with a password for privacy/security (Gautam)
10. File to Folder Organization - Allows user to organize each note to different folder or organize them by tags(Gautam)
11. Dark Mode - User can switch to dark mode(inverted colors) based on preference(Gautam)
12. Note Sharing - Allow users to share their notes publicly or privately with other users. (Steve)
13. Note Export - Allow users to export their notes to different formats, such as PDF, Word, or .txt (Steve)
14. Collaboration - Allow users to collaborate on notes with other users (Steve)

## Non-functional Requirements
1. The website should be responsive and functional on IOS and Macbooks
2. All webpages should load within 3 seconds - will be tested manually on a macbook

## Use Cases 
**1. Create and Save New Notes (Akhil) - Milestone is one week after UI is built out**
- **Pre-condition:** User is logged in and has an account
- **Trigger:** User clicks create a new note button
- **Primary Sequence:**
1. User clicks on "Create Note" Button
2. User is taken to new page with blank note
3. User enters text for new note
4. User clicks on "Save" button
5. System saves and confirms note is saved to user
- **Primary Postconditions:** A new note is created and saved to user's account
- **Alternate Sequence:** 
1. User does not enter any text and clicks "Save"
2. System tells user they can not make an empty note

**2. Edit Existing Notes (Akhil) - Milestone is one week after UI is built out**
- **Pre-condition:** User is logged in and has saved notes
- **Trigger:** User clicks edit button on a note
- **Primary Sequence:**
1. User clicks on "edit" button on a note
2. User is taken to that note page and can edit that note
3. User edits the text
4. User clicks on "Save" button
5. System saves and confirms note is saved to user
- **Primary Postconditions:** A new note is created and saved to user's account
- **Alternate Sequence:** 
1. User does notmake any changes anc clicks "Save"
2. System exits and tells user no changes were made

**3. Note Reminders (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in and has saved notes
- **Trigger:** User clicks reminder button in a note
- **Primary Sequence:**
1. User navigates to notes dashboard
2. User clicks on note they want to set reminder for
3. User clicks "Set Reminder" Button
4. User selects date and time they want reminder for
5. User clicks on "Save" button
6. System saves the reminder and tells user reminder has been set
7. System will notify User on top of the dashboard to revisit note when the date and time arrive
- **Primary Postconditions:** User is alerted when the time for reminder comes
- **Alternate Sequence:** 
1. User does not select a date and clicks "Save"
2. System alerts user they have to select date and time for the reminder

**4. Highlight Text (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed**
- **Pre-condition:** User is logged in a Note Editor State
- **Trigger:** User wants to highlight text within note
- **Primary Sequence:**
1. User navigates to notes edit or create page
2. User selects text to highlight
3. User clicks "Highlight" Button
4. System applies highlight to selected text
5. User clicks on "Save" button
6. System saves the text and tells user message based on whether user was in edit or create state
- **Primary Postconditions:** Selected text is highlighted in user's note
- **Alternate Sequence:** 
1. User does not select any text and clicks on "Highlight" Button
2. System alerts user they have to select text in order to highlight

**5. Creat an Account (Hoang)**
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Create Account" button
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Create a Account" button on the app 
3. User fill in their desire username and password and other information required
4. User then click on the "Create" button
5. System will confirm the account create
- **Primary Postconditions:** System will save the account and tell the user it was a success or not
- **Alternate Sequence:** 
1. User did not enter a email for the account
2. System will alert the user to enter missing field for information

**6. Log in (Hoang)**
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Log In" button on the app 
3. User fill in their username and password
4. User click on the "Submit" button to log in
- **Primary Postconditions:** System will check the account credential and log into the user account
- **Alternate Sequence:** 
1. User did not enter the correct username or password

**7. Passwords Reset (Hoang)**
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button and chose the option "Password Reset"
- **Primary Sequence:**
1. User nagivate to the app
2. User select the "Log In" button on the app 
3. User select the "Password Reset" option
4. User fill in their new desire username and password with other information
5. User click on the "Submit" button to reset password
6. System will process the information and save the account credential
- **Primary Postconditions:** System will say password reset is successful to user
- **Alternate Sequence:** 
1. User did not enter the new password correct in the field "Re-type new password"

**8. ... (Gautam)**
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...

**9. ... (Gautam)** 
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...

**10. ... (Gautam)** 
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...

**11. ... (Gautam)** 
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...

**12. ... (Steve)** 
- **Pre-condition:** User has created a note
- **Trigger:** User wants to share the note with another user
- **Primary Sequence:**
1. The user selects the note they want to share.
2. The user clicks the "Share" button.
3. The user enters the email address of the user they want to share the note with.
4. The user selects the desired access level (read or write) for the shared user.
5. The user clicks the "Share" button.
- **Primary Postconditions:** The shared user receives an email with a link to the note & can access the note with the specified access level
- **Alternate Sequence:** 
1. If the shared user does not have an account, they will be prompted to create one

**13. ... (Steve)** 
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...

**14. ... (Steve)** 
- **Pre-condition:** ...
- **Trigger:** ...
- **Primary Sequence:**
1. ...
2. ...
3. ...
4. ...
5. ...
- **Primary Postconditions:** ...
- **Alternate Sequence:** 
1. ...
