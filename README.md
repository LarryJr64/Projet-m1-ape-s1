# Projet-m1-ape-s1 (`･Д･)ノ=☆

## Table de Matières 
1. Introduction
2. Packages 
3. Description
4. Auteurs 


## Introduction

Le projet consiste à prédir l'avenir et à donner des conseils en utilisant l'horoscope, la boule de cristal (boule de destin et boule d'amour) mais également à utiliser les runes et leur tirage pour rendre notre avenir plus clair et supprimer nos doutes. 
Les prédiction seront précises et claires.

Le projet a été réalisé sur Python 3.9.


## Packages 

Le fonctionnement du code nécessite l'installation de "Selenium". Cependant, Selenium, à son tour, nécessite l'installation d'un web driver. Le type de web driver va dépendre de votre outil de recherche. En général, pour Fox le web driver est déjà installé alors que les utilisateur de Chrome et de Edge vont devoir télécharger le web driver correspondant à leur version de l'outil de recherche.
Après ces installations, plusieurs packages sont nécessaires, encore une fois selon l'outil de recherche, dans le projet, nous utilisons Chrome. Les packages sont les suivants:

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


Chacun de ces pachages sera utilisé dans le projet. Le package By va nous permettre de récupérer des éléments sur un site donné, Webdriverwait et EC vont nous permettre de créer des conditions à vérifier avec un temps donné, et pour finir, Options vont enlever des notifications et les cookies.


## Description
 
Le projet est composé de trois parties: horoscope, boule de cristal, tirage de runes. Le code pour chaque partie marche avec des fontions. 

### Horoscope 

La première partie du projet permet de connaitre son horoscope du jour en définissant son jour et son mois de naissance. Après avoir trouvé le signe astrologique, l'utilisateur doit faire un choix de thème, à savoir choisir entre l'amour, le travail, la finance, le bien-être et l'entourage. Chaque thhème est détaillé et les prédictions sont mises à jour tous les jours. 
Les prédictions sont accompagnées d'étoiles ou de coeurs (pour la partie amour). Le nombre des ces étoiles ou de coeurs (au nombre de 6) indique le niveau de chance.

### Boule de Cristal

La deuxième partie permet d'avoir des conseil sur l'amour et des précisions sur le destin. 
Il y a 3 différentes boules: boule de cristal qui permet de poser une question, la boule de destin qui nous révèle ce que l'avenir nous réserve et la boule d'amour qui nous conseil sur notre situation et fait des prédictions. 

Les 2 dernières boules fonctionnent avec une simple connexion d'esprits entre l'utilisateur et la boule et donc nous ne pouvons pas poser de questions explicites, il faut simplement penser à tout ce qui nous préoccupe. 

### Tirage des runes

Les runes sont au nombre de 24 et chacune d'elles a une signification brien précise. Comme les boules, ici encore la connexion d'esprit. 
Cette partie nous permet de tirer au sort 3 runes et d'avoir une interprétation pour chaque rune. 


## Auteurs

- Claude Roussaux
- Mariam Harutyunyan

M1 - APE - Data Science pour l'économie et l'entreprise du futur.
Faculté des Sciences Economiques et de la Gestion, Université de Strasbourg
