import streamlit as st
def render_formelsammlung():
    # Haupttitel ohne Icons
    st.title("Elektrotechnik-Formelsammlung")
    st.markdown("Umfassende Übersicht aller relevanten Formeln für das Techniker-Studium, inklusive Reinform, umgestellten Formen und präzisen Quellenangaben aus Standard-Fachliteratur.")

    # Suchfeld für Formeln
    suchbegriff = st.text_input("🔍 Formel oder Stichwort suchen...", "").lower()

    formeln = [
        {
            "titel": "Ohmsches Gesetz",
            "kategorie": "Gleichstromtechnik",
            "beschreibung": "Berechnung des Zusammenhangs von elektrischer Spannung, Stromstärke und Widerstand in einem linearen elektrischen Stromkreis.",
            "reinform": "U = R \\cdot I",
            "umgestellte_formen": [
                "Widerstand: R = \\frac{U}{I}",
                "Stromstärke: I = \\frac{U}{R}"
            ],
            "quelle": "Hagmann, Gert: Grundlagen der Elektrotechnik, Kapitel 2 (Stromkreis und Ohmsches Gesetz), S. 25-30"
        },
        {
            "titel": "Elektrische Leistung",
            "kategorie": "Gleich- und Wechselstromtechnik",
            "beschreibung": "Berechnung der umgesetzten elektrischen Wirkleistung aus Spannung und Stromstärke bei Gleichstrom oder rein ohmschen Lasten.",
            "reinform": "P = U \\cdot I",
            "umgestellte_formen": [
                "Spannung: U = \\frac{P}{I}",
                "Stromstärke: I = \\frac{P}{U}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 1 – Gleichstrom und elektromagnetisches Feld, Kapitel 3 (Elektrische Energie und Leistung), S. 45-48"
        },
        {
            "titel": "Elektrische Arbeit / Energie",
            "kategorie": "Gleich- und Wechselstromtechnik",
            "beschreibung": "Berechnung der umgesetzten elektrischen Energie über einen bestimmten Zeitraum.",
            "reinform": "W = P \\cdot t",
            "umgestellte_formen": [
                "Leistung: P = \\frac{W}{t}",
                "Zeit: t = \\frac{W}{P}"
            ],
            "quelle": "Hagmann, Gert: Grundlagen der Elektrotechnik, Kapitel 3 (Elektrische Arbeit und Leistung), S. 52-54"
        },
        {
            "titel": "Spezifischer Widerstand",
            "kategorie": "Gleichstromtechnik",
            "beschreibung": "Berechnung des elektrischen Widerstands eines Leiters in Abhängigkeit von Material (spezifischer Widerstand), Länge und Querschnittsfläche.",
            "reinform": "R = \\rho \\cdot \\frac{l}{A}",
            "umgestellte_formen": [
                "Spezifischer Widerstand: \\rho = \\frac{R \\cdot A}{l}",
                "Leiterlänge: l = \\frac{R \\cdot A}{\\rho}",
                "Querschnittsfläche: A = \\frac{\\rho \\cdot l}{R}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 1, Kapitel 2 (Der elektrische Stromkreis), S. 31-35"
        },
        {
            "titel": "Temperaturabhängigkeit des Widerstandes",
            "kategorie": "Gleichstromtechnik",
            "beschreibung": "Berechnung der Widerstandsänderung eines Leiters bei Temperaturänderung (Kupfer, Aluminium etc.).",
            "reinform": "R(\\vartheta) = R_0 \\cdot (1 + \\alpha \\cdot \\Delta\\vartheta)",
            "umgestellte_formen": [
                "Widerstand bei Basistemperatur: R_0 = \\frac{R(\\vartheta)}{1 + \\alpha \\cdot \\Delta\\vartheta}",
                "Temperaturkoeffizient: \\alpha = \\frac{\\frac{R(\\vartheta)}{R_0} - 1}{\\Delta\\vartheta}"
            ],
            "quelle": "Hagmann, Gert: Grundlagen der Elektrotechnik, Kapitel 2.4 (Temperaturabhängigkeit des Widerstandes), S. 38-41"
        },
        {
            "titel": "Spannungsteiler (Unbelastet)",
            "kategorie": "Grundlagen / Schaltungstechnik",
            "beschreibung": "Proportionale Aufteilung einer Eingangsspannung auf zwei in Reihe geschaltete Widerstände.",
            "reinform": "U_2 = U_{ges} \\cdot \\frac{R_2}{R_1 + R_2}",
            "umgestellte_formen": [
                "Gesamtspannung: U_{ges} = \\frac{U_2 \\cdot (R_1 + R_2)}{R_2}"
            ],
            "quelle": "Measures, R. / Tabellenbuch Elektrotechnik, Abschnitt Schaltungstechnik und Grundstromkreise, S. 54"
        },
        {
            "titel": "Kapazitiver Blindwiderstand",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Frequenzabhängiger Widerstand (Blindwiderstand) eines Kondensators in einem Wechselstromkreis.",
            "reinform": "X_C = \\frac{1}{2 \\cdot \\pi \\cdot f \\cdot C}",
            "umgestellte_formen": [
                "Kapazität: C = \\frac{1}{2 \\cdot \\pi \\cdot f \\cdot X_C}",
                "Frequenz: f = \\frac{1}{2 \\cdot \\pi \\cdot X_C \\cdot C}"
            ],
            "quelle": "Zinke, Otto; Seidler, Hans: Widerstände, Kondensatoren, Spulen und ihre Werkstoffe, Kapitel 4 (Der Kondensator im Wechselstromkreis), S. 112-115"
        },
        {
            "titel": "Induktiver Blindwiderstand",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Frequenzabhängiger Widerstand (Blindwiderstand) einer idealen Spule in einem Wechselstromkreis.",
            "reinform": "X_L = 2 \\cdot \\pi \\cdot f \\cdot L",
            "umgestellte_formen": [
                "Induktivität: L = \\frac{X_L}{2 \\cdot \\pi \\cdot f}",
                "Frequenz: f = \\frac{X_L}{2 \\cdot \\pi \\cdot L}"
            ],
            "quelle": "Hagmann, Gert: Elektrotechnik für Dummies / Grundlagen der Wechselstromtechnik, Kapitel 8 (Spule im Wechselstromkreis), S. 140-143"
        },
        {
            "titel": "Impedanz (Scheinwiderstand) im RLC-Reihenkreis",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Gesamtwiderstand einer Reihenschaltung aus Ohmschem Widerstand, Induktivität und Kapazität im Wechselstromkreis.",
            "reinform": "Z = \\sqrt{R^2 + (X_L - X_C)^2}",
            "umgestellte_formen": [
                "Ohmscher Widerstand: R = \\sqrt{Z^2 - (X_L - X_C)^2}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 2 – Wechselströme und Netze, Kapitel 5 (Komplexe Rechnung und Schwingungskreise), S. 88-92"
        },
        {
            "titel": "Wirkleistung im Wechselstromkreis",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Tatsächlich umgesetzte Leistung unter Berücksichtigung der Phasenverschiebung zwischen Spannung und Strom.",
            "reinform": "P = U \\cdot I \\cdot \\cos(\\varphi)",
            "umgestellte_formen": [
                "Spannung: U = \\frac{P}{I \\cdot \\cos(\\varphi)}",
                "Stromstärke: I = \\frac{P}{U \\cdot \\cos(\\varphi)}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 2 – Wechselströme und Netze, Kapitel 3 (Leistung im Wechselstromkreis), S. 60-65"
        },
        {
            "titel": "Blindleistung im Wechselstromkreis",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Zwischen Quelle und Verbraucher hin- und herpendelnde Leistung an Blindelementen (Spulen und Kondensatoren).",
            "reinform": "Q = U \\cdot I \\cdot \\sin(\\varphi)",
            "umgestellte_formen": [
                "Stromstärke: I = \\frac{Q}{U \\cdot \\sin(\\varphi)}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 2 – Wechselströme und Netze, Kapitel 3 (Leistung im Wechselstromkreis), S. 66-68"
        },
        {
            "titel": "Scheinleistung im Wechselstromkreis",
            "kategorie": "Wechselstromtechnik",
            "beschreibung": "Geometrische Summe aus Wirk- und Blindleistung, maßgeblich für die Dimensionierung von Leitungen und Transformatoren.",
            "reinform": "S = U \\cdot I",
            "umgestellte_formen": [
                "Aus Leistungssatz: S = \\sqrt{P^2 + Q^2}",
                "Spannung: U = \\frac{S}{I}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 2 – Wechselströme und Netze, Kapitel 3 (Leistung im Wechselstromkreis), S. 69-72"
        },
        {
            "titel": "Transformator-Übersetzungsverhältnis",
            "kategorie": "Antriebs- und Energietechnik",
            "beschreibung": "Verhältnis der Spannungen, Windungszahlen und Ströme an einem idealen Transformator.",
            "reinform": "\\frac{U_1}{U_2} = \\frac{N_1}{N_2} = \\frac{I_2}{I_1}",
            "umgestellte_formen": [
                "Sekundärspannung: U_2 = U_1 \\cdot \\frac{N_2}{N_1}",
                "Sekundärstrom: I_2 = I_1 \\cdot \\frac{N_1}{N_2}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 4 (Der Transformator), S. 105-110"
        },
        {
            "titel": "Synchrone Drehzahl (Drehstrommotor)",
            "kategorie": "Antriebstechnik",
            "beschreibung": "Berechnung der Drehfeld-Drehzahl eines Drehstrommotors in Abhängigkeit von Netzfrequenz und Polpaarzahl.",
            "reinform": "n_s = \\frac{f \\cdot 60}{p}",
            "umgestellte_formen": [
                "Frequenz: f = \\frac{n_s \\cdot p}{60}",
                "Polpaarzahl: p = \\frac{f \\cdot 60}{n_s}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 6 (Asynchronmaschine), S. 150-154"
        }
    ]

    gefilterte_formeln = [
        f for f in formeln 
        if suchbegriff in f["titel"].lower() or suchbegriff in f["beschreibung"].lower() or suchbegriff in f["kategorie"].lower()
    ]

    st.markdown("---")

    if not gefilterte_formeln:
        st.warning("Keine passenden Formeln gefunden.")
    
    for f in gefilterte_formeln:
        with st.container():
            # Titel ohne "Name der Formel:" und ohne Symbole
            st.markdown(f"### {f['titel']}")
            
            # Kategorie im schicken Lilaton via HTML-Badge
            st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>{f['kategorie']}</span>", unsafe_allow_html=True)
            
            st.markdown(f"**Anwendungsbereich / Erläuterung:** {f['beschreibung']}")
            
            st.markdown("**Reinform:**")
            st.latex(f["reinform"])
            
            st.markdown("**Umgestellte Formen:**")
            for form in f["umgestellte_formen"]:
                bezeichnung, mathtext = form.split(": ")
                st.markdown(f"- *{bezeichnung}:*")
                st.latex(mathtext)
                
            st.markdown(f"**Quelle:** {f['quelle']}")
            st.markdown("---")
# 1. Grund-Einstellungen der Seite (Muss immer ganz oben stehen)
st.set_page_config(page_title="Dungeons&Dioden", layout="wide")
# --- PASSWORTSCHUTZ MIT GEDÄCHTNIS ---
# 1. Prüfen, ob der Nutzer schon angemeldet ist
if "angemeldet" not in st.session_state:
    st.session_state.angemeldet = False

# 2. Wenn nicht angemeldet, zeige das Login-Fenster
if not st.session_state.angemeldet:
    st.title("🔒 Login erforderlich")
    passwort = st.text_input("Bitte Passwort eingeben:", type="password")
    
    if passwort == "Techniker2025":
        st.session_state.angemeldet = True
        st.rerun()  # Lädt die Seite blitzschnell neu - das Login-Feld verschwindet!
    elif passwort != "":
        st.error("Zugriff verweigert. Falsches Passwort.")
        
    st.stop() # Stoppt den Aufbau der restlichen Website
# 2. Die Navigation in der Seitenleiste (Sidebar) erstellen
# 1. Das Menü-Gedächtnis initialisieren
# 1. Das Menü-Gedächtnis initialisieren
if "menue" not in st.session_state:
    st.session_state.menue = "Startseite"

# 2. Die Navigation in der Sidebar (ohne direkten Key-Konflikt)
st.sidebar.title("Navigation")
menue_optionen = ["Startseite", "Grundlagen", "Verfahren", "Mathematik", "Lexikon & Abkürzungen", "Formelsammlung", "Dokumente & Uploads"]

# Wir holen den aktuellen Index aus dem Session State
aktueller_index = menue_optionen.index(st.session_state.menue) if st.session_state.menue in menue_optionen else 0

menue = st.sidebar.radio(
    "Wähle einen Bereich:",
    menue_optionen,
    index=aktueller_index
)

# Das aktuelle Menü im Session State speichern
st.session_state.menue = menue

# 3. Inhalte anzeigen, je nachdem was im Menü geklickt wurde
# 3. Inhalte anzeigen, je nachdem was im Menü geklickt wurde
if menue == "Startseite":
    st.title("Willkommen auf deiner persönlichen Lern-Zentrale für die Werner-von-Siemens-Schule.")
    
    st.markdown("### 🔍 Globale Suche")
    suchbegriff = st.text_input("Was suchst du? (z. B. Widerstand, Gauß, Zweipol, Diode):").lower()

    # Unser Suchindex: Hier hinterlegen wir alle Themen der website
    suchindex = [
        {"titel": "Knotenpotentialverfahren (Millman)", "ort": "Verfahren", "text": "Analyseverfahren für Netzwerke mit Leitwerten, Knotenpotentialen und äquivalenten Stromquellen."},
        {"titel": "Zweipoltheorie / Ersatzspannungsquelle", "ort": "Verfahren", "text": "Reduktion komplexer Netze auf eine reale Spannungsquelle mit Innenwiderstand."},
        {"titel": "Überlagerungssatz nach Helmholtz", "ort": "Verfahren", "text": "Netzwerke mit mehreren Spannungs- oder Stromquellen durch Teilströme berechnen."},
        {"titel": "Kreisstrom- / Maschenstromverfahren", "ort": "Verfahren", "text": "Komplexe Schaltungen mit fiktiven Kreisströmen in unabhängigen Maschen berechnen."},
        {"titel": "Kirchhoffsche Gesetze", "ort": "Verfahren", "text": "Knotenpunkt-Regel (Summe aller Ströme = 0) und Maschen-Regel (Summe aller Spannungen = 0)."},
        {"titel": "Das Gauß-Verfahren (3x3 Matrix)", "ort": "Mathematik", "text": "Lineare Gleichungssysteme schrittweise durch Zeilenumformung und Rückwärtseinsetzen lösen."},
        {"titel": "Cramersche Regel (Determinanten)", "ort": "Mathematik", "text": "2x2 Gleichungssysteme und Determinanten direkt über Kreuz ausrechnen."},
        {"titel": "Komplexe Wechselstromrechnung", "ort": "Mathematik", "text": "Umrechnung zwischen kartesischer Form (R + jX) und Polarform (Z und Phasenwinkel phi)."},
        {"titel": "Trigonometrie / Leistungsdreieck", "ort": "Mathematik", "text": "Wirk-, Blindleistung und Scheinleistung über Pythagoras und den Kosinus (cos phi) verknüpfen."},
        {"titel": "PQ-Formel", "ort": "Mathematik", "text": "Quadratische Gleichungen lösen (z.B. für Resonanzfrequenzen und Grenzfrequenzen)."},
        {"titel": "Ohmsches Gesetz", "ort": "Grundlagen", "text": "Zusammenhang zwischen Spannung, Strom und Widerstand: U = R * I."},
        {"titel": "Elektrischer Leitwert", "ort": "Grundlagen", "text": "Kehrwert des Widerstands: G = 1 / R in Siemens (S), wichtig für das Knotenpotentialverfahren."},
        {"titel": "Spannungsteiler (belastet & unbelastet)", "ort": "Grundlagen", "text": "Spannungsaufteilung in Reihenschaltungen, mit und ohne Querlast."},
        {"titel": "Blindwiderstand (kapazitiv / induktiv)", "ort": "Grundlagen", "text": "Wechselstromwiderstände von Spulen (XL) und Kondensatoren (XC)."},
        {"titel": "Elektrische Leistung und Arbeit", "ort": "Grundlagen", "text": "Leistung P = U * I und Arbeit als umgesetzte Energie über die Zeit."},
        {"titel": "Spannungsfall / Leitungswiderstand", "ort": "Grundlagen", "text": "Berechnung des Spannungsverlusts auf langen Kabelstrecken."},
        {"titel": "Bipolartransistor (NPN / PNP)", "ort": "Grundlagen", "text": "Aufbau, Anschlüsse (Basis, Emitter, Kollektor), Schalterfunktion und Stromverstärkung beta."},
        {"titel": "Transistor als Schalter & Übersteuerung", "ort": "Grundlagen", "text": "Sättigungsbereich, Sperrbereich und Dimensionierung des Basisvorwiderstands RV."},
        {"titel": "Darlington-Schaltung", "ort": "Grundlagen", "text": "Zwei Transistoren in Reihe für extreme Stromverstärkungen bei minimalem Steuerstrom."}
    ]

    # Such-Logik: Direktes Springen per Button
    # Such-Logik: Direktes Springen per Button
    if suchbegriff:
        ergebnisse = [eintrag for eintrag in suchindex if suchbegriff in eintrag["titel"].lower() or suchbegriff in eintrag["text"].lower()]
        
        if ergebnisse:
            st.success(f"**{len(ergebnisse)} Treffer gefunden:**")
            for i, e in enumerate(ergebnisse):
                # Wenn der Button geklickt wird, setzen wir das Menü und laden neu
                if st.button(f"🚀 Direkt zu: {e['titel']} (in '{e['ort']}')", key=f"such_btn_{i}"):
                    st.session_state.menue = e['ort']
                    st.rerun()
                st.caption(f"📝 {e['text']}")
                st.divider()
        else:
            st.warning("Keine direkten Treffer gefunden. Versuch es mit einem anderen Fachbegriff.")

elif menue == "Grundlagen":
    st.title("Grundlagen der Elektrotechnik")
    st.write("Hier findest du alle Basis-Berechnungen und Regeln. Klappe das jeweilige Thema auf, um die Formel zu sehen und Werte zu berechnen.")
    
    import math

    # --- THEORIE & REGELN ---
    st.subheader("Theorie & Sicherheitsregeln")
    
    with st.expander("Wirkungen des elektrischen Stroms"):
        st.write("Elektrischer Strom kann man nicht sehen, aber an seinen Wirkungen erkennen:")
        st.markdown("- **Wärmewirkung:** Bügeleisen, Schmelzsicherungen, Heizlüfter.\n- **Lichtwirkung:** Glühlampen, LEDs, Lichtbögen beim Schweißen.\n- **Magnetische Wirkung:** Elektromotoren, Relais, Transformatoren.\n- **Chemische Wirkung:** Galvanisieren, Akkumulatoren laden, Elektrolyse.\n- **Physiologische Wirkung:** Muskelverkrampfungen oder Herzkammerflimmern beim Menschen (Gefahr!).")

    with st.expander("Die fünf Sicherheitsregeln"):
        st.write("Vor Beginn der Arbeiten an elektrischen Anlagen (Spannungsfreiheit herstellen):")
        st.markdown("1. **Freischalten:** Anlage allpolig von der Spannung trennen.\n2. **Gegen Wiedereinschalten sichern:** Schalter blockieren, Warnschild anbringen.\n3. **Spannungsfreiheit feststellen:** Zweipoligen Spannungsprüfer verwenden.\n4. **Erden und Kurzschließen:** Ab 1000 V (1 kV) zwingend erforderlich.\n5. **Benachbarte, unter Spannung stehende Teile abdecken oder abschranken:** Berührungsschutz herstellen.")

    # --- INTERAKTIVE RECHNER ---
    st.subheader("Interaktive Rechner & Formeln")

    with st.expander("Ohmsches Gesetz (U, R, I)"):
        st.write("Beschreibt den grundlegenden Zusammenhang zwischen Spannung, Strom und Widerstand.")
        st.latex(r"U = R \cdot I \quad ; \quad I = \frac{U}{R} \quad ; \quad R = \frac{U}{I}")
        ziel_ohm = st.radio("Was möchtest du berechnen?", ["Spannung U (V)", "Strom I (A)", "Widerstand R (Ω)"], horizontal=True)
        if ziel_ohm == "Spannung U (V)":
            ohm_i = st.number_input("Strom I (in A)", value=5.0, key="ohm_i_u")
            ohm_r = st.number_input("Widerstand R (in Ω)", value=10.0, key="ohm_r_u")
            st.success(f"Spannung U = **{ohm_i * ohm_r:.2f} V**")
        elif ziel_ohm == "Strom I (A)":
            ohm_u = st.number_input("Spannung U (in V)", value=230.0, key="ohm_u_i")
            ohm_r = st.number_input("Widerstand R (in Ω)", value=10.0, key="ohm_r_i")
            if ohm_r != 0: st.success(f"Strom I = **{ohm_u / ohm_r:.2f} A**")
            else: st.error("Widerstand darf nicht 0 Ω sein.")
        elif ziel_ohm == "Widerstand R (Ω)":
            ohm_u = st.number_input("Spannung U (in V)", value=230.0, key="ohm_u_r")
            ohm_i = st.number_input("Strom I (in A)", value=16.0, key="ohm_i_r")
            if ohm_i != 0: st.success(f"Widerstand R = **{ohm_u / ohm_i:.2f} Ω**")
            else: st.error("Strom darf nicht 0 A sein.")

    with st.expander("Elektrischer Leitwert (G)"):
        st.write("Gibt an, wie gut ein Bauteil den elektrischen Strom leitet. Er ist der Kehrwert des Widerstands.")
        st.latex(r"G = \frac{1}{R}")
        g_r = st.number_input("Widerstand R (in Ω)", value=50.0, key="g_r")
        if g_r != 0: st.success(f"Leitwert G = **{1/g_r:.4f} S (Siemens)**")
        else: st.error("Widerstand darf nicht 0 Ω sein.")

    with st.expander("Leitungswiderstand / Spezifischer Leitwert"):
        st.write("Berechnet den Widerstand eines Kabels anhand seiner Länge, seines Querschnitts und des Materials (z. B. Kupfer).")
        st.latex(r"R = \frac{l}{\kappa \cdot A}")
        lw_l = st.number_input("Länge l (in m)", value=50.0, key="lw_l")
        lw_a = st.number_input("Querschnitt A (in mm²)", value=1.5, key="lw_a")
        lw_kappa = st.number_input("Spezifische Leitfähigkeit κ (Kupfer = 56, Alu = 36)", value=56.0, key="lw_kappa")
        if lw_kappa != 0 and lw_a != 0:
            st.success(f"Leitungswiderstand R = **{lw_l / (lw_kappa * lw_a):.4f} Ω**")
        else: st.error("Leitfähigkeit und Querschnitt dürfen nicht 0 sein.")

    with st.expander("Reihenschaltung von Widerständen"):
        st.write("In einer Reihenschaltung addieren sich die Einzelwiderstände zum Gesamtwiderstand. Der Strom ist überall gleich.")
        st.latex(r"R_{ges} = R_1 + R_2 + R_3 + \dots")
        rs_r1 = st.number_input("Widerstand R1 (in Ω)", value=10.0, key="rs_r1")
        rs_r2 = st.number_input("Widerstand R2 (in Ω)", value=20.0, key="rs_r2")
        rs_r3 = st.number_input("Widerstand R3 (in Ω) (0 wenn nicht vorhanden)", value=0.0, key="rs_r3")
        st.success(f"Gesamtwiderstand R_ges = **{rs_r1 + rs_r2 + rs_r3:.2f} Ω**")

    with st.expander("Parallelschaltung von Widerständen"):
        st.write("In einer Parallelschaltung ist der Gesamtwiderstand stets kleiner als der kleinste Einzelwiderstand. Die Spannung ist überall gleich.")
        st.latex(r"\frac{1}{R_{ges}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots")
        ps_r1 = st.number_input("Widerstand R1 (in Ω)", value=10.0, min_value=0.001, key="ps_r1")
        ps_r2 = st.number_input("Widerstand R2 (in Ω)", value=10.0, min_value=0.001, key="ps_r2")
        ps_r3 = st.number_input("Widerstand R3 (in Ω) (Optional, Feld leer lassen für 2 Widerstände)", value=None, key="ps_r3")
        
        leitwert_ges = (1/ps_r1) + (1/ps_r2)
        if ps_r3 is not None and ps_r3 > 0:
            leitwert_ges += (1/ps_r3)
        st.success(f"Gesamtwiderstand R_ges = **{1/leitwert_ges:.2f} Ω**")

    with st.expander("Unbelasteter Spannungsteiler"):
        st.write("Berechnet, wie sich eine Spannung auf zwei in Reihe geschaltete Widerstände aufteilt (ohne weiteren Verbraucher).")
        st.latex(r"U_1 = U_{ges} \cdot \frac{R_1}{R_1 + R_2} \quad ; \quad U_2 = U_{ges} \cdot \frac{R_2}{R_1 + R_2}")
        ut_uges = st.number_input("Gesamtspannung U_ges (in V)", value=24.0, key="ut_uges")
        ut_r1 = st.number_input("Widerstand R1 (in Ω)", value=100.0, key="ut_r1")
        ut_r2 = st.number_input("Widerstand R2 (in Ω)", value=200.0, key="ut_r2")
        r_ges = ut_r1 + ut_r2
        if r_ges != 0:
            st.success(f"Teilspannung U1 = **{ut_uges * (ut_r1 / r_ges):.2f} V**  |  Teilspannung U2 = **{ut_uges * (ut_r2 / r_ges):.2f} V**")

    with st.expander("Belasteter Spannungsteiler"):
        st.write("Ein Spannungsteiler, an dessen zweitem Widerstand (R2) ein weiterer Verbraucher (Lastwiderstand RL) parallel angeschlossen ist. Die Spannung bricht dadurch ein.")
        st.latex(r"U_{L} = U_{ges} \cdot \frac{R_2 || R_L}{R_1 + (R_2 || R_L)}")
        bt_uges = st.number_input("Gesamtspannung U_ges (in V)", value=24.0, key="bt_uges")
        bt_r1 = st.number_input("Vorwiderstand R1 (in Ω)", value=100.0, key="bt_r1")
        bt_r2 = st.number_input("Querwiderstand R2 (in Ω)", value=200.0, key="bt_r2")
        bt_rl = st.number_input("Lastwiderstand RL (in Ω)", value=50.0, key="bt_rl")
        
        if (bt_r2 + bt_rl) != 0:
            ersatz_parallel = (bt_r2 * bt_rl) / (bt_r2 + bt_rl)
            if (bt_r1 + ersatz_parallel) != 0:
                ul = bt_uges * (ersatz_parallel / (bt_r1 + ersatz_parallel))
                st.success(f"Spannung an der Last U_L = **{ul:.2f} V**")
        else:
            st.error("Widerstände R2 und RL dürfen nicht gleichzeitig 0 sein.")

    with st.expander("Vorwiderstand berechnen (z.B. für LEDs)"):
        st.write("Berechnet den nötigen Widerstand, um an einem Bauteil eine Überspannung zu " + "verhindern (die überschüssige Spannung muss am Vorwiderstand abfallen).")
        st.latex(r"R_V = \frac{U_{ges} - U_{Bauteil}}{I_{Bauteil}}")
        vw_uges = st.number_input("Gesamtspannung / Betriebsspannung (in V)", value=12.0, key="vw_uges")
        vw_ub = st.number_input("Spannung des Bauteils (in V, z.B. LED = 2V)", value=2.0, key="vw_ub")
        vw_ib = st.number_input("Strom des Bauteils (in A, z.B. 20mA = 0.02A)", value=0.02, key="vw_ib")
        if vw_ib != 0:
            st.success(f"Erforderlicher Vorwiderstand R_V = **{(vw_uges - vw_ub) / vw_ib:.2f} Ω**")

    with st.expander("Spannungsfall berechnen (Gleichstrom)"):
        st.write("Berechnet den Spannungsverlust auf einer Leitung (Hin- und Rückleiter = 2 * Länge).")
        st.latex(r"\Delta U = \frac{2 \cdot l \cdot I}{\kappa \cdot A}")
        sf_l = st.number_input("Einfache Leitungslänge l (in m)", value=25.0, key="sf_l")
        sf_i = st.number_input("Stromstärke I (in A)", value=16.0, key="sf_i")
        sf_a = st.number_input("Querschnitt A (in mm²)", value=1.5, key="sf_a")
        sf_kappa = st.number_input("Leitfähigkeit κ (Kupfer = 56)", value=56.0, key="sf_kappa")
        if sf_kappa != 0 and sf_a != 0:
            delta_u = (2 * sf_l * sf_i) / (sf_kappa * sf_a)
            st.success(f"Spannungsfall ΔU = **{delta_u:.2f} V**")

    with st.expander("Elektrische Leistung (P)"):
        st.write("Gibt an, wie viel elektrische Energie pro Zeitspanne umgesetzt wird.")
        st.latex(r"P = U \cdot I \quad ; \quad P = I^2 \cdot R \quad ; \quad P = \frac{U^2}{R}")
        leistung_u = st.number_input("Spannung U (in V)", value=230.0, key="p_u")
        leistung_i = st.number_input("Strom I (in A)", value=16.0, key="p_i")
        st.success(f"Leistung P = **{leistung_u * leistung_i:.2f} W (Watt)**")

    with st.expander("Elektrische Arbeit / Energie (W)"):
        st.write("Die elektrische Arbeit ist die Leistung, die über eine bestimmte Zeitdauer bezogen wird.")
        st.latex(r"W = P \cdot t")
        w_p = st.number_input("Leistung P (in kW)", value=2.5, key="w_p")
        w_t = st.number_input("Zeit t (in h)", value=4.0, key="w_t")
        st.success(f"Arbeit W = **{w_p * w_t:.2f} kWh (Kilowattstunden)**")

    with st.expander("Wirkungsgrad (η)"):
        st.write("Beschreibt das Verhältnis von abgegebener Leistung zu zugeführter Leistung (immer kleiner als 1 bzw. 100%).")
        st.latex(r"\eta = \frac{P_{ab}}{P_{zu}}")
        eta_pzu = st.number_input("Zugeführte Leistung P_zu (in W)", value=1000.0, key="eta_pzu")
        eta_pab = st.number_input("Abgegebene Leistung P_ab (in W)", value=850.0, key="eta_pab")
        if eta_pzu != 0:
            wirkungsgrad = eta_pab / eta_pzu
            st.success(f"Wirkungsgrad η = **{wirkungsgrad:.4f} (entspricht {wirkungsgrad * 100:.2f} %)**")

    with st.expander("Induktiver Blindwiderstand (XL)"):
        st.write("Gibt den frequenzabhängigen Widerstand einer Spule im Wechselstromkreis an.")
        st.latex(r"X_L = 2 \cdot \pi \cdot f \cdot L")
        xl_f = st.number_input("Frequenz f (in Hz)", min_value=0.1, value=50.0, key="xl_f")
        xl_l = st.number_input("Induktivität L (in mH)", min_value=0.01, value=100.0, key="xl_l")
        xl = 2 * math.pi * xl_f * (xl_l * 1e-3)
        st.success(f"Induktiver Blindwiderstand XL = **{xl:.2f} Ω**")

    with st.expander("Kapazitiver Blindwiderstand (XC)"):
        st.write("Gibt den frequenzabhängigen Widerstand eines Kondensators im Wechselstromkreis an.")
        st.latex(r"X_C = \frac{1}{2 \cdot \pi \cdot f \cdot C}")
        xc_f = st.number_input("Frequenz f (in Hz)", min_value=0.1, value=50.0, key="xc_f")
        xc_c = st.number_input("Kapazität C (in µF)", min_value=0.01, value=10.0, key="xc_c")
        xc = 1 / (2 * math.pi * xc_f * (xc_c * 1e-6))
        st.success(f"Kapazitiver Blindwiderstand XC = **{xc:.2f} Ω**")

    st.divider()
    st.caption("Quellen: [^1] Europa-Lehrmittel, Fachkunde Elektrotechnik | [^2] Formelsammlung Elektrotechnik, Werner-von-Siemens-Schule.")

elif menue == "Verfahren":
    st.title("Analyseverfahren der Elektrotechnik")
    st.write("Hier findest du alle wichtigen Verfahren zur Berechnung komplexer Netzwerke. Zu jedem Verfahren gibt es eine Erklärung, den Lösungsweg und einen Praxis-Rechner.")

    # --- 1. KIRCHHOFFSCHE GESETZE ---
    st.header("1. Kirchhoffsche Gesetze (Knoten- und Maschensatz)")
    st.info("Wann anwenden? Das absolute Basiswerkzeug für jedes Netzwerk. Wird genutzt, um Ströme an Verzweigungen oder Spannungen in geschlossenen Ringen zu berechnen.")

    with st.expander("Schritt-für-Schritt & Interaktiver Rechner"):
        st.markdown("""
        **1. Knotenpunkt-Regel (Knotensatz)**
        In jedem Stromverzweigungspunkt ist die Summe aller Ströme gleich Null[cite: 15].
        *Es gilt:* Die Summe der zufließenden Ströme ist stets gleich der Summe der abfließenden Ströme[cite: 15].
        """)
        st.latex(r"\sum_{k=1}^{n} I_k = 0 \quad \text{bzw.} \quad I_{zu} = I_{ab}")
        
        st.markdown("""
        **2. Maschen-Regel (Maschensatz)**
        In jedem geschlossenen Stromkreis (Masche) ist die Summe der Spannungen unter Beachtung der Vorzeichen stets gleich Null[cite: 15]. Die Umlaufrichtung in der Masche ist dabei frei wählbar[cite: 15].
        """)
        st.latex(r"\sum_{k=1}^{n} U_k = 0")
        
        st.divider()
        st.write("**Rechner: Knotenpunkt mit 3 Strömen**")
        k_i1 = st.number_input("Zufließender Strom I1 (in A)", value=5.0)
        k_i2 = st.number_input("Zufließender Strom I2 (in A)", value=2.5)
        st.success(f"Der abfließende Strom I3 muss betragen: **{k_i1 + k_i2:.2f} A**")

    # --- 2. KNOTENPOTENTIALVERFAHREN (MILLMAN) ---
    st.header("2. Knotenpotentialverfahren (Satz von Millman)")
    st.info("Wann anwenden? Wenn die Schaltung aus mehreren parallelen Strängen besteht, die alle oben und unten an denselben durchgehenden Knotenpunkten zusammenlaufen.")

    with st.expander("Schritt-für-Schritt & Interaktiver Rechner"):
        st.markdown("""
        **Das Prinzip:**
        Das Verfahren fasst Schaltungen mit nur zwei Hauptknoten in einer direkten Formel zusammen[cite: 12]. Man wandelt jeden Zweig gedanklich in eine Stromquelle um ($I = U / R$) und teilt die Summe der Ströme durch den Gesamtleitwert ($G = 1 / R$) der Parallelschaltung[cite: 12].
        """)
        st.latex(r"U_{q} = \frac{\sum (U_n \cdot G_n)}{\sum G_n} = \frac{\frac{U_1}{R_1} + \frac{U_2}{R_2} + \dots}{\frac{1}{R_1} + \frac{1}{R_2} + \dots}")
        
        st.divider()
        st.write("**Rechner: 2 parallele aktive Zweige & 1 passiver Zweig**")
        m_u1 = st.number_input("Spannung U1 (Zweig 1, in V)", value=4.5)
        m_r1 = st.number_input("Widerstand R1 (Zweig 1, in Ω)", value=100.0)
        m_u2 = st.number_input("Spannung U2 (Zweig 2, in V)", value=3.0)
        m_r2 = st.number_input("Widerstand R2 (Zweig 2, in Ω)", value=100.0)
        m_r3 = st.number_input("Widerstand R3 (Zweig 3 ohne Quelle, in Ω)", value=50.0)
        
        if m_r1 != 0 and m_r2 != 0 and m_r3 != 0:
            zaehler = (m_u1 / m_r1) + (m_u2 / m_r2)
            nenner = (1 / m_r1) + (1 / m_r2) + (1 / m_r3)
            st.success(f"Die Spannung zwischen den Hauptknoten (Ersatzspannung U_q) beträgt: **{zaehler / nenner:.3f} V**")
            st.caption("Vergleiche ET_Arbeitsmappe_1[cite: 12].")

    # --- 3. ZWEIPOLTHEORIE / ERSATZSPANNUNGSQUELLE ---
    st.header("3. Zweipoltheorie (Ersatzspannungsquelle / Thévenin)")
    st.info("Wann anwenden? Wenn ein nicht-lineares Bauteil (z.B. Diode, Transistor) vorhanden ist oder man einen Lastwiderstand variieren möchte. Man trennt das Bauteil ab und vereinfacht den Rest der Schaltung[cite: 12].")

    with st.expander("Schritt-für-Schritt & Interaktiver Rechner"):
        st.markdown("""
        **Schritt 1: Den 'Störenfried' isolieren (Auftrennen)**
        Das Bauteil (z.B. Diode oder Lastwiderstand) an den Klemmen A und B heraustrennen[cite: 12]. Der aktive Zweipol wird nun im Leerlauf betrieben[cite: 15].
        
        **Schritt 2: Ersatzspannungsquelle ($U_0$ bzw. $U_q$) berechnen**
        Die Leerlaufspannung $U_{AB0}$ an den Klemmen berechnen. Das ist unsere neue Quellenspannung $U_0$[cite: 15].
        
        **Schritt 3: Innenwiderstand ($R_i$) berechnen**
        Alle Spannungsquellen im Netzwerk kurzschließen ($U = 0$) und den Ersatzwiderstand von den Klemmen A und B aus berechnen[cite: 15]. Dieser Wert ist der Innenwiderstand $R_i$[cite: 15].
        
        **Schritt 4: Bauteil wieder anschließen (Maschengleichung)**
        Die komplexe Schaltung ist nun zu einer Reihenschaltung aus $U_0$, $R_i$ und dem Lastwiderstand $R_L$ (oder der Diode) geschrumpft[cite: 12, 15].
        """)
        st.latex(r"I_L = \frac{U_0}{R_i + R_L} \quad ; \quad U_L = I_L \cdot R_L")
        
        st.divider()
        st.write("**Rechner: Aktiver Zweipol unter Last**")
        z_u0 = st.number_input("Ermittelte Leerlaufspannung U_0 (in V)", value=12.0)
        z_ri = st.number_input("Ermittelter Innenwiderstand R_i (in Ω)", value=36.0)
        z_rl = st.number_input("Angeschlossener Lastwiderstand R_L (in Ω)", value=100.0)
        
        if (z_ri + z_rl) != 0:
            z_il = z_u0 / (z_ri + z_rl)
            st.success(f"Laststrom $I_L$ = **{z_il * 1000:.1f} mA** | Spannung an der Last $U_L$ = **{z_il * z_rl:.2f} V**")

    # --- 4. ÜBERLAGERUNGSSATZ NACH HELMHOLTZ ---
    st.header("4. Überlagerungssatz nach Helmholtz (Superposition)")
    st.info("Wann anwenden? Bei Netzwerken mit mehreren unabhängigen Spannungs- oder Stromquellen[cite: 15].")

    with st.expander("Schritt-für-Schritt & Interaktiver Rechner"):
        st.markdown("""
        **Das Prinzip:**
        Der Strom in jedem Zweig setzt sich aus fiktiven Teilströmen zusammen, wobei jede Quelle für sich allein einen Teilstrom erzeugt[cite: 15].
        
        **Schritt 1: Alle Quellen bis auf eine 'ausschalten'**
        *   **Spannungsquellen** werden kurzgeschlossen ($U = 0\,V$)[cite: 15].
        *   **Stromquellen** werden durchtrennt (Leerlauf, $I = 0\,A$)[cite: 13].
        
        **Schritt 2: Fiktive Teilströme berechnen**
        Die Schaltung mit nur noch einer aktiven Quelle berechnen (z.B. $I_1', I_2'$). Dies für jede Quelle wiederholen[cite: 15].
        
        **Schritt 3: Überlagerung (Addition)**
        Die berechneten Teilströme richtungsrichtig addieren. Ströme in die gleiche Richtung bekommen ein Plus, Ströme in die entgegengesetzte Richtung ein Minus[cite: 15].
        """)
        st.latex(r"I_{ges} = I' + I'' + I'''")
        
        st.divider()
        st.write("**Rechner: Überlagerung von zwei Quellen**")
        h_i1 = st.number_input("Teilstrom aus Quelle 1 (in A, z.B. 1.5)", value=1.5)
        h_i2 = st.number_input("Teilstrom aus Quelle 2 (in A, negativ wenn Gegenrichtung, z.B. -1.0)", value=-1.0)
        st.success(f"Der resultierende Gesamtstrom beträgt: **{h_i1 + h_i2:.2f} A**")

    # --- 5. KREISSTROMVERFAHREN ---
    st.header("5. Kreisstrom-Verfahren (Maschenstrom-Verfahren)")
    st.info("Wann anwenden? Bei komplexen Schaltungen mit vielen Knoten und Maschen, um die Anzahl der benötigten Gleichungen drastisch zu reduzieren[cite: 15].")

    with st.expander("Schritt-für-Schritt Erklärung"):
        st.markdown("""
        **Schritt 1: Unabhängige Maschen festlegen**
        Sämtliche Knotenpunkte werden über den sogenannten 'vollständigen Baum' miteinander verbunden (ohne dass sich geschlossene Maschen bilden)[cite: 15]. Die verbleibenden Verbindungen bilden die unabhängigen Zweige[cite: 15]. Nie zweimal über einen unabhängigen Zweig gehen[cite: 15]!
        
        **Schritt 2: Kreisströme einzeichnen**
        Jeder Masche wird ein fiktiver Kreisstrom (z.B. $I_a, I_b$) zugeordnet[cite: 15]. Die Richtung (im Uhrzeigersinn) wird als positiv definiert[cite: 15].
        
        **Schritt 3: Maschengleichungen aufstellen**
        Die Spannungsabfälle werden als Produkt aus Widerstand und Kreisstrom angegeben[cite: 15]. Fließen zwei Kreisströme durch denselben Widerstand (gemeinsamer Zweig), müssen beide berücksichtigt werden (z.B. $R_2 \cdot (I_a - I_b)$)[cite: 15].
        
        **Schritt 4: Gleichungssystem lösen & Überlagern**
        Das System (z.B. mit dem Gauß-Verfahren) nach den Kreisströmen auflösen[cite: 15]. Liegt ein Bauteil in einem Zweig mit mehreren Kreisströmen, wird der tatsächliche Zweigstrom durch Überlagerung (z.B. $I_2 = I_a - I_b$) ermittelt[cite: 15].
        """)
        st.caption("Ausführliche Beispiele für Matrizen (Gauß) findest du im Bereich 'Mathematik'.")
        
    st.divider()
    st.caption("Quellen: [^1] Aufgabensammlung Grundlagen ET[cite: 11] | [^2] Arbeitsmappen Diode & Schaltungsanalyse[cite: 12, 13, 14] | [^3] Kirchhoff, Helmholtz & Maschenstromverfahren[cite: 15].")

elif menue == "Mathematik":
    st.title("Mathematik für Elektrotechniker")
    st.write("Alle wichtigen mathematischen Lösungswege. Zu jedem Thema gibt es eine fiktive Beispielaufgabe aus der Elektrotechnik.")

    import math

    # --- 1. GAUß-VERFAHREN (3x3 MATRIX) ---
    st.header("1. Das Gauß-Verfahren (3x3 Matrix)")
    st.info("Wird z.B. beim Knotenpotentialverfahren verwendet, wenn man 3 unbekannte Knotenspannungen berechnen muss.")

    with st.expander("Fiktive Aufgabe & Schritt-für-Schritt Lösung"):
        st.markdown(r"""
        **Fiktive Aufgabe:** 
        Wir haben ein Netzwerk analysiert und folgendes Gleichungssystem für drei Knotenspannungen ($U_1, U_2, U_3$) aufgestellt:
        *   **Gleichung I:**  $1 \cdot U_1 + 1 \cdot U_2 + 1 \cdot U_3 = 6\,V$
        *   **Gleichung II:** $2 \cdot U_1 + 1 \cdot U_2 - 1 \cdot U_3 = 1\,V$
        *   **Gleichung III:** $3 \cdot U_1 - 1 \cdot U_2 + 1 \cdot U_3 = 4\,V$
        """)
        
        st.markdown(r"**Schritt 1: Startmatrix aufstellen**\nWir lassen die Variablen ($U_1, U_2, U_3$) weg und schreiben nur die Zahlen (Koeffizienten) in eine Tabelle.")
        st.latex(r"""
        \begin{array}{l|ccc|c}
        \text{I} & 1 & 1 & 1 & 6 \\
        \text{II} & 2 & 1 & -1 & 1 \\
        \text{III} & 3 & -1 & 1 & 4 
        \end{array}
        """)
        
        st.markdown(r"""
        **Schritt 2: Nullen in der ersten Spalte erzeugen (unter der ersten 1)**
        *Ziel:* Die 2 in Zeile II und die 3 in Zeile III sollen zu Null werden.
        *Weg:* Um die 2 verschwinden zu lassen, rechnen wir Zeile II minus (2 mal Zeile I). Um die 3 verschwinden zu lassen, rechnen wir Zeile III minus (3 mal Zeile I).
        """)
        st.latex(r"""
        \begin{array}{l|ccc|c|l}
        \text{I} & 1 & 1 & 1 & 6 & \text{Bleibt unberührt} \\
        \text{II}' & \color{red}0 & -1 & -3 & -11 & \text{Rechnung: } \text{II} - (2 \cdot \text{I}) \\
        \text{III}' & \color{red}0 & -4 & -2 & -14 & \text{Rechnung: } \text{III} - (3 \cdot \text{I})
        \end{array}
        """)

        st.markdown(r"""
        **Schritt 3: Null in der zweiten Spalte erzeugen (unter der -1)**
        *Ziel:* Die -4 in Zeile III' soll zu Null werden, damit wir unten links unser Dreieck aus drei Nullen haben.
        *Weg:* Wir nutzen jetzt nur noch Zeile II' und III'. Wir rechnen Zeile III' minus (4 mal Zeile II').
        """)
        st.latex(r"""
        \begin{array}{l|ccc|c|l}
        \text{I} & 1 & 1 & 1 & 6 & \\
        \text{II}' & 0 & -1 & -3 & -11 & \\
        \text{III}'' & 0 & \color{blue}0 & 10 & 30 & \text{Rechnung: } \text{III}' - (4 \cdot \text{II}')
        \end{array}
        """)

        st.markdown(r"""
        **Schritt 4: Rückwärtseinsetzen (von unten nach oben auflösen)**
        Wir übersetzen die Matrix zurück in Gleichungen und lösen sie auf:
        * **Aus Zeile III'':** $10 \cdot U_3 = 30 \implies \mathbf{U_3 = 3\,V}$
        * **Einsetzen in Zeile II':** $-1 \cdot U_2 - 3 \cdot (3) = -11 \implies -U_2 - 9 = -11 \implies \mathbf{U_2 = 2\,V}$
        * **Einsetzen in Zeile I:** $1 \cdot U_1 + 1 \cdot (2) + 1 \cdot (3) = 6 \implies U_1 + 5 = 6 \implies \mathbf{U_1 = 1\,V}$
        """)

    # --- 2. CRAMERSCHE REGEL ---
    st.header("2. Cramersche Regel (2x2 Matrix)")
    st.write("Schnelle Alternative zum Gauß-Verfahren, wenn man nur 2 Gleichungen hat.")
    
    with st.expander("Fiktive Aufgabe & Rechner"):
        st.markdown(r"""
        **Fiktive Aufgabe (Maschenstromverfahren):**
        Wir haben zwei Maschenströme ($I_1, I_2$) aufgestellt:
        * Gleichung I:  $2 \cdot I_1 + 1 \cdot I_2 = 5\,V$
        * Gleichung II: $4 \cdot I_1 - 2 \cdot I_2 = 2\,V$
        
        **Lösungsweg (Über-Kreuz-Rechnen der Determinante D):**
        * $D = (2 \cdot -2) - (1 \cdot 4) = -8$
        * $D_{I1} = (5 \cdot -2) - (1 \cdot 2) = -12 \implies I_1 = \frac{-12}{-8} = \mathbf{1{,}5\,A}$
        * $D_{I2} = (2 \cdot 2) - (5 \cdot 4) = -16 \implies I_2 = \frac{-16}{-8} = \mathbf{2{,}0\,A}$
        """)
        st.divider()
        st.write("**Eigene Werte berechnen:**")
        
        col1, col2, col3 = st.columns(3)
        with col1: a11 = st.number_input("Zahl 1 oben (a11)", value=2.0)
        with col2: a12 = st.number_input("Zahl 2 oben (a12)", value=1.0)
        with col3: b1 = st.number_input("Ergebnis I (b1)", value=5.0)
        
        col4, col5, col6 = st.columns(3)
        with col4: a21 = st.number_input("Zahl 1 unten (a21)", value=4.0)
        with col5: a22 = st.number_input("Zahl 2 unten (a22)", value=-2.0)
        with col6: b2 = st.number_input("Ergebnis II (b2)", value=2.0)
        
        hauptdeterminante_D = (a11 * a22) - (a12 * a21)
        if hauptdeterminante_D != 0:
            Dx = (b1 * a22) - (a12 * b2)
            Dy = (a11 * b2) - (b1 * a21)
            st.success(f"Lösung: **Unbekannte 1 = {Dx / hauptdeterminante_D:.2f}** | **Unbekannte 2 = {Dy / hauptdeterminante_D:.2f}**")
        else:
            st.error("Die Hauptdeterminante ist 0. Das System ist nicht eindeutig lösbar.")

    # --- 3. KOMPLEXE RECHNUNG ---
    st.header("3. Komplexe Wechselstromrechnung")
    
    with st.expander("Fiktive Aufgabe & Rechner"):
        st.markdown(r"""
        **Fiktive Aufgabe:**
        Eine Spule mit einem Wirkwiderstand von $R = 4\,\Omega$ und einem induktiven Blindwiderstand von $X_L = 3\,\Omega$ ist an Wechselstrom angeschlossen. Wie groß ist der Scheinwiderstand ($Z$) und der Phasenwinkel ($\varphi$)?
        
        **Lösungsweg (Kartesisch $\rightarrow$ Polar):**
        * $Z = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = \mathbf{5\,\Omega}$
        * $\varphi = \arctan(\frac{3}{4}) = \mathbf{36{,}87^\circ}$
        """)
        st.divider()
        
        richtung = st.radio("Umrechnungsrichtung wählen:", ["Kartesisch zu Polar (R, X -> Z, φ)", "Polar zu Kartesisch (Z, φ -> R, X)"])
        
        if richtung == "Kartesisch zu Polar (R, X -> Z, φ)":
            real = st.number_input("Realteil R (Wirkwiderstand in Ω):", value=4.0, key="c_real")
            imag = st.number_input("Imaginärteil X (Blindwiderstand in Ω):", value=3.0, key="c_imag")
            z = math.sqrt(real**2 + imag**2)
            winkel_grad = math.degrees(math.atan2(imag, real))
            st.success(f"Polarform: **Z = {z:.2f} Ω** | **Winkel φ = {winkel_grad:.2f}°**")
            
        elif richtung == "Polar zu Kartesisch (Z, φ -> R, X)":
            z_betrag = st.number_input("Betrag Z (Scheinwiderstand in Ω):", value=5.0, key="c_z")
            winkel = st.number_input("Winkel φ (in Grad °):", value=36.87, key="c_winkel")
            realteil = z_betrag * math.cos(math.radians(winkel))
            imagteil = z_betrag * math.sin(math.radians(winkel))
            st.success(f"Kartesische Form: **R = {realteil:.2f} Ω** | **X = {imagteil:.2f} Ω**")

    # --- 4. TRIGONOMETRIE (LEISTUNGSDREIECK) ---
    st.header("4. Trigonometrie (Das Leistungsdreieck)")
    
    with st.expander("Fiktive Aufgabe & Rechner"):
        st.markdown(r"""
        **Fiktive Aufgabe:**
        Ein Asynchronmotor nimmt $P = 3000\,W$ Wirkleistung und $Q = 4000\,var$ Blindleistung aus dem Netz auf. Berechne die Scheinleistung ($S$) und den Wirkfaktor ($\cos\varphi$).
        
        **Lösungsweg (Satz des Pythagoras):**
        * Scheinleistung $S = \sqrt{3000^2 + 4000^2} = \mathbf{5000\,VA}$
        * Wirkfaktor $\cos(\varphi) = \frac{P}{S} = \frac{3000}{5000} = \mathbf{0{,}6}$
        """)
        st.divider()
        
        st.latex(r"S = \sqrt{P^2 + Q^2} \quad ; \quad \cos(\varphi) = \frac{P}{S}")
        P = st.number_input("Wirkleistung P (in W):", value=3000.0)
        Q = st.number_input("Blindleistung Q (in var):", value=4000.0)
        
        S = math.sqrt(P**2 + Q**2)
        cos_phi = P / S
        winkel_p = math.degrees(math.acos(cos_phi))
        
        st.success(f"Scheinleistung **S = {S:.2f} VA** | Wirkfaktor **cos(φ) = {cos_phi:.2f}** | **Winkel φ = {winkel_p:.2f}°**")

    # --- 5. PQ-FORMEL ---
    st.header("5. PQ-Formel (Quadratische Gleichungen)")
    
    with st.expander("Fiktive Aufgabe & Rechner"):
        st.markdown(r"""
        **Fiktive Aufgabe:**
        Bei der Berechnung einer Resonanzfrequenz stoßen wir auf die Gleichung: $x^2 - 2x - 8 = 0$. Wir müssen die Nullstellen (Grenzfrequenzen) finden.
        Hier ist $p = -2$ und $q = -8$.
        
        **Lösungsweg:**
        * $x_{1,2} = -\frac{-2}{2} \pm \sqrt{\left(\frac{-2}{2}\right)^2 - (-8)}$
        * $x_{1,2} = 1 \pm \sqrt{1 + 8} = 1 \pm 3$
        * $\mathbf{x_1 = 4} \quad ; \quad \mathbf{x_2 = -2}$
        """)
        st.divider()
        
        st.latex(r"x^2 + p \cdot x + q = 0 \implies x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}")
        p_val = st.number_input("Wert für p:", value=-2.0)
        q_val = st.number_input("Wert für q:", value=-8.0)
        
        diskriminante = (p_val / 2)**2 - q_val
        if diskriminante > 0:
            x1 = -(p_val / 2) + math.sqrt(diskriminante)
            x2 = -(p_val / 2) - math.sqrt(diskriminante)
            st.success(f"Zwei Lösungen: **x1 = {x1:.2f}** | **x2 = {x2:.2f}**")
        elif diskriminante == 0:
            x1 = -(p_val / 2)
            st.success(f"Eine Lösung: **x = {x1:.2f}**")
        else:
            st.error("Keine reelle Lösung (Wurzel aus negativer Zahl).")

    st.divider()
    st.caption("Quellen: [^1] Lothar Papula, Mathematik für Ingenieure, Band 1 | [^2] Formelsammlung Mathematik für Techniker, Werner-von-Siemens-Schule.")
elif menue == "Lexikon & Abkürzungen":
    st.title("Variablen-Lexikon & Abkürzungen")
    st.write("Schlage hier die Bedeutung von Formelzeichen und Fachbegriffen nach. Nutze die Filter, um die Daten logisch zu sortieren.")
    
    # Zwei Tabs erstellen
    tab_variablen, tab_abkuerzungen = st.tabs(["Formelzeichen (Variablen)", "Abkürzungen"])
    
    with tab_variablen:
        st.subheader("Wichtige Formelzeichen")
        
        # Ein interaktives Dropdown-Menü zum Filtern der Kategorien
        kategorie_filter = st.selectbox(
            "Nach Kategorie filtern:", 
            ["Alle anzeigen", "Grundgrößen & Gleichstrom", "Wechselstrom", "Leistung & Arbeit", "Felder & Magnetismus"]
        )
        
        # Umfassende Daten aus der Wikibooks-Formelsammlung & Grundlagen
        variablen_daten = [
            {"Zeichen": "U", "Bedeutung": "Spannung", "Einheit": "V (Volt)", "Kategorie": "Grundgrößen & Gleichstrom"},
            {"Zeichen": "I", "Bedeutung": "Stromstärke", "Einheit": "A (Ampere)", "Kategorie": "Grundgrößen & Gleichstrom"},
            {"Zeichen": "R", "Bedeutung": "Wirkwiderstand", "Einheit": "Ω (Ohm)", "Kategorie": "Grundgrößen & Gleichstrom"},
            {"Zeichen": "G", "Bedeutung": "Elektrischer Leitwert", "Einheit": "S (Siemens)", "Kategorie": "Grundgrößen & Gleichstrom"},
            {"Zeichen": "Q", "Bedeutung": "Elektrische Ladung", "Einheit": "C (Coulomb) / As", "Kategorie": "Grundgrößen & Gleichstrom"},
            
            {"Zeichen": "Z", "Bedeutung": "Scheinwiderstand (Impedanz)", "Einheit": "Ω (Ohm)", "Kategorie": "Wechselstrom"},
            {"Zeichen": "Y", "Bedeutung": "Scheinleitwert (Admittanz)", "Einheit": "S (Siemens)", "Kategorie": "Wechselstrom"},
            {"Zeichen": "X_C", "Bedeutung": "Kapazitiver Blindwiderstand", "Einheit": "Ω (Ohm)", "Kategorie": "Wechselstrom"},
            {"Zeichen": "X_L", "Bedeutung": "Induktiver Blindwiderstand", "Einheit": "Ω (Ohm)", "Kategorie": "Wechselstrom"},
            {"Zeichen": "f", "Bedeutung": "Frequenz", "Einheit": "Hz (Hertz)", "Kategorie": "Wechselstrom"},
            {"Zeichen": "ω (Omega)", "Bedeutung": "Kreisfrequenz", "Einheit": "1/s", "Kategorie": "Wechselstrom"},
            {"Zeichen": "φ (Phi)", "Bedeutung": "Phasenverschiebungswinkel", "Einheit": "° oder rad", "Kategorie": "Wechselstrom"},
            
            {"Zeichen": "P", "Bedeutung": "Wirkleistung", "Einheit": "W (Watt)", "Kategorie": "Leistung & Arbeit"},
            {"Zeichen": "S", "Bedeutung": "Scheinleistung", "Einheit": "VA (Voltampere)", "Kategorie": "Leistung & Arbeit"},
            {"Zeichen": "Q", "Bedeutung": "Blindleistung", "Einheit": "var (Voltampere reactiv)", "Kategorie": "Leistung & Arbeit"},
            {"Zeichen": "W", "Bedeutung": "Elektrische Arbeit / Energie", "Einheit": "J (Joule) / Ws / kWh", "Kategorie": "Leistung & Arbeit"},
            
            {"Zeichen": "C", "Bedeutung": "Kapazität", "Einheit": "F (Farad)", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "L", "Bedeutung": "Induktivität", "Einheit": "H (Henry)", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "E", "Bedeutung": "Elektrische Feldstärke", "Einheit": "V/m", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "D", "Bedeutung": "Elektrische Flussdichte", "Einheit": "C/m²", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "B", "Bedeutung": "Magnetische Flussdichte", "Einheit": "T (Tesla)", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "H", "Bedeutung": "Magnetische Feldstärke", "Einheit": "A/m", "Kategorie": "Felder & Magnetismus"},
            {"Zeichen": "Φ (Phi)", "Bedeutung": "Magnetischer Fluss", "Einheit": "Wb (Weber)", "Kategorie": "Felder & Magnetismus"}
        ]
        
        # Logik: Nur die Daten anzeigen, die im Dropdown ausgewählt wurden
        if kategorie_filter != "Alle anzeigen":
            variablen_daten = [eintrag for eintrag in variablen_daten if eintrag["Kategorie"] == kategorie_filter]
            
        st.dataframe(variablen_daten, use_container_width=True, hide_index=True)
        
    with tab_abkuerzungen:
        st.subheader("Elektrotechnische Abkürzungen")
        
        suchbegriff = st.text_input("Suche nach einer Abkürzung oder einem Begriff (z. B. RCD, Leiter oder Norm):").lower()
        
        # Umfassende Liste der wichtigsten Abkürzungen inkl. Kategorie
        abkuerzungen = [
            {"Abkürzung": "AC", "Bedeutung": "Alternating Current (Wechselstrom)", "Kategorie": "Allgemein"},
            {"Abkürzung": "DC", "Bedeutung": "Direct Current (Gleichstrom)", "Kategorie": "Allgemein"},
            {"Abkürzung": "RMS", "Bedeutung": "Root Mean Square (Effektivwert)", "Kategorie": "Messtechnik"},
            {"Abkürzung": "RCD / FI", "Bedeutung": "Residual Current Device (Fehlerstromschutzschalter)", "Kategorie": "Schutztechnik"},
            {"Abkürzung": "LS", "Bedeutung": "Leitungsschutzschalter", "Kategorie": "Schutztechnik"},
            {"Abkürzung": "PE", "Bedeutung": "Protective Earth (Schutzleiter)", "Kategorie": "Netzformen"},
            {"Abkürzung": "N", "Bedeutung": "Neutralleiter", "Kategorie": "Netzformen"},
            {"Abkürzung": "PEN", "Bedeutung": "Protective Earth Neutral (Kombinierter Schutz- und Neutralleiter)", "Kategorie": "Netzformen"},
            {"Abkürzung": "L1, L2, L3", "Bedeutung": "Außenleiter (Phasen) im Dreiphasenwechselstrom", "Kategorie": "Netzformen"},
            {"Abkürzung": "VDE", "Bedeutung": "Verband der Elektrotechnik, Elektronik und Informationstechnik", "Kategorie": "Normen & Gesetze"},
            {"Abkürzung": "DGUV", "Bedeutung": "Deutsche Gesetzliche Unfallversicherung (z. B. DGUV V3)", "Kategorie": "Normen & Gesetze"},
            {"Abkürzung": "TAB", "Bedeutung": "Technische Anschlussbedingungen", "Kategorie": "Normen & Gesetze"},
            {"Abkürzung": "PELV", "Bedeutung": "Protective Extra Low Voltage (Schutzkleinspannung)", "Kategorie": "Schutzklassen"},
            {"Abkürzung": "SELV", "Bedeutung": "Safety Extra Low Voltage (Sicherheitskleinspannung)", "Kategorie": "Schutzklassen"},
            {"Abkürzung": "FELV", "Bedeutung": "Functional Extra Low Voltage (Funktionskleinspannung)", "Kategorie": "Schutzklassen"}
        ]
        
        # Logik: Filtere die Liste anhand der Eingabe im Suchfeld (sucht in allen 3 Spalten)
        gefilterte_daten = [eintrag for eintrag in abkuerzungen if suchbegriff in eintrag["Abkürzung"].lower() or suchbegriff in eintrag["Bedeutung"].lower() or suchbegriff in eintrag["Kategorie"].lower()]
        
        st.dataframe(gefilterte_daten, use_container_width=True, hide_index=True)
        
    st.divider()
    st.caption("Quellen: [^1] Wikibooks: Formelsammlung Elektrotechnik | [^2] VDE-Normen | [^3] Formelsammlung Elektrotechnik, Werner-von-Siemens-Schule.")
elif menue == "Formelsammlung":
    render_formelsammlung()
elif menue == "Dokumente & Uploads":
    st.title("Dokumente & Uploads")
    st.write("Lade hier deine Schaltpläne, PDFs oder Bilder für die Weiterbildung hoch.")
    
    import os
    
    # Prüfen, ob der Ordner "uploads" existiert, falls nicht: erstellen
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
        
    # Das Upload-Feld für den Nutzer (beschränkt auf PDFs und Bilder)
    hochgeladene_datei = st.file_uploader("Wähle eine Datei aus", type=["pdf", "png", "jpg", "jpeg"])
    
    if hochgeladene_datei is not None:
        # Dateipfad zusammenbauen (Zielordner + Dateiname)
        dateipfad = os.path.join("uploads", hochgeladene_datei.name)
        
        # Die Datei physisch auf der Festplatte speichern
        with open(dateipfad, "wb") as f:
            f.write(hochgeladene_datei.getbuffer())
            
        st.success(f"Datei '{hochgeladene_datei.name}' wurde erfolgreich gespeichert!")
        
        # Wenn es ein Bild ist, zeigen wir es direkt auf der Website an
        if hochgeladene_datei.type in ["image/png", "image/jpeg", "image/jpg"]:
            st.image(hochgeladene_datei, caption=f"Vorschau: {hochgeladene_datei.name}")
        