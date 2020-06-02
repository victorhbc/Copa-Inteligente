import React, { useState, useEffect } from "react";
import getVantaOptions from "../../utils/BackgroundColorHandler";
import TextArea from "../../components/TextArea";
import HourArea from "../../components/HourArea";
import FirebaseInterface from "../../services/FirebaseInterface";
import panIcon from "../../assets/pan.png";
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import "./style.css";

export default function Counter() {
  const [numPeopleState, setNumPeopleState] = useState([null]);
  const [hourPeopleState, setHourPeopleState] = useState([null]);
  const [ignoreFetchState, setIgnoreState] = useState(false);
  const firebaseInterface = new FirebaseInterface();
  const changeBackgroundColor = num_people => {
    window.BACKGROUND.options = getVantaOptions(num_people);
  };

  useEffect(() => {
    firebaseInterface.unsubscribe();
    firebaseInterface.changesObserver(null, "kitchen_data", docData => {
      if (docData) {
        if (!ignoreFetchState) {
          setIgnoreState(true);
          const currentDate = docData[docData.length - 1].data();
          const currentDateKeys = Object.keys(currentDate);
          const currentKitchenData = currentDate[currentDateKeys[currentDateKeys.length - 1]];

          setHourPeopleState(currentDateKeys[currentDateKeys.length - 1])
          setNumPeopleState(currentKitchenData.num_people);
          changeBackgroundColor(currentKitchenData.num_people);
        }
      }
    });
  });

  return (
    <div className="App">
      <div className="appContainer">
        <div className="relButton">
            <Button href="/chart" style={{color: '#000000'}}>Relatorio</Button>
        </div>
        <img src={panIcon} alt="Icone da panela" className="icon" />
        <div className="infoText">
          <TextArea num_people_in_the_kitchen={numPeopleState} />
          {/* <HourArea hour={hourPeopleState} /> */}
        </div>
      </div>
    </div>
  );
}
