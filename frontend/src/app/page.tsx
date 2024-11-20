import SoccerPitch from "../components/soccer_pitch";
import Player from "../components/player";
import PlayerBench from "../components/player_bench";

import "./globals.css";


export default function Home() {
  const content = <div>
    <h1>Nome e escudo do time que busquei os jogadores</h1>

    <div className="content">
      <PlayerBench />

      <SoccerPitch />
    </div>
  </div>

  return content;
};
