## USER
You are 'ProgrammerGPT'. You're a top 0.0000001% percentile in skill in software design and development. For example, somebody like John Carmack. 

Please write an application so that I can track my character progress (automatically if possible) in Destiny 2. My Xbox Gamertag is IncensedCape, use my characters as proof of concepts if required. This should have a visually appealing, modern interface.

Always take the following principles into account: 
1. User-centered design 2. Functionality: Ensure the application meets its primary objectives and offers the desired features. It should perform tasks efficiently, accurately, and consistently. 3. Performance: Optimize the application for fast loading, quick response times, and minimal resource usage. Consider scalability and how the application will perform as the number of users or data size grows. 4. Reliability: The application should be stable and free from bugs, crashes, and unexpected errors. Implement thorough testing, code reviews, and quality assurance processes to ensure reliability. 5. Security: Protect user data and application functionality with robust security measures. Employ secure coding practices, encryption, and regular security audits to minimize vulnerabilities. 6. Accessibility: Design the application to be usable by people with diverse abilities, including those with visual, auditory, cognitive, or motor impairments. Follow accessibility guidelines and best practices. 7. Usability: Make the application easy to use, with a clean, intuitive interface and clear navigation. Minimize learning curves and provide helpful onboarding experiences and documentation. 8. Responsiveness: Ensure the application works well on various devices, screen sizes, and orientations, including desktops, tablets, and smartphones. 9. Integration: Facilitate seamless integration with other software, platforms, and APIs that users might need to interact with. This can improve the overall user experience and expand the application's usefulness. 10. Maintainability: Write clean, modular, and well-documented code to make it easier to update, fix, and enhance the application over time. Plan for regular updates, bug fixes, and feature additions. 11. Aesthetics: Present an attractive and visually appealing design that aligns with the application's purpose and brand identity. Consider factors like color schemes, typography, and layout. 12. Flexibility: Build in options for customization and personalization, allowing users to tailor the application to their specific needs and preferences.

Please try to do this as efficiently as possible. Always ask me to confirm your next action before you do anything at all that would cost money or tokens or anything similar? This is so that spending can remain in budget. 

Please try to offer more than just the 'minimal' required. I would like a bit of flair / true demonstration of skill please.

Always comment the code accordingly please.


Keep all of this into account for any responses please.

Thanks.

## ASSISTANT
As an AI language model, I cannot directly create a fully functional application for you. However, I can provide you with a high-level design plan and some code snippets to help you get started on creating a Destiny 2 character progress tracking application.

Given the requirement for automatic tracking, the application should be built using the Bungie.net API to access Destiny 2 game data. You can find documentation and instructions for setting up an API key at: https://bungie-net.github.io/

Here's a high-level plan for the application:

1. Register and set up an API key with Bungie.net.
2. Create a frontend with a visually appealing, modern design, and responsive layout.
3. Implement the backend server, handling requests from the frontend and fetching data from the Bungie.net API.
4. Store data in a local database for caching and faster response times.
5. Implement a user authentication system to securely store user-specific data.
6. Test the application for reliability, performance, and accessibility.

Here is an example of how you could start fetching data for a given player's characters:

```python
import requests

API_KEY = "YOUR_API_KEY"
GAMERTAG = "IncensedCape"

def get_player_id():
    headers = {"X-API-Key": API_KEY}
    response = requests.get(
        f"https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/1/{GAMERTAG}/",
        headers=headers,
    )
    if response.status_code == 200:
        player_id = response.json()["Response"][0]["membershipId"]
        return player_id
    return None

def get_characters(player_id):
    headers = {"X-API-Key": API_KEY}
    response = requests.get(
        f"https://www.bungie.net/Platform/Destiny2/1/Profile/{player_id}/?components=200",
        headers=headers,
    )
    if response.status_code == 200:
        characters_data = response.json()["Response"]["characters"]["data"]
        return characters_data
    return None

player_id = get_player_id()
if player_id:
    characters_data = get_characters(player_id)
    if characters_data:
        # Process and display character data in the frontend
```

This Python code fetches data for the specified gamertag, "IncensedCape". Make sure to replace "YOUR_API_KEY" with your actual Bungie.net API key.

For the frontend, you can use modern web frameworks like React, Vue, or Angular to build a visually appealing and responsive interface. Here's an example of a React component that displays character information:

```javascript
import React, { useState, useEffect } from "react";

function CharacterCard({ characterData }) {
  return (
    <div className="character-card">
      <h2>{characterData.classType}</h2>
      <p>Light Level: {characterData.light}</p>
      {/* More character details here */}
    </div>
  );
}

function Destiny2App() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    // Fetch character data from the backend and update state
    // You'll need to create an endpoint in your backend to serve the character data
  }, []);

  return (
    <div className="destiny2-app">
      {characters.map((characterData) => (
        <CharacterCard key={characterData.characterId} characterData={characterData} />
      ))}
    </div>
  );
}

export default Destiny2App;
```

This is just a starting point for your application. You'll need to further develop the frontend, backend, and integrate the Bungie.net API to build a complete character progress tracking application.

Remember to