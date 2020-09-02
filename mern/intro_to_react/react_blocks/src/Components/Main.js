import React, { Component } from "react";
import styles from "./CSS/main.module.css";

class Main extends Component {
	render() {
		return <div className={styles.main}>{this.props.children}</div>;
	}
}

export default Main;
