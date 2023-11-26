import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

function Notes() {
    const [newNote, setNewNote] = useState('');
    const [reminder, setReminder] = useState('');
    const [highlights, setHighlights] = useState([]);

    const noteRef = useRef(null);
    
    const navigate = useNavigate();

    const handleNoteChange = (event) => {
        setNewNote(event.target.innerText);
    };

    const addNote = () => {
        console.log("addNote called");
        if (!newNote.trim()) {
            console.log("Note content is empty."); 
            return;
        }
        const noteData = {
            title: 'New Note',
            content: newNote,
            highlights: highlights,
            reminder: reminder, 
        };
    
        fetch('/api/notes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(noteData),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            navigate('/');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };
    

    const handleReminderChange = (e) => {
        setReminder(e.target.value);
    };

    const handleHighlight = () => {
        if (window.getSelection) {
            const selection = window.getSelection();
            if (!selection.rangeCount || selection.isCollapsed) {
                alert('Please select text to highlight.');
                return;
            }
            const range = selection.getRangeAt(0);
            const start = range.startOffset;
            const end = range.endOffset;
    
            setHighlights([...highlights, { start, end }]);
    
            if (range.commonAncestorContainer.parentNode.style.backgroundColor === 'yellow') {
                const parentSpan = range.commonAncestorContainer.parentNode;
                const spanContents = document.createRange();
                spanContents.selectNodeContents(parentSpan);
                parentSpan.replaceWith(...parentSpan.childNodes);
            } else {
                const span = document.createElement('span');
                span.style.backgroundColor = 'yellow';
                range.surroundContents(span);
            }
            selection.removeAllRanges();
        }
    };
    
    

    return (
        <div className="App flex flex-col items-center justify-center">
            <div className="w-2/3 bg-gray-200 p-4 border-black border rounded-lg my-2">
                <h1 className="text-center font-bold">Add a Note</h1>
                <div
                    ref={noteRef}
                    contentEditable
                    onInput={handleNoteChange} 
                    className="p-2 border-black border rounded-lg w-full mb-2"
                    style={{ minHeight: '100px' }}
                ></div>
                <div className="flex items-center mb-2">
                    <button onClick={handleHighlight} className="p-2 bg-yellow-300 text-black rounded-lg mr-2">
                        Highlight
                    </button>
                    <span>Select your word then click the highlight button to highlight it!</span>
                </div>
                <h3 className="text-center font-semibold mb-1">Set an Optional Reminder</h3>
                <input 
                    type="datetime-local" 
                    value={reminder}
                    onChange={handleReminderChange}
                    className="p-2 border-black border rounded-lg w-full mb-2"
                />
                <button 
                    onClick={addNote} 
                    className="p-2 bg-blue-500 text-white rounded-lg w-full">
                    Save Note
                </button>
            </div>
        </div>
    );
}

export default Notes;
