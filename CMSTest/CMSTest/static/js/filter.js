$(document).ready(function() {
  $('#category').change(function() {
    var category_id = $(this).val();
    $.ajax({
      type: 'GET',
      url: '/filter/',
      data: {
        category_id: category_id,
      },
      success: function(data) {
        $('#results').html(data);
      }
    });
  });
});