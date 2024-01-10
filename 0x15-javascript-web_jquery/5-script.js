$('#add_item').click(function () {
  const newLi = $('<li></li>').text('Item');
  $('ul.my_list').append(newLi);
});
