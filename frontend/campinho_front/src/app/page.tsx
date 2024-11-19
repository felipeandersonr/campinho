import Campo from "../components/campo";
import Jogador from "../components/jogador";

import "./globals.css";


export default function Home() {
  const content = <div>
    <h1>Nome e escudo do time que busquei os jogadores</h1>

    <div className="content">
      <Jogador shirt_number="10" player_name="Rodrigo Garro"></Jogador>

      <Campo />
    </div>
  </div>

  return content;
};
