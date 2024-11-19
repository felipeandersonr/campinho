import React from "react";
import "./jogador.css";

const Jogador = (props: any) => {
    const content = <div className="player">
        <div className="shirt_number"> {props.shirt_number} </div>
        <p className="player_name"> {props.player_name} </p>
    </div>

    return content;
};

export default Jogador;
