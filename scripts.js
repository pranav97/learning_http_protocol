// # GET: fetch an existing resource.The URL contains all the necessary information the server needs to locate and return the resource.
// # POST: create a new resource.POST requests usually carry a payload that specifies the data for the new resource.
// # PUT: update an existing resource.The payload may contain the updated data for the resource.
// # DELETE: delete an existing resource.



var application = {
    clicked_go_button: function() {
        $.ajax("localhost:3000/get_testing", {
            header1: "this is what header1 is",
            header3: "this is where 3 is"

        }).success(function() {
            console.log("done")
        })
        console.log("clicked go todo the get request to /get_testing");
    },
    init: function() {
        this.go_button  = document.getElementById("go-button")
        console.log(this.go_button)
        this.go_button.addEventListener("click", this.clicked_go_button)

    }
    
    // make_get
    // make_put
}

$(document).ready(function () {
    application.init()

});