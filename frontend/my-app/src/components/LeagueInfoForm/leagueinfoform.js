import React, { useEffect } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Table from "react-bootstrap/Table";
import { useState } from "react";

export default function LeagueInfoForm() {
  const [formData, setFormData] = useState({
    leagueSize: "",
    category1: "",
    category2: "",
  });
  const [hasResult, setHasResult] = useState(false);
  const [resData, setResData] = useState();

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = async (event) => {
    try {
      // alert(
      //   `League Size: ${formData.leagueSize}, Category 1: ${formData.category1}, Category 2: ${formData.category2}`
      // );
      const response = await fetch(
        `http://127.0.0.1:8000/season_stats?rank_threshold=${formData.leagueSize}&cat1=${formData.category1}&cat2=${formData.category2}`
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setResData(data); // Update the state variable with the response data
      setHasResult(true);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <>
      <Form.Select
        name="leagueSize"
        value={formData.leagueSize}
        onChange={handleChange}
      >
        <option>How many players are in your league?</option>
        <option value="130">10-Team League</option>
        <option value="156">12-Team League</option>
        <option value="182">14-Team League</option>
        <option value="208">16-Team League</option>
        <option value="234">18-Team League</option>
        <option value="260">20-Team League</option>
      </Form.Select>
      <br />
      <Form.Select
        name="category1"
        value={formData.category1}
        onChange={handleChange}
      >
        <option>Category 1</option>
        <option value="pV">Points</option>
        <option value="3V">3 Pointers</option>
        <option value="rV">Rebounds</option>
        <option value="aV">Assists</option>
        <option value="sV">Steals</option>
        <option value="bV">Blocks</option>
        <option value="fgpV">Field Goal Percentage</option>
        <option value="ftpV">Free Throw Percentage</option>
        <option value="toV">Turnovers</option>
      </Form.Select>
      <br />
      <Form.Select
        name="category2"
        value={formData.category2}
        onChange={handleChange}
      >
        <option>Category 2</option>
        <option value="pV">Points</option>
        <option value="3V">3 Pointers</option>
        <option value="rV">Rebounds</option>
        <option value="aV">Assists</option>
        <option value="sV">Steals</option>
        <option value="bV">Blocks</option>
        <option value="fgpV">Field Goal Percentage</option>
        <option value="ftpV">Free Throw Percentage</option>
        <option value="toV">Turnovers</option>
      </Form.Select>
      <br />
      <Button variant="primary" onClick={handleSubmit}>
        Tell me who to stream!
      </Button>
      <br />
      <br />
      {hasResult ? (
        <Table striped>
          <thead>
            <tr>
              <th>Round</th>
              <th>Rank</th>
              <th>Value</th>
              <th>Player</th>
              <th>Team</th>
              <th>POS</th>
              <th>INJ</th>
              <th>GP</th>
              <th>MPG</th>
              <th>PPG</th>
              <th>3PG</th>
              <th>RPG</th>
              <th>APG</th>
              <th>SPG</th>
              <th>BPG</th>
              <th>FG%</th>
              <th>FGAPG</th>
              <th>FT%</th>
              <th>FTAPG</th>
              <th>ToPG</th>
              <th>3P%</th>
              <th>3PAPG</th>
              <th>2P%</th>
              <th>2PAPG</th>
              <th>pV</th>
              <th>3V</th>
              <th>rV</th>
              <th>aV</th>
              <th>sV</th>
              <th>bV</th>
              <th>fgpV</th>
              <th>ftpV</th>
              <th>toV</th>
            </tr>
          </thead>
          <tbody>
            {resData.map((numList, i) => (
              <tr key={i}>
                {numList.map((num, j) => (
                  <td key={j}>{num}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </Table>
      ) : (
        <p>no result</p>
      )}
    </>
  );
}
