import React, {useEffect, useState} from "react";
import styles from "../styles/Worksheet.module.css"
import {FormControlLabel, Switch} from "@mui/material";
import Question, {TQuestion} from "../components/Question";
import {useRouter} from "next/router";
import {NextPage} from "next";

interface Props {
    questions: TQuestion[]
}

const Worksheet: NextPage<Props> = ({questions}) => {
    const router = useRouter()

    useEffect(() => {
        if (questions.length == 0) {
            router.push("/")
        }
    })

    const [showAnswers, setShowAnswers] = useState(false)
    const [leaveSpace, setLeaveSpace] = useState(false)

    const questionElements = questions.map((question, index) =>
        <Question key={index} question={question} questionNumber={index + 1} showAnswer={showAnswers}
                  leaveSpace={leaveSpace}/>
    )

    return (
        <div className={styles.worksheet}>
            <FormControlLabel
                control={<Switch onClick={() => setShowAnswers(!showAnswers)}/>}
                label="Show answers"
            />
            <FormControlLabel
                control={<Switch onClick={() => setLeaveSpace(!leaveSpace)}/>}
                label="Leave space to show working"
            />
            {questionElements}
        </div>
    )
}

export default Worksheet