<!DOCTYPE html>
<html>
  <head>
    <title>Frontend Site</title>
  </head>
  <body>
    <h1>Frontend Site</h1>
    <pre id="data"></pre>

    <script>
      // Use the Fetch API to retrieve data from the backend site
      fetch('http://localhost:5000/api/data')
       .then(response => response.json())
       .then(data => {
          // Display the retrieved data on the page
          document.getElementById('data').textContent = JSON.stringify(data, null, 2);
        })
       .catch(error => {
          console.error('Error retrieving data:', error);
        });
    </script>
  </body>
</html>