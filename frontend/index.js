import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('http://localhost:8000/test')
            .then((response) => response.json())
            .then((json) => setMessage(json.message || 'No message'))
            .catch(() => setMessage('Error occured whilst fetching the message'))
    }, [])

    return (
        <h1>{message}</h1>
    );
}

ReactDOM.render(<App />, document.getElementById('app'));
