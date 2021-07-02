import React, { useEffect, useState } from 'react'
import Header from './Header'
import Sidebar from './Sidebar'
import Topic from './Topic'

function TopicList() {
    const [filter, updateFilter] = useState('all')
    const [search, updateSearch] = useState('search')
    const [topics, updateTopics] = useState([])
    const [next, updateNext] = useState(null)

    useEffect(() => {
        fetch('http://localhost:8000/topics/?format=json')
            .then(result => result.json())
            .then(result => {
                updateTopics(result['results'])
                updateNext(result['next'])
            })
    }, [])

    function loadMore() {
        fetch(next)
            .then(result => result.json())
            .then(result => {
                updateTopics(topics.concat(result['results']))
            })
    }

    return (
        <div className="inner-wrapper">
            <Sidebar filter={filter} updateFilter={updateFilter} />
            <div className="inner-main">
                <Header search={search} updateSearch={updateSearch} />
                <div className="inner-main-body p-2 p-sm-3 collapse forum-content show">
                    {topics.map(({ id, title, text, count_replies, solved, author, last_message }) => (
                        <Topic key={"topic-" + id} id={id} title={title} text={text} count_replies={count_replies} solved={solved} author={author} last_message={last_message} /> 
                    ))}
                    {next != null && <a className="btn btn-primary has-icon btn-block" type="button" style={{width: 150}} onClick={loadMore}>Load more</a>}
                </div>
            </div>
        </div>
    )
}

export default TopicList