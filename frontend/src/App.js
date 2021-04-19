import { ToggleSection } from "quick-n-dirty-react"
import { ModelEditor, Timeseries3D } from "timeseries-3d"
import React from "react"
import util from "quick-n-dirty-utils"
import demoModel from "./model3d-export.json"
import demoDataSingle from "./model-data-single.json"
import demoDataMulti from "./model-data-multi.json"


const style = {
    main: {
        padding: "10px",
    },
}

const App = () => (
    <div style={style.main}>
        <ToggleSection label="Editor">
            <ModelEditor model={demoModel} />
        </ToggleSection>
        <hr />
        <ToggleSection label="Visualisation (model)">
            <Timeseries3D model={demoModel} />
        </ToggleSection>
        <ToggleSection label="Visualisation (single)">
            <Timeseries3D model={demoModel} data={demoDataSingle}/>
        </ToggleSection>
        <ToggleSection label="Visualisation (multi)" show>
            <Timeseries3D model={demoModel} data={demoDataMulti} autoplay inverse />
        </ToggleSection>
    </div>
)

export default App
