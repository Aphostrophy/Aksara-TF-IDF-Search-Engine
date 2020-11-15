import React from "react";
import "./style.scss";

function About(){
    return(
        <div className="about">

            <div className="concept">
                <div className="container-img-concept">
                    <div className="img-concept"></div>
                </div>
                <div className="content-concept">
                    <p>Search engine ini dibuat dengan menggunakan metode <i>cosine similarity</i> untuk menentukan relevansi sebuah dokumen dengan query yang dimasukkan.</p>
                    <p>Metode <i>cosine similarity</i> dilakukan dengan cara memodelkan seluruh dokumen dan query menjadi vektor yang menyatakan kemunculan kata-kata dalam dokumen/query tersebut.</p>
                    <p>Kemudian untuk menentukan relevansi suatu dokumen, dilakukan penghitungan <i>similarity</i> yang merupakan penurunan dari konsep perkalian titik vektor.</p>
                    <p>Semakin tinggi nilai similarity antara suatu dokumen dengan query, maka dokumen tersebut semakin relevan dengan query.</p>
                </div>
            </div>

            <div className="container-img-htu">
                    <div className="img-htu"></div>
            </div>

            <div className="container-htu">
                <div className="content-htu">
                    <p><b>Mode search pada dokumen</b></p>
                    <p>1. Upload file pada page uploader</p>
                    <p>2. Tekan tombol search di bawah uploader</p>
                    <p>3. Masukan query pada search bar kemudian tekan tombol search</p>
                    <p>4. Hasil akan ditampilkan pada halaman berbeda, klik judul file untuk menampilkan isi cerita</p>
                    <br />
                    <p><b>Mode search pada web (<i>webscraping</i>)</b></p>
                    <p>1. Klik 'search' pada navbar</p>
                    <p>2. Klik tombol checklist pada navbar untuk mengaktifkan mode webscraping</p>
                    <p>3. Masukan query pada search bar kemudian tekan tombol search</p>
                    <p>4. Hasil akan ditampilkan pada halaman berbeda, klik judul file untuk mengunjungi web asli dari cerita tersebut</p>
                </div>
            </div>


            <div className="container-img-about">
                <div className="img-header-about"></div>
            </div>
            <div className="container-profil">
                <div className="jesson">
                </div>
                <div className="member">
                    <div className="img-jesson"></div>
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