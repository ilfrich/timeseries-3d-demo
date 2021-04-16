import { ToggleSection } from "quick-n-dirty-react"
import { ModelEditor } from "timeseries-3d"
import React from "react"


const style = {
    main: {
        padding: "10px",
    },
}

const App = () => (
    <div style={style.main}>
        <ToggleSection label="Editor" show>
            <ModelEditor model={{ layers: [{ components: [], height: 50 }]}} />
        </ToggleSection>
        <hr />
    </div>
)

export default App
