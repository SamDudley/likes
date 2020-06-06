export const getPost = async () => {
    const response = await fetch('http://localhost:8000/post');

    if (!response.ok) {
        throw new Error('Server error');
    }

    return response.json();
};

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

    return response;
};
