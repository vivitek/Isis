import './App.css';
import github from "./github.svg"
import linkedin from "./linkedin.svg"

function App() {
  return (
    <div className="App">
      <header>
        <h1 style={{paddingTop: "10px"}}>Isis</h1>
        <h3>By vincipit</h3>
      </header>

      <div id="search">
        <input type="url" placeholder="Type your URL here"/><br/>
        <button>Submit</button>
      </div>

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
