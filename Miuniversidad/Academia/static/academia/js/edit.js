$(document).ready(function() {
    $('#txtnombre').click(function() {
      // AJAX request to fetch list of courses
    $.ajax({
        url: '{% url "academia:list" %}',
        method: 'GET',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        success: function(data) {
          // Populate dropdown menu with list of courses
        var options = '';
        for (var i = 0; i < data.length; i++) {
            options += '<option value="' + data[i].codigo + '">' + data[i].nombre + '</option>';
        }
        $('#curso-dropdown').html(options);
        $('#curso-dropdown').show();
        },
        error: function() {
        alert('Error fetching courses.');
        }
    });
    });
});