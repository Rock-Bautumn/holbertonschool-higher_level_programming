$.get('https://swapi-api.hbtn.io/api/films/?format=json', (returnData) => {
  const films = returnData.results;
  for (const item in films) {
    $('#list_movies').append(`<li>${films[item].title}</li>`);
  }
});
