import React from 'react';
import './style.css';
import panIcon from '../../assets/pan.png';

export default function PanIcon(props) {
	return (
		<div className="PanIcon">
			<img src={panIcon} alt="Icone da panela" className="icon" />
		</div>
	);
}
