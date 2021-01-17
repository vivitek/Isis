import "./App.css";
import github from "./github.svg";
import linkedin from "./linkedin.svg";
import { useState } from "react";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import Button from "@material-ui/core/Button";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const App = () => {
  const [url, setUrl] = useState("");
  const [reportValue, setReportValue] = useState("");
  const [category, setCategory] = useState(undefined);

  const submit = () => {
    fetch(`${process.env.REACT_APP_API_URL}/${url}`)
      .then(async (res) => res.json())
      .then((res) => {
        setCategory(res.category);
        if (res.category === "") {
          toast("Nothing found!", {
            type: "error",
            position: toast.POSITION.BOTTOM_RIGHT,
            style: {
              backgroundColor: "#b53f3f",
              width: "450px",
            },
          });
        }
      });
  };

  const report = () => {
    fetch(`${process.env.REACT_APP_API_URL}/report`, {
      method: "POST",
      headers: { "Content-type": "application/json; charset=UTF-8" },
      body: JSON.stringify({ url, category: reportValue }),
    }).then(() => {
      toast("Thank you for your contribution!", {
        type: "success",
        position: toast.POSITION.BOTTOM_RIGHT,
        style: {
          backgroundColor: "#3fb58f",
          width: "450px",
        }
      });
      setCategory(undefined);
      setUrl("");
    });
  };

  return (
    <div className="App">
      <header>
        <h1 style={{ paddingTop: "10px" }}>X.A.N.A</h1>
        <h3>by vincipit</h3>
      </header>

      <div id="search">
        <input
          value={url}
          onChange={(e) => {
            setUrl(e.target.value.toLowerCase());
            if (category !== undefined) setCategory(undefined);
          }}
          type="url"
          placeholder="Type your URL here"
        />
        <br />
        <Button
          disabled={!/^[a-z0-9.]+\.[a-z]{2,}$/.test(url)}
          onClick={submit}
          variant="contained"
          color="primary"
        >
          Search
        </Button>
      </div>

      {category !== undefined && (
        <div class="result">
          {category !== "" ? (
            <div class="category">
              <img alt="logo" src={`https://favicon.splitbee.io/?url=${url}`} />
              <h3>It seems that your site is a(n) {category} site</h3>
              <Button
                style={{ width: "200px" }}
                variant="contained"
                color="secondary"
                onClick={() => {
                  setCategory("");
                }}
              >
                Report an error
              </Button>
            </div>
          ) : (
            <div class="category">
              <h3>
                This website enters in
                <Select
                  style={{
                    margin: "0px 15px",
                    color: "white",
                    width: "130px",
                    borderBottom: "1px solid white",
                  }}
                  value={reportValue}
                  onChange={(e) => {
                    setReportValue(e.target.value);
                  }}
                >
                  <MenuItem value="entertainment">entertainment</MenuItem>
                  <MenuItem value="education">education</MenuItem>
                  <MenuItem value="information">information</MenuItem>
                </Select>
                category
              </h3>
              <Button
                style={{ width: "25%", borderWidth: "2px" }}
                variant="contained"
                color="default"
                onClick={report}
                disabled={reportValue === ""}
              >
                Submit for review
              </Button>
            </div>
          )}
        </div>
      )}
      <ToastContainer />

      <footer>
        <a href="https://www.github.com/vivitek" target="blank" alt="github">
          <img align="center" alt="github" src={github} />
        </a>
        <a
          href="https://www.linkedin.com/company/vivi-network/about/"
          target="blank"
          alt="linkedin"
        >
          <img align="center" alt="linkedin" src={linkedin} />
        </a>
      </footer>
    </div>
  );
};

export default App;
