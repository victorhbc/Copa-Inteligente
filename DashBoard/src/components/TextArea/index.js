import React from "react";
import "./style.css";

function chooseTextToShow(num_people) {
  let textToShow = "";

  if (num_people < 6) {
    textToShow = "disponível";
  } else if (num_people < 11) {
    textToShow = "movimentada";
  } else {
    textToShow = "lotada";
  }

  return textToShow;
}

export default function TextArea(props) {
  return (
    <div className="TextArea">
      <div className="header">
        <p>M.E.C {chooseTextToShow(props.num_people_in_the_kitchen)}</p>
      </div>
      <div className="info">
        <div className="num_people">
          <p>{props.num_people_in_the_kitchen}</p>
        </div>
        <div className="text_info">
          <p>
            {" "}
            pessoas usando no <br />
            momento.{" "}
          </p>
        </div>
      </div>
    </div>
  );
}
