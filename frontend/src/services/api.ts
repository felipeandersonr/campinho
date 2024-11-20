const API_URL = "http://localhost:8000";

const fetchPlayers = async () => {
    const response = await fetch(`${API_URL}/lineup/5`); // /lineup/id_do_time

    if (!response.ok) {
        throw new Error("Failed to fetch players");
    }

    return response.json();
};

export default fetchPlayers;
