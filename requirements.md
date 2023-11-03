## <remove all of the example text and notes in < > such as this one>

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
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The website should be responsive and functional on IOS and Macbooks
2. All webpages should load within 3 seconds - will be tested manually on a macbook

<each of the 14 requirements will have a use case associated with it>
## Use Cases 
1. Create and Save New Notes (Akhil) - Milestone is one week after UI is built out
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

2. Edit Existing Notes (Akhil) - Milestone is one week after UI is built out
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

3. Note Reminders (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed
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

4. Highlight Text (Akhil) - Milestone is one week after Edit and Save Notes requirements are completed
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

5. Creat an Account (Hoang) 
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Create Account" button
- **Primary Sequence:**

6. Log in (Hoang)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button
- **Primary Sequence:**

7. Passwords Reset (Hoang)
- **Pre-condition:** User must go to the app
- **Trigger:** User click on the "Log In" button and chose the option "Password Reset"
- **Primary Sequence:**
