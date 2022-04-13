// $("header").attr( "class", "red" );
console.log($('header').attr('class'));

$('div#toggle_header').on('click', function () {
  if ($('header').attr('class') === 'red') { $('header').attr('class', 'green'); } else { $('header').attr('class', 'red'); }
});
