import moment from 'moment'
import React from 'react'

function Topic({ id, title, text, count_replies, solved, author, last_message }) {
    return (
        <div className="card mb-2">
            <div className="card-body p-2 p-sm-3">
                <div className="media forum-item">
                    <img src={author['avatar']} className="mr-3 rounded-circle"
                        width="50" alt="User" />
                    <div className="media-body">
                        <h6 className="text-body"><a className="text-dark" href={"/" + id}>{title} <small>{solved && "Solved"}</small></a></h6>
                        <p className="text-secondary">
                            {text}
                        </p>
                        <p className="text-muted">
                            <span className="text-secondary font-weight-bold">{last_message['author']} </span>
                            replied at
                            <span className="text-secondary font-weight-bold"> {moment(last_message['date']).fromNow()}</span>
                        </p>
                    </div>
                    <div className="text-muted small text-center align-self-center">
                        <span><i className="far fa-comment ml-2"></i> {count_replies}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Topic