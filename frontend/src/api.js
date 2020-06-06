export const getPost = async () => {
    const response = await fetch('http://localhost:8000/post');

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

    return response;
};
