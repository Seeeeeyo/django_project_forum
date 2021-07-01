import React, { useEffect, useState } from 'react'
import Header from './Header'
import Sidebar from './Sidebar'
import Topic from './Topic'

const topicList = {
    "count": 7,
    "next": "http://localhost:8000/api/topic/?page=2&search=%22test%22",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "test",
            "description": "test",
            "topicmessage_count": 3,
            "is_solved": false,
            "creator_serializer": {
                "email": "dubois.rom@gmail.com",
                "avatar": null,
                "first_name": "Romain",
                "last_name": "Dubois"
            },
            "created_at": "2021-05-19T19:24:44.166583Z"
        },
        {
            "id": 2,
            "title": "test",
            "description": "test",
            "topicmessage_count": 0,
            "is_solved": true,
            "creator_serializer": {
                "email": "dubois.rom@gmail.com",
                "avatar": null,
                "first_name": "Romain",
                "last_name": "Dubois"
            },
            "created_at": "2021-05-19T19:29:21.675850Z"
        },
        {
            "id": 3,
            "title": "tes 3",
            "description": "ts 3",
            "topicmessage_count": 1,
            "is_solved": false,
            "creator_serializer": {
                "email": "dubois.rom@gmail.com",
                "avatar": null,
                "first_name": "Romain",
                "last_name": "Dubois"
            },
            "created_at": "2021-05-19T19:58:31.087581Z"
        }
    ]
}

function TopicList() {
    const [filter, updateFilter] = useState('all')
    const [search, updateSearch] = useState('search')

    useEffect(() => {
        console.log(filter)
    }, [filter])

    useEffect(() => {
        console.log(search)
    }, [search])

    const topics = topicList['results']

    return (
        <div className="inner-wrapper">
            <Sidebar filter={filter} updateFilter={updateFilter} />
            <div className="inner-main">
                <Header search={search} updateSearch={updateSearch} />
                <div className="inner-main-body p-2 p-sm-3 collapse forum-content show">
                    {topics.map(({ id, title, description, topicmessage_count, is_solved, creator_serializer, created_at }) => (
                        <Topic key={"topic-" + id} id={id} title={title} description={description} topicmessage_count={topicmessage_count} is_solved={is_solved} creator_serializer={creator_serializer} created_at={created_at} /> 
                    ))}
                </div>
            </div>
        </div>
    )
}

export default TopicList