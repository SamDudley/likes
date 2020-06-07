import React from 'react';

import Post from './components/Post';

/**
 * Root component for our app.
 */
const App = () => {
    return (
        <main className="h-full flex justify-center items-center">
            <Post></Post>
        </main>
    );
};

export default App;
