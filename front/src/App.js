import './App.css';
import github from "./github.svg"
import linkedin from "./linkedin.svg"
import { useState } from 'react'

const App = () => {
  const [url, setUrl] = useState("")
  const [category, setCategory] = useState(undefined)

  const submit = async () => {
    fetch(`http://localhost:8080/${url}`)
      .then(async res => res.json())
      .then(res => {
        setCategory(res.category)
      })
  }

  const submitError = async (e) => {
    e.preventDefault()
    console.log(e.target[0].value)
  }

  return (
    <div className="App">
      <header>
        <h1 style={{paddingTop: "10px"}}>X.A.N.A</h1>
        <h3>by vincipit</h3>
      </header>

      <div id="search">
        <input value={url} onChange={(e) => {
          setUrl(e.target.value)
        }} type="url" placeholder="Type your URL here"/><br/>
        <button
          disabled={url.match("^[a-z0-9\.]+\.[a-z]{2,}$") ? false : true}
          onClick={submit}
        >Submit</button>
      </div>

      {typeof category === "string" && <div class="result">
          {category !== "" ?
            <div class="category">
              <h3>Wow, we found something !</h3>
              <h3>It seems that your site is a.n {category} site</h3>
            </div>
          :
            <div class="category">
              <h3>Nothing found ☹</h3>
              <h3>Please contact us.</h3>
            </div>
          }
          </div>
      }

      <footer>
        <a href="https://www.github.com/vivitek" target="blank" alt="github">
          <img align="center" alt="github" src={github}/>
        </a>
        <a href="https://www.linkedin.com/company/vivi-network/about/" target="blank" alt="linkedin">
          <img align="center" alt="linkedin" src={linkedin}/>
        </a>
      </footer>
    </div>
  );
}

export default App;
