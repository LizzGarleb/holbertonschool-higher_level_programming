
const toggleHeader = $('DIV#toggle_header');
toggleHeader.on('click', () => {
  const header = $('header');
  header.toggleClass('red green');
});
