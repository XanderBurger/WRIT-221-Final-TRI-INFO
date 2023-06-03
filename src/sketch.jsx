import React from 'react'
import { ReactP5Wrapper } from "react-p5-wrapper";
import csvData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/data/finalDataCombinedRounded.csv"


export default function Sketch(p5) {

    
    function drawing(p5){

        let data
        
        p5.preload = () => {
            data = p5.loadTable(csvData, "csv", "header")
        }

        p5.setup = () => {
            var sum = data.getColumn("Total Underground").reduce((accumulator, currentValue) => {
                return parseInt(accumulator) + parseInt(currentValue)
              }, 0);
            console.log(sum)
            p5.createCanvas(300, 1500)
        }

        p5.draw = () => {
            return
        }


    }
 
    return <ReactP5Wrapper sketch={drawing} />
}
