import React from "react";
import styles from "../styles/Worksheet.module.css";
import katex from "katex";
import "katex/dist/katex.css"

export interface TQuestion {
    question: string
    answer: string
    image_url?: string
    image_alt?: string
}

interface Props {
    question: TQuestion
    questionNumber: number,
    showAnswer: boolean,
    leaveSpace: boolean
}

const Question: React.FC<Props> = ({question, questionNumber, showAnswer, leaveSpace}) => {
    const questionString = katex.renderToString(question.question)
    const answerString = katex.renderToString(question.answer)

    return (
        <div>
            <p>
                {questionNumber}) <span dangerouslySetInnerHTML={{
                __html: questionString
            }}></span>
            </p>
            {question.image_url && (
                // TODO: Set this URL depending on the environment we're running in (dev or prod)

                <img width={400} height={300} src={"http://localhost:5000" + question.image_url} alt={question.image_alt}/>
            )}
            <p hidden={!showAnswer} className={styles.answer}>
                Answer: <span dangerouslySetInnerHTML={{
                __html: answerString
            }}/>
            </p>
            {leaveSpace && (
                <div>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                </div>
            )}
            <br/>
        </div>
    )
}

export default Question