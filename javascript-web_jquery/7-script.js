const char = $('DIV#character');
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: (data) => {char.text(data.name); }
});
