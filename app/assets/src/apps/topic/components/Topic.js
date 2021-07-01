import moment from 'moment'
import React from 'react'

function Topic({ id, title, description, topicmessage_count, is_solved, creator_serializer, created_at }) {
    return (
        <div className="card mb-2">
            <div className="card-body p-2 p-sm-3">
                <div className="media forum-item">
                    <img src={creator_serializer['avatar']} className="mr-3 rounded-circle"
                        width="50" alt="User" />
                    <div className="media-body">
                        <h6 className="text-body"><a className="text-dark" href={"/" + id}>{title} <small>{is_solved && "Solved"}</small></a></h6>
                        <p className="text-secondary">
                            {description}
                        </p>
                        <p className="text-muted">
                            <span className="text-secondary font-weight-bold">{creator_serializer['first_name'] + " " + creator_serializer['last_name']} </span>
                            created
                            <span className="text-secondary font-weight-bold"> {moment(created_at).fromNow(true)} ago</span>
                        </p>
                    </div>
                    <div className="text-muted small text-center align-self-center">
                        <span><i className="far fa-comment ml-2"></i> {topicmessage_count}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Topic