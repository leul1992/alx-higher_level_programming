$(function () {
  $('INPUT#btn_translate').bind('click', function () {
    $.getJSON(
      'https://fourtonfish.com/hellosalut/',
      { lang: $('INPUT#language_code').val() },
      function (json) {
        $('DIV#hello').text(json.hello);
      }
    );
  });
});
