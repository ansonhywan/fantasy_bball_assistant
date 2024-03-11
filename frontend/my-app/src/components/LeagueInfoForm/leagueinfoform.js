import React from 'react'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'
import { useState } from "react";

export default function LeagueInfoForm() {
  const [formData, setFormData] = useState({leagueSize: "",category1: "",category2: ""});

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`League Size: ${formData.leagueSize}, Category 1: ${formData.category1}, Category 2: ${formData.category2}`
    );
};

  return (
    <>
      <Form.Select name="leagueSize" value={formData.leagueSize} onChange={handleChange}>
        <option>How many players are in your league?</option>
        <option value="10-team-league">10-Team League</option>
        <option value="12-team-league">12-Team League</option>
        <option value="14-team-league">14-Team League</option>
        <option value="16-team-league">16-Team League</option>
        <option value="18-team-league">18-Team League</option>
        <option value="20-team-league">20-Team League</option>
      </Form.Select>
      <br />
      <Form.Select name="category1" value={formData.category1} onChange={handleChange}>
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
      <Form.Select name="category2" value={formData.category2} onChange={handleChange}>
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
      <Button variant="primary" onClick={handleSubmit}>Tell me who to stream!</Button>
    </>
  );
}
