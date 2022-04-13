// $("header").attr( "class", "red" );
// console.log($("header").attr( "class"));
// $("#divText").text("A dynamically set text");
$('div#update_header').on('click', function () {
  $('header').text('New Header!!!');
});
