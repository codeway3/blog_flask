$(function() {

  console.log( "ready!" ); // sanity check

  $('#delete-info').hide()

  $('.entry').on('click', function() {
    var entry = this;
    var post_id = $(this).find('h2').attr('id');
    $.ajax({
      type:'GET',
      url: '/delete' + '/' + post_id,
      context: entry,
      success:function(result) {
        if(result.status === 1) {
          $('#flash').hide()
          $('#delete-info').text('The entry was deleted.').show()
          $(this).remove();
          console.log(result);
        }
      }
    });
  });

});