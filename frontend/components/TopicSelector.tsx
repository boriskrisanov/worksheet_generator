import { Checkbox, FormControl, FormControlLabel, Slider } from "@mui/material"
import React, { useState } from "react"
import style from "../styles/TopicSelector.module.css"

interface Props {
  topic: string
  name?: string
  maxDifficulty?: number
}

const TopicSelector: React.FC<Props> = ({ topic, name, maxDifficulty = 1 }) => {

  const [selected, setSelected] = useState(false)
  const [difficulty, setDifficulty] = useState(1)

  return (
    <div className={style.topicSelector}>
      <FormControlLabel name={name} control={<Checkbox onClick={() => setSelected(!selected)} />} label={topic} />
      {selected && maxDifficulty > 1 && (
        <div className={style.difficultySlider}>
          <p>Difficulty</p>
          <FormControl>
            <input onChange={() => {
              // Not adding an onChange handler results in console errors even though it works fine
            }} name={name + "_difficulty"} value={difficulty} style={{
              display: "none"
            }} />
          </FormControl>
          <Slider onChange={(_, v) => {
            setDifficulty(v as number)
          }} defaultValue={1} marks step={1} min={1} max={maxDifficulty} valueLabelDisplay="auto" />
        </div>
      )}
    </div>
  )
}

export default TopicSelector
