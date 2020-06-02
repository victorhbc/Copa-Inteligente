import React from "react";
import "./style.css";

export default function TextArea(props) {
  return (
    <div className="TextArea">
      <div className="info_hour">
        <div className="hour">
          <p>{props.hour}</p>
        </div>
        <div className="text_info_hour">
          <p>
            {" "}
            ultima hora <br />
            atualizada.{" "}
          </p>
        </div>
      </div>
    </div>
  );
}
