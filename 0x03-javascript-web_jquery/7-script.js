$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (returnData) => {
  $('DIV#character').text(returnData.name);
});
