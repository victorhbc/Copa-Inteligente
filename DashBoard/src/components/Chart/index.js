import React, { useState, useEffect } from 'react';
import getVantaOptions from "../../utils/BackgroundColorHandler";
import FirebaseInterface from "../../services/FirebaseInterface";
import Button from 'react-bootstrap/Button';
import { Chart } from "react-google-charts";
import "./style.css";

export default function Charts(props) {
  const model = [["Horários", "Pessoas"], ['10:30',0],['10:45',0],['11:00', 0], ['11:15', 0], ['11:30', 0], ['11:45', 0], ['12:00', 0], ['12:15', 0], ['12:30', 0], ['12:45', 0], ['13:00', 0], ['13:15', 0], ['13:30', 0], ['13:45', 0], ['14:00', 0],['14:15', 0],['14:30', 0]]
  const horasFixed = ['10:30','10:45','11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30'];
  let relatorio;
  var horasToAverage = [];
  var horasIndex = [];
  
  const [currentDay, setCurrentDay] = useState(null) 
  const [horasState, setHorasState] = useState([null]);
  const [ignoreFetchState, setIgnoreState] = useState(false);
  const firebaseInterface = new FirebaseInterface();
  const changeBackgroundColor = num_people => {
    window.BACKGROUND.options = getVantaOptions(num_people); 
  };

  useEffect(() => {

    firebaseInterface.unsubscribe();
    firebaseInterface.changesObserver(null, "kitchen_data", docData => {
      if (docData) {
        
        /* Pega ultima data do banco de dados e converte para string e imprime no gráfico como título */
        let currentInfo = docData.slice(-1).pop()
        let formatDate = currentInfo._document.key.path.segments.slice(-1).pop()
        let arrayDate = formatDate.split('-')
        arrayDate = arrayDate[2] +'/'+ arrayDate[1] +'/'+ arrayDate[0]
        
        /* Definindo variável título do gráfico */
        setCurrentDay(arrayDate)

        if (!ignoreFetchState) {
          let currentDate = docData.slice(-1)
          relatorio = model;
          horasToAverage = [];
          horasIndex = [];

          /* Ultimas informações do banco referente a hora e quantidade de pessoas */
          currentDate.forEach((element, index) => {
            element = element.data()
            let aux = [];
            let currentDateKeys = Object.keys(element)
            currentDateKeys.forEach((element, index) => {
              if (horasFixed.indexOf(element) !== -1) aux.push(element)
            })
            horasIndex.push(aux)
          });

          horasIndex.forEach((element, index) => {
            let val = [];
            let arrayAux = []
            element.forEach((element) => {
              val.push(element)
            })

            val.forEach((element) => {
              let aux = element;
              try {
                element = currentDate[index].data();
              } catch (error) {
                // console.log("Encontrei um error: " + error)
              }
              arrayAux.push(element[aux]);
            })

            horasToAverage.push(arrayAux)
          })


          /* Compara as informações retornadas do banco de dados com as variáveis definidas nas linhas 9 e 10 (model ; horasFixed) */
          /* Se forem iguais as informações serão atribuidas as varáveis (relatorio ; horasIndex ; horasToAverage) */
          horasIndex.forEach((element, index) => {
            element.forEach((element2, index2) => {
              relatorio.forEach((element3, index3) => {
                if (element3[0] === element2 && element[index2] !== 0) {
                  if (relatorio[index3][1] === 0) {
                    relatorio[index3][1] = horasToAverage[index][index2].num_people
                  }
                }
              })
            })
          })
          
          /* Define os valores para serem plotados no gráfico */
          setHorasState(relatorio)
          
        }
      }
    });
  });

  return (
    <div>
      <div className="relButton">
        <Button href="/">Voltar</Button>
      </div>
      <div className="Charts">
      
      <Chart
        width={'900px'}
        height={'500px'}
        chartType="Bar"
        loader={<div>Loading Chart</div>}
        data={(horasState[0] != null) ? horasState : model}
        options={{
          chart: {
            title: 'Gráfico referente: ' + currentDay
          },
        }}
        rootProps={{ 'data-testid': '3' }}
      />
      </div>
    </div>
  );
}
