import React, { useState, useEffect } from 'react';

import { getPost, postLike } from '../api';

import Like from './Like';

/**
 * Post with likes component.
 */
const Post = () => {
    const [post, setPost] = useState(null);

    useEffect(() => {
        getPost().then((post) => setPost(post));
    }, []);

    const addLike = () => {
        // Temporarily store the previous like count incase of a server error.
        const prevLikes = post.likes;

        // Increment the like count.
        setPost({ ...post, likes: post.likes + 1 });

        // Tell the server we would are adding a like to this post.
        postLike({ post_id: post.id })
            // Catch server errors and rollback to the previous like count.
            .catch(() => setPost({ ...post, likes: prevLikes }));
    };

    if (!post) {
        return null;
    }

    return (
        <div className="max-w-sm bg-white p-3 rounded shadow-lg">
            <div className="mb-2">{post.content}</div>
            <Like likes={post.likes} addLike={addLike}></Like>
        </div>
    );
};

export default Post;
