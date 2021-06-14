$(document).ready(function(){
    $('#title').keyup(function(){         
        let words = $(this)[0].value    // jquery "keyup" creates a list, as opposed to just a value, so we need to grab the [0] position's value
        $.ajax({
            method: "GET",
            url: "title_valid/"+words,
            success: function(serverResponse){
                $('#show_title_valid').html(serverResponse)     //put the serverResponse into the the #show_title_valid section as html (comes from views.py)
            }
        })
    })
})
