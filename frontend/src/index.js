import React from 'react';
import ReactDOM from 'react-dom';

import Post from './components/Post';

const App = () => {
    return <Post></Post>;
};

ReactDOM.render(<App />, document.getElementById('app'));
