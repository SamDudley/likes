import React from 'react';
import PropTypes from 'prop-types';

const Like = ({ likes, addLike }) => {
    return (
        <div className="like">
            <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded"
                onClick={addLike}
            >
                Like
            </button>
            <span className="ml-2">{likes}</span>
        </div>
    );
};

Like.propTypes = {
    likes: PropTypes.number.isRequired,
    addLike: PropTypes.func.isRequired,
};

export default Like;
