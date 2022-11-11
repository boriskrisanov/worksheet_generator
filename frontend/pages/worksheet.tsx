import React, {useEffect, useState} from "react";
import styles from "../styles/Worksheet.module.css"
import {Button, FormControlLabel, Switch} from "@mui/material";
import Question, {TQuestion} from "../components/Question";
import {useRouter} from "next/router";
import {NextPage} from "next";
import Head from "next/head";

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
            <Head>
                {/*This route should not be indexed because its content depends on the form in index.tsx*/}
                <meta name="robots" content="noindex"/>
                <title>Worksheet Generator</title>
            </Head>
            <span className={styles.hiddenOnPrint}>
            <FormControlLabel
                control={<Switch onClick={() => setShowAnswers(!showAnswers)}/>}
                label="Show answers"
            />
            <FormControlLabel
                control={<Switch onClick={() => setLeaveSpace(!leaveSpace)}/>}
                label="Leave space to show working"
            />
            <Button variant="contained" onClick={() => window.print()}>
                <img className={styles.printIcon} src="/icons/print.svg" alt="Printer icon"/>
                Print
            </Button>
            </span>
            {questionElements}
        </div>
    )
}

export default Worksheet