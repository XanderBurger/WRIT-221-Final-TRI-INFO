import React, { useState } from "react";
import Sketch from './sketch'
import "./Graph.css"

export default function Graph() {
    let [graph, setGraph] = useState("Air");
    
    const handleGraph = (graphType) => {
    return setGraph(graphType);
    };


  return (
    <div>
        <div className="graphButtons">
            <button onClick={() => handleGraph("Air")}>Air</button>
            <button onClick={() => handleGraph("Land Treatment")}>Land Treatment</button>
            <button onClick={() => handleGraph("Landfill")}>Landfill</button>
            <button onClick={() => handleGraph("Surface Impoundment")}>Surface Impoundment</button>
            <button onClick={() => handleGraph("Underground Wells")}>Underground Wells</button>
            <button onClick={() => handleGraph("Water")}>Water</button>
            <button onClick={() => handleGraph("Recycled")}>Recycled</button>
        </div>
        <div className="key">
            <p className="keyTitle">Special Classification:</p>
            <p>Carcinogen –</p> <div className="carcinogen"></div>
            <p>PBT – </p> <div className="PBT"></div>
        </div>
        <Sketch className="sketch" graph = {graph}/>
    </div>
  )
}
