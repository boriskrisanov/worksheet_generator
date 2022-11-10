import '../styles/globals.css'
import type {AppProps} from 'next/app'
import {TQuestion} from "../components/Question";
import {useState} from "react";

function MyApp({Component, pageProps}: AppProps) {
    const [questions, setQuestions] = useState<TQuestion[]>([])
    
    return (
        <Component {...pageProps} questions={questions} setQuestions={setQuestions}/>
    )
}

export default MyApp
