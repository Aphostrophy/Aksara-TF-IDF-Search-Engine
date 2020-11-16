# Algeo02-19079
# Project Name
> Aksara

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Important](#important)
* [Features](#features)
* [Status](#status)
* [Contact](#contact)

## General info
Project ini merupakan tugas besar Algeo ITB ke 2. Project ini dibuat dengan menggunakan framework React.js dengan create-react-app dan Flask. 
Tujuan dari project ini adalah untuk membuat Search Engine sederhana menggunakan metode Term Frequency sebagai aplikasi dot product dan vektor yang dapat menerima inputan file dan melakukan Search query berdasarkan dokumen yang dimasukkan.

## Screenshots
![Halaman Utama](./src/screenshot.jpg)

## Technologies
* Flask - version 1.1.2
* React.js - version 7.10.4
* Axios
* Beautifulsoup - version 4.9.3
* NLTK - version 3.5
* regex - version 2020.11.13
* Dependencies lainnya

## Setup
- git clone
- yarn install di frontend folder
- pipenv install di backend folder, Jika tidak memiliki pipenv bisa install pipenv dengan pip atau install semua lockfile secara manual(tidak disarankan karena pip menginstall secara global)
  
  Untuk menyalakan frontend
   - Tambahkan file .env yang setara dengan package.json pada folder frontend dan tulis
      REACT_APP_URL = http://localhost:5000/api jika belum ada
   - yarn start
   
  Untuk menyalakan backend
   - python installSisanya.py (untuk mendownload dictionary nltk)
   - pipenv shell
   - python app.py

   
## Important
- 15 file .html sudah ada di folder ../src/backend/static.
- Website https://www.worldoftales.com/ yang digunakan untuk webscraping terkadang mengalami down, silakan cek status web di https://www.isitdownrightnow.com/
- Perbedaan konfigurasi network Anda tidak menjamin bahwa tidak akan mempengaruhi hasil dari webscraping karena bisa ditolak oleh target webscrap


## Features
List of features ready and TODOs for future development :
* Multiple-upload file with drag and drop or onclick features
* Normal mode and Webscrap mode features 
* Search query from documents features

## Status
Project is: finished.

## Contact
Created by 
- Jesson Gosal Yo (13519079)
- Marcello Faria (13519086)
- Hera Shafira (13519131)
