import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

st.set_page_config(page_title="DataInsight Solutions - Vols", page_icon="✈️", layout="wide")

# Chemin absolu vers ce script, pour retrouver accounts.csv peu importe
# depuis quel dossier la commande streamlit run est lancee (local ou cloud).
ACCOUNTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.csv")

# --- Initialisation de la session ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""


@st.cache_data
def load_accounts():
    return pd.read_csv(ACCOUNTS_PATH)


def authenticate(username_input, password_input):
    accounts_df = load_accounts()
    user_match = accounts_df[
        (accounts_df["name"] == username_input)
        & (accounts_df["password"] == password_input)
    ]
    return not user_match.empty


if not st.session_state["logged_in"]:
    st.title("Connexion à la plateforme DataInsight Solutions")
    st.subheader("Veuillez vous identifier pour accéder au contenu")

    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username_input
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

else:
    @st.cache_data
    def load_flights():
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
        return pd.read_csv(url)

    df = load_flights()

    with st.sidebar:
        st.write(f"Connecté en tant que : **{st.session_state['username']}**")
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()
        st.divider()

        selected_page = option_menu(
            menu_title="Navigation",
            options=["Dashboard Vols", "Galerie Photos"],
            icons=["airplane", "images"],
            default_index=0,
        )

    if selected_page == "Dashboard Vols":
        st.title("✈️ Dashboard d'Analyse des Vols")
        st.write("Bienvenue sur la plateforme sécurisée de DataInsight Solutions.")

        st.subheader("Filtres")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            annee_min, annee_max = int(df["year"].min()), int(df["year"].max())
            plage_annees = st.slider(
                "Plage d'années",
                min_value=annee_min,
                max_value=annee_max,
                value=(annee_min, annee_max),
            )
        with col_f2:
            mois_liste = ["Tous"] + df["month"].unique().tolist()
            mois_choisi = st.selectbox("Mois", mois_liste)

        df_filtre = df[(df["year"] >= plage_annees[0]) & (df["year"] <= plage_annees[1])]
        if mois_choisi != "Tous":
            df_filtre = df_filtre[df_filtre["month"] == mois_choisi]

        st.divider()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Nombre total de passagers",
                f"{df_filtre['passengers'].sum():,}".replace(",", " "),
                border=True,
            )
        with col2:
            st.metric(
                "Moyenne de passagers / mois",
                f"{df_filtre['passengers'].mean():,.0f}".replace(",", " "),
                border=True,
            )
        with col3:
            if not df_filtre.empty:
                mois_pic = df_filtre.groupby("month")["passengers"].sum().idxmax()
            else:
                mois_pic = "N/A"
            st.metric("Mois le plus chargé", mois_pic, border=True)

        st.divider()

        col_a, col_b = st.columns(2)
        with col_a:
            with st.container(border=True):
                st.subheader("Évolution du trafic par année")
                evolution = df_filtre.groupby("year")["passengers"].sum()
                st.line_chart(evolution)
        with col_b:
            with st.container(border=True):
                st.subheader("Passagers moyens par mois")
                moyenne_mois = df_filtre.groupby("month")["passengers"].mean()
                st.bar_chart(moyenne_mois)

        if st.checkbox("Afficher la heatmap année / mois"):
            with st.container(border=True):
                st.subheader("Répartition des passagers par mois et par année")
                pivot = df_filtre.pivot(index="month", columns="year", values="passengers")
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.heatmap(pivot, cmap="Blues", annot=False, ax=ax)
                st.pyplot(fig)

        with st.expander("Voir les données brutes filtrées"):
            st.dataframe(df_filtre, hide_index=True)

    elif selected_page == "Galerie Photos":
        st.title("Album photos")
        st.write("Galerie aéroports & aviation, alignée sur 3 colonnes :")

        sample_images = [
            ("https://images.unsplash.com/photo-1517400508447-f8dd518b86db?w=800&q=80", "Tableau des départs"),
            ("https://images.unsplash.com/photo-1561101904-da649fcbf03f?w=800&q=80", "Couloir du terminal"),
            ("https://images.unsplash.com/photo-1721592873149-9823d9dc6b40?w=800&q=80", "Atterrissage au crépuscule"),
            ("https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800&q=80", "Vue aérienne de l'aéroport"),
            ("https://images.unsplash.com/photo-1504150558240-0b4fd8946624?w=800&q=80", "Voyageur avec bagages"),
            ("https://images.unsplash.com/photo-1549897411-b06572cdf806?w=800&q=80", "Salle d'attente"),
            ("https://images.unsplash.com/photo-1542296332-2e4473faf563?w=800&q=80", "Avion au terminal"),
        ]
        cols = st.columns(3)
        for idx, (img_url, caption) in enumerate(sample_images):
            with cols[idx % 3]:
                st.image(img_url, caption=caption, width="stretch")
