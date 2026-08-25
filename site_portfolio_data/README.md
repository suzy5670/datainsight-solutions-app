# Présentation de l'équipe

## DataInsight Solutions

Projet réalisé en binôme dans le cadre de la formation Data Analyst à Simplon Lyon.

---

### Suz Didolène Massamouna

Experte en Systèmes d'Information (Bac+5), forte d'une solide expérience en administration systèmes et réseaux, en reconversion vers la Data Analysis. Combine rigueur infrastructurelle et compétences analytiques (SQL, Power BI, Python) pour transformer la donnée en leviers de décision.

🌐 [Portfolio](https://suzy5670.github.io/) · 🔗 [LinkedIn](https://www.linkedin.com/in/suz-didolene-massamouna/) · 💻 [GitHub](https://github.com/suzy5670)

### Zohair Nazhaoui

Analyste curieux, passé du terrain à la data sans perdre le sens du concret. 15 ans à piloter des équipes et des indicateurs business dans le commerce et le tourisme, aujourd'hui tourné vers l'analyse de données.

🌐 [Portfolio](https://zohair69.github.io/) · 💻 [GitHub](https://github.com/Zohair69)

---

Ensemble, l'équipe a conçu et déployé ce dashboard Streamlit pour DataInsight Solutions, de la modélisation des données jusqu'à la mise en ligne sur le cloud.
# DataInsight Solutions — Dashboard d'Analyse de Données

Application web interactive développée avec Streamlit dans le cadre du brief *"Développement et déploiement d'une application Web Data avec Streamlit"* — Formation Data Analyst, Simplon Lyon.

**Contexte** : l'entreprise fictive **DataInsight Solutions** souhaite moderniser la restitution de ses travaux d'analyse via une interface web interactive, versionnée avec Git et hébergée dans le cloud.

**Équipe** : Suz Didolène Massamouna & Zohair Nazhaoui

## Démo en ligne

- 🚀 **Application déployée** : [datainsight-suz-zohair.streamlit.app](https://datainsight-suz-zohair.streamlit.app/)
- 📦 **Dépôt GitHub** : [github.com/suzy5670/datainsight-solutions-app](https://github.com/suzy5670/datainsight-solutions-app)

## Portfolios de l'équipe

- Suz Didolène Massamouna : [suzy5670.github.io](https://suzy5670.github.io/)
- Zohair Nazhaoui : [zohair69.github.io](https://zohair69.github.io/)

## Fonctionnalités

- 🔐 Authentification sécurisée via fichier CSV (`accounts.csv`)
- ✈️ Visualisation interactive du dataset `flights` (Seaborn) : mise en cache des données (`@st.cache_data`)
- 🎚️ Filtres dynamiques : plage d'années (slider), mois (menu déroulant)
- 📈 3 indicateurs clés (KPI) : total de passagers, moyenne mensuelle, mois le plus chargé
- 📊 Graphiques interactifs : évolution annuelle (line chart), moyenne par mois (bar chart)
- 🔥 Heatmap Seaborn : répartition des passagers par mois × année
- 🖼️ Galerie de photos (thème aéroport/aviation) en disposition 3 colonnes
- 📋 Menu latéral de navigation (`streamlit-option-menu`)

## Méthodologie de mise en place

Le projet a suivi une progression en 6 guides, chacun validé avant de passer au suivant :

1. **Environnement** : `venv` Python isolé + Git + `.gitignore` (rien de sensible ni de lourd sur GitHub)
2. **Portfolio HTML/CSS** individuel, publié sur GitHub Pages
3. **Première application Streamlit** + exercice sur un jeu de données Seaborn
4. **Data visualisation interactive** : cache, graphiques natifs, heatmap Seaborn
5. **Authentification CSV**, navigation par menu, galerie multi-colonnes
6. **Déploiement** sur Streamlit Cloud via `requirements.txt` et GitHub

Le dépôt final est organisé en **2 dossiers** pour séparer clairement les responsabilités :

datainsight-solutions-app/
├── streamlit/ # Le code de l'application
│ ├── app.py
│ ├── accounts.csv
│ └── requirements.txt
├── site_portfolio_data/ # Références aux portfolios de l'équipe
│ └── README.md
└── .gitignore




## Difficultés rencontrées et solutions

| Difficulté | Solution |
|---|---|
| `pip install` installait les paquets dans le Python global au lieu du `venv` (PATH ambigu sur Windows) | Toujours utiliser `python -m pip install` / `python -m streamlit run` plutôt que `pip`/`streamlit` seuls |
| `requirements.txt` généré illisible (encodage UTF-16 au lieu d'UTF-8 via PowerShell) | Régénéré avec `Out-File -Encoding utf8` |
| `FileNotFoundError: accounts.csv` au déploiement sur Streamlit Cloud | Le chemin `"accounts.csv"` était relatif au dossier de lancement, pas au script — corrigé avec un chemin basé sur `os.path.dirname(__file__)` |
| Connexion en boucle sur Streamlit Cloud (`accounts.csv` absent du dépôt) | Le fichier avait été exclu par erreur dans le `.gitignore` — retiré et commité |
| `git push` refusé ("fetch first") | Un fichier avait été ajouté directement depuis l'interface GitHub entre-temps — résolu avec `git pull origin main` avant de repousser |

## Installation et lancement en local

**Prérequis** : Python 3.10 à 3.12

```bash
# 1. Cloner le dépôt
git clone https://github.com/suzy5670/datainsight-solutions-app.git
cd datainsight-solutions-app

# 2. Créer et activer l'environnement virtuel
python -m venv venv

# Sous Windows (PowerShell) :
.\venv\Scripts\Activate.ps1
# Sous macOS/Linux :
source venv/bin/activate

# 3. Installer les dépendances
python -m pip install -r streamlit/requirements.txt

# 4. Lancer l'application
python -m streamlit run streamlit/app.py