import React from 'react';
import PropTypes from 'prop-types';

const Like = ({ likes, addLike }) => {
    return (
        <div className="like">
            <button className="like-button" onClick={addLike}>
                Like
            </button>
            {likes}
        </div>
    );
};

Like.propTypes = {
    likes: PropTypes.number.isRequired,
    addLike: PropTypes.func.isRequired,
};

export default Like;
