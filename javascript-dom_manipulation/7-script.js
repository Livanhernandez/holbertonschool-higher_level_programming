fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the response as JSON.
  .then(data => {
    const listMoviesElement = document.getElementById('list_movies');
    
    data.results.forEach(movie => {
        const movieElement = document.createElement('li');
        movieElement.textContent = movie.title;
        listMoviesElement.appendChild(movieElement);
    });
  })
  .catch(error => {
    console.error('Error fetching movie titles:', error);
  });
