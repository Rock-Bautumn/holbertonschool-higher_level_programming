// $("header").attr( "class", "red" );
// console.log($("header").attr( "class"));

$('div#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
