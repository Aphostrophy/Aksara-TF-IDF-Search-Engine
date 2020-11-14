import React from "react";
import "./style.scss";

function About(){
    return(
        <div className="about">
            <div className="container-img-about">
                <div className="img-header-about"></div>
            </div>
            <div className="container-profil">
                <div className="jesson">
                </div>
                <div className="member">
                    <div className="img-marcello"></div>
                    <p><b>Jesson Gossal Yo</b> 
                    <br/> 13519079
                    </p>
                </div>
                <div className="member">
                    <div className="img-marcello"></div>
                    <p><b>Marcello Faria</b> 
                    <br/> 13519086
                    </p>
                </div>
                <div className="member">
                    <div className="img-hera"></div>
                    <p><b>Hera Shafira</b><br/>
                    13519131
                    </p>
                </div>               
            </div>
        </div>
    )
}

export default About