/**
 * @typedef {Object} Post
 * @property {number} id - The post id.
 * @property {string} content - Content of the post.
 * @property {number} likes - How many likes the post has.
 */

/**
 * Request the first and only post.
 * @returns {Promise<Post>} Post response from the server.
 */
export const getPost = async () => {
    const response = await fetch('http://localhost:8000/post');

    if (!response.ok) {
        throw new Error('Server error');
    }

    return response.json();
};

/**
 * Request to add a like against the post.
 * @param {Object} request - JSON data to be sent.
 * @param {number} request.post_id - The id of the post to like.
 * @returns {Promise<Response>} Response from the server.
 */
export const postLike = async ({ post_id }) => {
    const response = await fetch('http://localhost:8000/like', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ post_id }),
    });

    if (!response.ok) {
        throw new Error('Server error');
    }

    return response.json();
};
