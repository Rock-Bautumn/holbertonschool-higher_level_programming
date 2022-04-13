$.get('https://fourtonfish.com/hellosalut/?lang=fr', (returnData) => {
  $('DIV#hello').text(returnData.hello);
});
