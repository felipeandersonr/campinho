import React from "react";
import "./player.css";


interface DataPlayer {
    name: string;
    shirt_number: number;
};

const Player = (props: DataPlayer) => {
    const content = <div className="player">
        <div className="shirt_number"> {props.shirt_number} </div>
        <p className="player_name"> {props.name} </p>
    </div>

    return content;
};

export default Player;
