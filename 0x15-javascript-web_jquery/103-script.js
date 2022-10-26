function hello () {
  $.getJSON(
    'https://fourtonfish.com/hellosalut/',
    { lang: $('INPUT#language_code').val() },
    function (json) {
      $('DIV#hello').text(json.hello);
    }
  );
}

$(function () {
  $('INPUT#btn_translate').bind('click', hello);
  $('INPUT#language_code').bind('keydown', function (event) {
    if (event.which === 13) {
      hello();
    }
  });
});
