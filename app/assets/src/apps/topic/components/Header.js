import React from 'react'

function Header({ search, updateSearch }) {
    return (
        <div className="inner-main-header">
            <span className="input-icon input-icon-sm ml-auto w-auto">
                <form onSubmit={(e) => {e.preventDefault(); updateSearch(e.target[0].value)}}>
                    <div className="form-row align-items-center">
                        <div className="col-auto">
                            <input name="search" type="text" className="form-control bg-gray-200 border-gray-200 shadow-none"
                                placeholder="Search forum" />
                        </div>
                        <div className="col-auto">
                            <input type="submit" className="btn btn-primary has-icon btn-block" value="Search" />
                        </div>
                    </div>
                </form>
            </span>
        </div>
    )
}

export default Header