const hello = $('DIV#hello');
$.ajax({
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  success: function (data) {
    hello.text(data.hello);
  }
});
