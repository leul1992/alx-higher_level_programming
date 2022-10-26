$(function () {
  const $my_List = $('UL.my_list');

  $('DIV#add_item').click(() => {
    $my_List.append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list LI').last().remove();
  });
  $('DIV#clear_list').click(() => {
    $my_List.empty();
  });
});
