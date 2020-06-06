import React, { useState, useEffect } from 'react';

import { getPost, postLike } from '../api';

import Like from './Like';

const Post = () => {
    const [post, setPost] = useState(null);

    useEffect(() => {
        getPost().then((post) => setPost(post));
    }, []);

    const addLike = () => {
        const prevLikes = post.likes;

        setPost({ ...post, likes: post.likes + 1 });

        postLike({ post_id: post.id }).catch(() =>
            setPost({ ...post, likes: prevLikes }),
        );
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
