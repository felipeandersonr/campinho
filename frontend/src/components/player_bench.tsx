"use client";

import { useEffect, useState } from "react";
import Player from "./player";
import fetchPlayers from "../services/api";


interface DataPlayer {
    name: string;
    shirt_number: number;
};


const PlayerBench = () => {
    const [players, setPlayers] = useState<DataPlayer[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const getPlayers = async () => {
            try {
                const data = await fetchPlayers();

                setPlayers(data)
            }

            catch (err) {
                setError((err as Error).message);
            }
        };

        getPlayers();

    }, []);

    const content = <div>
        <h1>Banco de jogadores</h1>
        {error && <p>Error: {error}</p>}

        <div className="player-list">
            {
                players.map((player) => (
                    <Player name={player.name} shirt_number={player.shirt_number} />
                ))
            }
        </div>
    </div>

    return content;
};

export default PlayerBench;
