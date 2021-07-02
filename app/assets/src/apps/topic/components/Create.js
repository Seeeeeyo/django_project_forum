function Create(handleCreate) {
    return (
        <div>
            <a href="javascript:void(0)" class="btn btn-light btn-sm mb-3 has-icon">
                <i class="fa fa-arrow-left mr-2"></i> Back
            </a>
            <h3>Create new Topic</h3>
            <hr />
            <form onSubmit={handleSubmit}>
                <div class="form-group mb-2">
                    <label for="title" class="">Your title</label>
                    <input type="text" class="form-control" id="title"/>
                </div>
                <div class="form-group mb-2">
                    <label for="description" class="">Your message</label>
                    <textarea class="form-control" id="description" style="height: 145px;"></textarea>
                </div>
                <button type="submit" class="btn btn-primary mb-2">Create</button>
            </form>
        </div>
    )
}

export default Create