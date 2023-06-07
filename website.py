import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
  <title>Project</title>
</head>

<body>
  <h1>
    量化多头
  </h1>
  <p style="text-align:center">
    <iframe width="1500" height="300" src="https://lookerstudio.google.com/embed/reporting/392a01a6-c808-4734-9b9f-e12cd6a390ee/page/nSSTD" frameborder="0" style="border:0" allowfullscreen></iframe>
  </p>
  <script src="script.js"></script>
</body>

</html>
    """,
    height=600,width=1500
)