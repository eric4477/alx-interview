#!/usr/bin/node

const axios = require('axios');

// Function to fetch and print character names for a given movie ID
async function getMovieCharacters (movieId) {
  const baseUrl = 'https://swapi.dev/api/films/';

  try {
    // Fetch the movie data
    const response = await axios.get(`${baseUrl}${movieId}/`);
    const movieData = response.data;

    // Get the list of character URLs
    const characterUrls = movieData.characters;

    // Fetch and print each character name
    for (const url of characterUrls) {
      const charResponse = await axios.get(url);
      const charData = charResponse.data;
      console.log(charData.name);
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Check if a movie ID was provided
if (process.argv.length !== 3) {
  console.log('Usage: ./starwars_characters.js <movie_id>');
} else {
  // Get the movie ID from the command-line arguments
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
