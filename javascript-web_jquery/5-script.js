const addItem = $('DIV#add_item');
addItem.on('click', () => {
  const newLi = $('<li>').text('Item');
  $('ul.my_list').append(newLi);
});
