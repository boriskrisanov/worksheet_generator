import {Button, CircularProgress, TextField} from "@mui/material"
import type {NextPage} from "next"
import Head from "next/head"
import TopicSelector from "../components/TopicSelector"
import styles from "../styles/Home.module.css"
import {FormEvent, useState} from "react";
import {TQuestion} from "../components/Question";
import {useRouter} from "next/router";

interface Props {
    questions: TQuestion[]
    setQuestions: (questions: TQuestion[]) => void
}

const Home: NextPage<Props> = ({setQuestions}) => {
    const router = useRouter()
    const [loading, setLoading] = useState(false)

    function submit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const form = document.getElementById("form") as HTMLFormElement
        let formData = new FormData(form)

        let numQuestions;
        const topics: string[] = []
        const difficulties = {}
        // @ts-ignore
        for (let [key, value] of formData.entries()) {
            if (key == "questions") {
                numQuestions = parseInt(value)
            } else if (key.endsWith("_difficulty")) {
                // @ts-ignore
                difficulties[key.substring(0, key.indexOf("_difficulty"))] = parseInt(value)
            } else {
                topics.push(key)
            }
        }

        const topicsJSON = topics.map((topic) => {
            // @ts-ignore
            const difficulty = difficulties[topic]
            if (!difficulty) {
                return {name: topic}
            }
            return {name: topic, difficulty: difficulty}
        })

        const body = JSON.stringify({
            questions: numQuestions,
            topics: topicsJSON
        })

        // TODO: Set this URL depending on the environment we're running in (dev or prod)
        fetch("http://localhost:5000/worksheet", {
            method: "POST",
            body: body,
            headers: {
                "Content-Type": "application/json"
            }
        }).then(async res => {
            const json = await res.json()
            setQuestions(json.questions)
            await router.push("/worksheet")
        })

    }

    return (
        <div className={styles.home}>
            <Head>
                <title>Worksheet generator</title>
                <meta name="viewport" content="initial-scale=1, width=device-width"/>
            </Head>

            <h1>Worksheet generator</h1>

            <form onSubmit={submit} id="form">
        <span className={styles.numberOfQuestions}>
          <TextField
              name="questions"
              size="medium"
              variant="outlined"
              label="Number of questions"
              type="number"
          />
        </span>
                <span className={styles.generateButton}>
          <Button type="submit" variant="contained" disabled={loading} onClick={() => setLoading(true)}>
            Generate
              <CircularProgress style={{
                  position: "absolute",
                  display: loading ? "block" : "none"
              }}/>
          </Button>
        </span>
                <TopicSelector
                    name="linear_equations"
                    topic="Linear equations"
                    maxDifficulty={4}
                />
                <TopicSelector
                    name="simultaneous_equations"
                    topic="Simultaneous Equations"
                />
                <TopicSelector
                    name="factorising_quadratics"
                    topic="Factorising quadratics"
                />
                <TopicSelector
                    name="solving_quadratics"
                    topic="Solving quadratics"
                />
                <TopicSelector
                    name="pythagoras_theorem"
                    topic="Pythagoras' theorem"
                />
                <TopicSelector
                    name="right_angle_trig_missing_sides"
                    topic="Finding missing sides in right angled triangles"
                />
                <TopicSelector
                    name="right_angle_trig_missing_angles"
                    topic="Finding missing angles in right angled triangles"
                />
                <TopicSelector
                    name="simplifying"
                    topic="Simplifying"
                />
                <TopicSelector
                    name="index_laws"
                    topic="Index laws"
                />
            </form>
        </div>
    )
}

export default Home
