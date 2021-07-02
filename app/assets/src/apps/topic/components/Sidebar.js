import React from 'react'

const filters = {
    'all': 'All Threads',
    'solved': 'Solved',
    'unsolved': 'Unsolved',
    'noreply': 'No replies yet'
}

function Sidebar({ filter, updateFilter, updatePage }) {
    return (
        <div className="inner-sidebar">
            <div className="inner-sidebar-header justify-content-center">
                <a className="btn btn-primary has-icon btn-block" type="button" onClick={() => {updatePage('create')}}>New topic</a>
            </div>

            <div className="inner-sidebar-body p-0">
                <div className="p-3 h-100" data-simplebar="init">
                    <nav className="nav nav-pills nav-gap-y-1 flex-column">
                        {Object.entries(filters).map(([ k, v ]) => (
                            <a key={k} className={"nav-link nav-link-faded has-icon" + (k == filter && " active")} onClick={() => updateFilter(k)}>
                                {v}
                            </a>
                        ))}
                    </nav>
                </div>
            </div>
        </div>
    )
}

export default Sidebar