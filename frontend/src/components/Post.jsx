import React, { useState, useEffect } from 'react';

import { getPost, postLike } from '../api';

import Like from './Like';

/**
 * Post with likes component.
 */
const Post = () => {
    const [post, setPost] = useState(null);
    const [newLikes, setNewLikes] = useState(0);

    useEffect(() => {
        getPost().then((post) => setPost(post));
    }, []);

    const addLike = () => {
        // Temporarily store the previous like count incase of a server error.
        const prevLikes = post.likes;

        // Create a variable for the new likes count.
        const likes = prevLikes + 1;

        // Increment the like count.
        setPost({ ...post, likes });

        // Tell the server we would are adding a like to this post.
        postLike({ post_id: post.id })
            // The server will return the updated like count.
            .then((response) => {
                setPost({ ...post, likes: response.likes });
                setNewLikes(response.likes - likes);
            })
            // Catch server errors and rollback to the previous like count.
            .catch(() => setPost({ ...post, likes: prevLikes }));
    };

    if (!post) {
        return null;
    }

    return (
        <div className="max-w-sm bg-white p-3 rounded shadow-lg">
            <div className="mb-2">{post.content}</div>
            <Like
                likes={post.likes}
                newLikes={newLikes}
                addLike={addLike}
            ></Like>
        </div>
    );
};

export default Post;
