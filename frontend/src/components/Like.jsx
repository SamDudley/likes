import React from 'react';
import PropTypes from 'prop-types';

/**
 * Callback to add a like against a post.
 * @callback addLike
 */

/**
 * Like component.
 * @param {Object} props - Like component props.
 * @param {number} props.likes - Number of likes.
 * @param {addLike} props.addLike - Callback triggered on like button click.
 */
const Like = ({ likes, newLikes, addLike }) => {
    return (
        <div className="like">
            <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded"
                onClick={addLike}
            >
                Like
            </button>
            <span className="ml-2">{likes}</span>
            {!!newLikes && (
                <span className="ml-2 text-sm text-gray-700">{`${
                    newLikes > 0 ? '+' : '-'
                }${newLikes} new likes`}</span>
            )}
        </div>
    );
};

Like.propTypes = {
    likes: PropTypes.number.isRequired,
    newLikes: PropTypes.number.isRequired,
    addLike: PropTypes.func.isRequired,
};

export default Like;
