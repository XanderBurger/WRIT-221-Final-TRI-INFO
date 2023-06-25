import React from 'react'
import { ReactP5Wrapper } from "react-p5-wrapper";
import topAirData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topAir.csv"
import topLandData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topLand.csv"
import topLandfillData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topLandfill.csv"
import topRecycledData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topRecycled.csv"
import topSurfaceData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topSurface.csv"
import topUndergroundData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topUnderground.csv"
import topWaterData from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/data/dataByDisposalType/topWater.csv"

import caslonBold from "/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/Assets/fonts/LibreCaslonText-Bold.ttf"


export default function Sketch({graph}) {

    let graphDescriptions = {
        "Air": "Chemicals released by air stacks and fumes.",
        "Land Treatment":  "Chemicals that have been applied to the environment as a part of farming practices. Meaning fertilizers, pesticides or herbicides." ,
        "Landfill": "Chemicals that have been dumped in landfills on or off site of the facility.",
        "Recycled":"Chemicals recycled for reuse",
        "Surface Impoundment": "Chemicals stored in enclosed or open air pools or pounds.",
        "Underground Wells": "A release type involving pumping chemicals deep underground into specialized wells.",
        "Water": "Chemicals released as surface water discharge. Meaning chemicals that have either directly or indirectly been released into bodies of water on or off site."
    }

    function drawing(p5){

        let data
        let topAir
        let topLand
        let topLandfill
        let topRecycled
        let topSurface
        let topUnderground
        let topWater
        let topDisposalTypes

        let caslonFont


        function drawBars(startX, startY, spacing, strokeWidth, maxValue, maxWidth , data, column) {
            
            p5.strokeCap(p5.SQUARE)
            //p5.noSmooth()
            
            let yesNoBool = {
                "YES": true,
                "NO": false
            }

            let values = data.getColumn(column)
            let names = data.getColumn("Chemical")
            let metal = data.getColumn("Metal")
            let carcinogen = data.getColumn("Carcinogen")
            let PBT = data.getColumn("PBT")
            let PFAS = data.getColumn("PFAS")

            for (let i = 0; i < values.length; i++) {
                
                let isMetal = yesNoBool[metal[i]]
                let isCarcinogen = yesNoBool[carcinogen[i]]
                let isPBT = yesNoBool[PBT[i]]
                let isPFAS = yesNoBool[PFAS[i]]
                
                let endX = p5.max(startX+8, startX + Math.round(maxWidth*(parseInt(values[i])/maxValue)))
                
                if (isCarcinogen){
                    p5.stroke("#EA7979")
                }else if (isPBT){
                    p5.stroke("#F2CE6D")
                }else if (isPFAS){
                    p5.stroke("#9CEAE1")
                }else{
                    p5.stroke("#FFFFFF")
                }

                p5.strokeWeight(strokeWidth)
                p5.line(startX, startY, endX, startY)
                p5.strokeWeight(1)
                p5.textSize(14)
                p5.strokeWeight(0)
                p5.push()
                p5.textAlign(p5.RIGHT)
                p5.textFont(caslonFont)
                p5.fill("#ffffff")
                // p5.translate(startX,0);
                // p5.rotate(p5.radians(90))
                p5.text(names[i], startX - 10, startY+4)
                p5.textAlign(p5.LEFT) 
                p5.text(parseInt(values[i]).toLocaleString("en-US") + " Ibs", endX+10, startY+4)
                p5.pop()

                startY += spacing
            }     
        }
        
        p5.preload = () => {
            data = p5.loadTable(csvData, "csv", "header")
            topAir = p5.loadTable(topAirData, "csv", "header")
            topLand = p5.loadTable(topLandData, "csv", "header")
            topLandfill = p5.loadTable(topLandfillData, "csv", "header")
            topRecycled = p5.loadTable(topRecycledData, "csv", "header")
            topSurface = p5.loadTable(topSurfaceData, "csv", "header")
            topUnderground = p5.loadTable(topUndergroundData, "csv", "header")
            topWater = p5.loadTable(topWaterData, "csv", "header")
            
            topDisposalTypes = {
                "Air": topAir,
                "Land Treatment": topLand,
                "Landfill": topLandfill,
                "Recycled": topRecycled,
                "Surface Impoundment": topSurface,
                "Underground Wells": topUnderground,
                "Water": topWater
            }

            caslonFont = p5.loadFont(caslonBold)
        }

        p5.setup = () => {
            var sum = data.getColumn("Total Underground").reduce((accumulator, currentValue) => {
                return parseInt(accumulator) + parseInt(currentValue)
              }, 0);
            console.log(sum)
            
            p5.createCanvas(900, 800)
            p5.background("#1D8E63")
            drawBars(190, 18, 40, 15, 105000000, 100, topDisposalTypes[graph], graph)   
        }

        p5.draw = () => {
            return
        }

    }
 
    return(
        <>
            <ReactP5Wrapper sketch={drawing} />
            <h4 className='typeDescription'>{graphDescriptions[graph]}</h4>
        </>
    ) 
}
