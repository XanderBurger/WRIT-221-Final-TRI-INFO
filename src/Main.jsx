import React from 'react'
import "./Main.css"
import Graph from './Graph'

export default function Main() {

    const source5 = <a href="https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-present" target="_blank"><p> 1. Toxic Release Inventory Data</p></a>
    const source2 = <a href="https://www.sciencedirect.com/topics/earth-and-planetary-sciences/surface-water-pollution" target="_blank"><p> 2. Facts About Surface Water Pollution</p></a>
    const source3 = <a href="https://www.epa.gov/uic/general-information-about-injection-wells" target="_blank"><p> 3. Information on Underground Injection Wells</p></a>
    const source4 = <a href="https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-guide" target="_blank"><p> 4. Guid to the TRI Data Set</p></a>
    const source1 = <a href="https://www.epa.gov/toxics-release-inventory-tri-program" target="_blank"><p> 5. About the TRI Program</p></a>
    
  return (
    <div className='mainBody'>
        <div className='header'>
            <h1>EPA Toxic Release Inventory – 2021</h1>
            <h2>how and what chemicals are being disposed </h2>
        </div>
        <div className= 'bodyText'>
            <h3>What is the TRI Program?</h3>
            <p>
            
                The TRI or Toxic Release Inventory is a program run by the EPA to provide transparency on how and where chemicals that are harmful to human health are released into the environment. The program requires facilities to report where, how, and what chemicals are being disposed of. This data is then gathered by the EPA and released to the public. <sup>1</sup>

            <h3>History</h3>

                The TRI was established following the 1984 Bhopal Chemical Plant disaster which led to the death of thousands in India after a toxic gas leak, and a series of similar chemical leaks at a plant in West Virginia. Congress passed the Right-to-Know Act in 1986 which created the Toxic Release Inventory. Every year since designated facilities are required to report their chemical releases. <sup>1</sup> 

            <h3>About The Graphs</h3>
            
                These graphs are a summary of the most common disposal types reported by the TRI and the 20 most released chemicals in that disposal type. Also noted is if the chemical is classified as a carcinogen or Persistent Bioaccumulative Toxic (PBT) chemical. <sup>2, 3, 4, 5</sup>

            </p>
        </div>
        <div className='graph'>
            <h3>Top 20 Chemicals By Release Type</h3>
            <Graph/>
        </div>
        <div className='footer'> 
        <h3>Sources</h3>
        {source1}
        {source2}
        {source3}
        {source4}
        {source5}
        </div>
    </div>
  )
}
