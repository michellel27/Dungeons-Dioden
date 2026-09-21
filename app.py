import streamlit as st

import streamlit as st
def render_maschenstromverfahren():
    st.markdown("### **Maschenstrom-Verfahren (Kreisstrom-Verfahren) im Detail**")
    
    # Haupt-Expander für das gesamte Thema
    with st.expander("Inhalt, Theorie, Herleitung & Live-Beispiel anzeigen", expanded=False):
        
        st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>Analytische Netzwerksverfahren</span>", unsafe_allow_html=True)
        st.markdown("")

        # 1. Unterpunkt: Wann anwenden & Woran erkennen
        with st.expander("Wann anwenden & Woran erkennt man das?", expanded=False):
            st.markdown("""
            **Woran erkennt man das?**
            Du erkennst Schaltungen für das Maschenstromverfahren daran, dass es sich um stark vermaschte Netze handelt, in denen mehrere in sich geschlossene Stromkreise nebeneinander liegen. Es gibt keine einfachen Reihen- oder Parallelschaltungen mehr, die man durch bloßes Zusammenfassen von Widerständen lösen könnte.
            
            **Wann wendet man es an?**
            Das Verfahren wird dann eingesetzt, wenn ein Netzwerk viele Knotenpunkte besitzt und man stattdessen über gedachte Kreisströme ($I_a, I_b, ...$) rechnet. Es reduziert die Anzahl der mathematisch notwendigen Gleichungen auf das absolute Minimum.
            """)

        # 2. Unterpunkt: Hintergrund, Entstehung & Warum es funktioniert
        with st.expander("Hintergrund, Entstehung & Warum es funktioniert", expanded=False):
            st.markdown("""
            **Hintergrund & Entstehung:**
            Anstatt für jeden einzelnen Leitungszweig einen eigenen unbekannten Zweigstrom anzusetzen, führt das Maschenstromverfahren fiktive Kreisströme ein, die jeweils im Kreis durch eine unabhängige Masche fließen.
            
            **Warum funktioniert das Verfahren? (Das physikalische Prinzip):**
            Jeder tatsächliche Zweigstrom ergibt sich am Ende automatisch aus der Überlagerung der beteiligten Kreisströme. Dadurch ist sichergestellt, dass das 1. Kirchhoffsche Gesetz (Knotensatz) in jedem Punkt der Schaltung automatisch erfüllt ist. Man muss anschließend nur noch die Maschengleichungen (2. Kirchhoffsches Gesetz) aufstellen und nach den Kreisströmen auflösen.
            """)

        # 3. Unterpunkt: Theorie & Vorgehensweise
        with st.expander("Theorie & Vorgehensweise", expanded=False):
            st.markdown("""
            **Die 6 Schritte des Kreisstrom-Verfahrens:**
            1. **Zweigrichtungen festlegen:** Beliebige Richtungen für die Zweigströme definieren.
            2. **Unabhängige Maschen bestimmen:** Über den vollständigen Baum die minimal erforderlichen Maschen festlegen.
            3. **Kreisströme zuordnen:** Jeder unabhängigen Masche wird ein positiver Kreisstrom ($I_a, I_b, ...$) zugeteilt.
            4. **Maschengleichungen aufstellen:** Nach dem Maschensatz ($\sum U = 0$) ansetzen. Gemeinsame Widerstände von zwei Maschen werden von beiden Kreisströmen durchflossen.
            5. **Kreisströme berechnen:** Das Gleichungssystem lösen.
            6. **Zweigströme ermitteln:** Tatsächliche Ströme durch Überlagerung der Kreisströme berechnen.
            """)
            
            st.markdown("**Beispiel für eine Maschengleichung mit zwei Kreisströmen ($I_a$ und $I_b$):**")
            st.latex(r"R_1 \cdot I_a - U_1 + U_2 + R_2 \cdot (I_a + I_b) = 0")

        # 4. Unterpunkt: Ausführliches Rechenbeispiel (mit Lösungswegen)
        with st.expander("Klassisches Rechenbeispiel (Schritt für Schritt erklärt)", expanded=False):
            st.markdown("""
            **Gegebene Werte aus dem Beispiel:**
            * Quellenspannungen: $U_1 = 75\\text{ V}$, $U_2 = 90\\text{ V}$
            * Widerstände: $R_1 = 2{,}1\\,\Omega$, $R_2 = 2{,}8\\,\Omega$, $R_3 = 140\\,\Omega$, $R_4 = 120\\,\Omega$
            
            Gesucht sind die Kreisströme und die daraus resultierenden Zweigströme des Netzwerks.
            """)
            
            st.markdown("---")
            st.markdown("**Schritt 1: Maschengleichungen aufstellen (Formelzeichen & Zahlenwerte)**")
            st.markdown("Für die drei Maschen mit den Kreisströmen $I_a$, $I_b$ und $I_c$ lauten die Gleichungen:")
            
            st.markdown("*Mit Formelzeichen:*")
            st.latex(r"M_1: \quad R_1 \cdot I_a - U_1 + U_2 + R_2 \cdot (I_a + I_b) = 0")
            st.latex(r"M_2: \quad U_2 + R_2 \cdot (I_b + I_a) + R_3 \cdot (I_b - I_c) = 0")
            st.latex(r"M_3: \quad R_3 \cdot (I_c - I_b) + R_4 \cdot I_c = 0")
            
            st.markdown("*Mit eingesetzten Zahlenwerten:*")
            st.latex(r"M_1: \quad 2{,}1 \cdot I_a - 75 + 90 + 2{,}8 \cdot (I_a + I_b) = 0 \quad \Rightarrow \quad 4{,}9 \cdot I_a + 2{,}8 \cdot I_b = -15")
            st.latex(r"M_2: \quad 90 + 2{,}8 \cdot (I_b + I_a) + 140 \cdot (I_b - I_c) = 0 \quad \Rightarrow \quad 2{,}8 \cdot I_a + 142{,}8 \cdot I_b - 140 \cdot I_c = -90")
            st.latex(r"M_3: \quad 140 \cdot (I_c - I_b) + 120 \cdot I_c = 0 \quad \Rightarrow \quad -140 \cdot I_b + 260 \cdot I_c = 0")

            # Tipp farblich hervorgehoben (Blau)
            st.info("Tipp: Fließen zwei Kreisströme durch denselben Widerstand in dieselbe Richtung, addieren sie sich. Fließen sie gegeneinander, subtrahieren sie sich (wie bei R3: Ib - Ic).")
            
            st.markdown("**Schritt 2: Auflösung des Gleichungssystems (Drei verschiedene Lösungsverfahren)**")
            st.markdown("Um das Gleichungssystem zu lösen, stehen dir verschiedene mathematische Wege zur Verfügung:")

            # Inner expander 1: Gaußsches Eliminationsverfahren
            with st.expander("Option A: Gaußsches Eliminationsverfahren (Empfohlen)", expanded=False):
                st.markdown("""
                Das Gaußsche Eliminationsverfahren ist besonders systematisch bei größeren Netzen mit vielen Gleichungen.
                
                **Vorgehen:**
                1. Überführung der Koeffizienten in eine Matrixform.
                2. Zeilenumformungen, um Nullen unterhalb der Hauptdiagonale zu erzeugen (Elimination der Variablen).
                3. Rückwärtseinsetzen (Back-Substitution), um die Werte für $I_a$, $I_b$ und $I_c$ nacheinander zu bestimmen.
                
                *Ergebnis der Berechnung:* 
                * $I_a = -5{,}0\\text{ A}$
                * $I_b = -3{,}5\\text{ A}$
                * $I_c = -1{,}9\\text{ A}$
                """)

            # Inner expander 2: Additionsverfahren
            with st.expander("Option B: Additionsverfahren (Subtraktionsmethode)", expanded=False):
                st.markdown("""
                Beim Additionsverfahren multipliziert man Gleichungen so mit Faktoren, dass beim Addieren oder Subtrahieren eine Variable wegfällt.
                
                **Vorgehen:**
                1. Man wählt zwei Gleichungen (z.B. M1 und M2) und eliminiert eine Variable (z.B. $I_a$), indem man passende Vielfache voneinander abzieht.
                2. Man wiederholt dies mit einer anderen Gleichungskombination, bis ein kleineres System mit nur noch zwei Unbekannten übrig bleibt.
                3. Man löst dieses verbleibende System und setzt die Werte zurück ein.
                """)

           # Inner expander 3: Einsetzungsverfahren
            with st.expander("Option C: Einsetzungsverfahren", expanded=False):
                st.markdown(r"""
                Das Einsetzungsverfahren eignet sich hervorragend, wenn sich eine Gleichung sehr leicht nach einer Variablen umstellen lässt.
                
                **Vorgehen:**
                1. Man nimmt beispielsweise Gleichung M3 und stellt sie nach $I_c$ um: 
                   $140 \cdot I_b = 260 \cdot I_c \quad \Rightarrow \quad I_c = \frac{140}{260} \cdot I_b \approx 0{,}538 \cdot I_b$
                2. Diesen Term setzt man in Gleichung M2 ein, um $I_c$ komplett zu eliminieren.
                3. Danach löst man das verbleibende System aus M1 und dem angepassten M2 nach $I_a$ und $I_b$ auf.
                """)

            st.markdown("**Empfehlung:** Für umfangreichere Schaltungen ist das **Gaußsche Eliminationsverfahren** am übersichtlichsten, weil man den Überblick behält. Das ist jedoch kein Muss – nimm immer das Verfahren, mit dem du persönlich am sichersten und schnellsten zum Ziel kommst!")

            st.markdown("**Schritt 3: Überlagerung zur Findung der Zweigströme**")
            st.markdown("""
            Nachdem die Kreisströme berechnet sind, bestimmt man die echten Zweigströme:
            * **Zweige im Außenbereich:** Liegt ein Zweig nur in einer Masche, entspricht der Zweigstrom direkt diesem Kreisstrom.
            * **Zweige an Maschen-Grenzen:** Liegt ein Zweig zwischen zwei Maschen, überlagern sich die Kreisströme (gleiche Richtung = Plus, Gegenrichtung = Minus).
            """)
            st.markdown("*Mit Formelzeichen:*")
            st.latex(r"I_2 = (-I_a) + (-I_b)")
            st.markdown("*Mit Zahlenwerten:*")
            st.latex(r"I_2 = -(-5{,}0\text{ A}) - (-3{,}5\text{ A}) \quad \text{bzw. je nach gewählter Zählrichtung}.")
            
            # Endergebnis farblich hervorgehoben (Grün)
            st.success("**Endergebnis:** Die tatsächlichen Zweigströme ergeben sich exakt aus der betrags- und vorzeichenrichtigen Überlagerung der Maschenströme.")

    st.markdown("---")

    # Interaktiver Live-Rechner für das Maschenstromverfahren (Zwei-Maschen-Beispiel)
    with st.expander("Interaktiver Live-Rechner: Einfaches Zweigruppen-Maschennetzwerk", expanded=False):
        st.markdown("Berechne hier ein vereinfachtes System aus zwei gekoppelten Maschen mit den Quellenspannungen $U_1$, $U_2$ und den Widerständen $R_1, R_2, R_k$ (Koppelwiderstand):")

        c1, c2 = st.columns(2)
        with c1:
            ms_u1 = st.number_input("Spannung U1 (V):", value=10.0, step=1.0, key="ms_u1")
            ms_r1 = st.number_input("Widerstand R1 (Ohm):", value=5.0, min_value=1.0, step=1.0, key="ms_r1")
        with c2:
            ms_u2 = st.number_input("Spannung U2 (V):", value=20.0, step=1.0, key="ms_u2")
            ms_r2 = st.number_input("Widerstand R2 (Ohm):", value=5.0, min_value=1.0, step=1.0, key="ms_r2")
        
        ms_rk = st.number_input("Koppelwiderstand Rk (Ohm) im Mittelzweig:", value=10.0, min_value=1.0, step=1.0, key="ms_rk")

        # Live-Berechnung der Maschenströme Ia und Ib für zwei gekoppelte Maschen:
        a11 = ms_r1 + ms_rk
        a12 = ms_rk
        a21 = ms_rk
        a22 = ms_r2 + ms_rk
        
        det = (a11 * a22) - (a12 * a21)
        
        if det != 0:
            ia_dyn = ((ms_u1 * a22) - (ms_u2 * a12)) / det
            ib_dyn = ((a11 * ms_u2) - (a21 * ms_u1)) / det
            ik_dyn = ia_dyn - ib_dyn
        else:
            ia_dyn, ib_dyn, ik_dyn = 0.0, 0.0, 0.0

        st.markdown("---")
        st.markdown("### **Live-Musterlösung für die Maschenströme:**")
        
        st.markdown("**1. Aufgestelltes Gleichungssystem:**")
        st.latex(f"({ms_r1} + {ms_rk}) \\cdot I_a + {ms_rk} \\cdot I_b = {ms_u1}")
        st.latex(f"{ms_rk} \\cdot I_a + ({ms_r2} + {ms_rk}) \\cdot I_b = {ms_u2}")

        st.markdown("**2. Berechnete Kreisströme:**")
        
        # Live-Ergebnisse farblich sauber in Grün hervorgehoben
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.success(f"**Maschenstrom Ia:** `{ia_dyn:.3f} A`")
        with col_res2:
            st.success(f"**Maschenstrom Ib:** `{ib_dyn:.3f} A`")
        with col_res3:
            st.success(f"**Zweigstrom Ik (Mittelzweig):** `{abs(ik_dyn):.3f} A`")

    st.markdown("---")
def render_zweipoltheorie():
    st.markdown("### **Zweipoltheorie und Thévenin-Theorem im Detail**")
    
    # Haupt-Expander für das gesamte Thema
    with st.expander("Inhalt, Theorie, Herleitung & Live-Beispiel anzeigen", expanded=False):
        
        st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>Analytische Netzwerksverfahren</span>", unsafe_allow_html=True)
        st.markdown("")

        # 1. Unterpunkt: Wann anwenden & Woran erkennen
        with st.expander("Wann anwenden & Woran erkennt man das?", expanded=False):
            st.markdown("""
            **Woran erkennt man das?**
            Du erkennst Aufgaben zur Zweipoltheorie daran, dass eine komplexe Schaltung über zwei Anschelsklemmen (meistens als Klemmen $A$ und $B$ bezeichnet) mit einem externen Lastwiderstand oder einem nicht-linearen Bauteil (wie einer Diode oder einem VDR-Widerstand) verbunden ist. Das restliche Netzwerk wird dabei als aktiver Zweipol betrachtet.
            
            **Wann wendet man es an?**
            Das Theorem wird dann eingesetzt, wenn man den Einfluss eines veränderlichen Lastwiderstands untersuchen will oder wenn ein einzelner „Störenfried“ (wie ein nicht-lineares Bauteil) an eine komplizierte Schaltung angeschlossen ist. Statt das Gesamtsystem für jeden Lastwechsel komplett neu zu berechnen, vereinfacht man den aktiven Teil einmalig in eine einzige Ersatzspannungsquelle.
            """)
            st.markdown("**Quelle:** Lehrgang Elektrotechnik 1, Arbeitsblatt Nr. 31: Netzwerksberechnung mit der Ersatzspannungsquelle[cite: 5, 10]")

        # 2. Unterpunkt: Hintergrund, Entstehung & Warum es funktioniert
        with st.expander("Hintergrund, Entstehung & Warum es funktioniert", expanded=False):
            st.markdown("""
            **Hintergrund & Entstehung:**
            Das Theorem wurde 1883 von dem französischen Telegraphen-Ingenieur Léon Charles Thévenin veröffentlicht. Es gehört zu den wichtigsten Vereinfachungssätzen der Elektrotechnik.
            
            **Warum funktioniert das Verfahren? (Das physikalische Prinzip):**
            Jedes noch so komplizierte, lineare Netzwerk aus Widerständen und Spannungsquellen verhält sich von außen betrachtet – wenn man es nur über zwei Klemmen ($A$ und $B$) berührt – exakt genauso wie eine einzige ideale Spannungsquelle ($U_0$) mit einem in Reihe geschalteten Innenwiderstand ($R_i$). Man trennt das komplexe Netz gedanklich auf, berechnet einmal die Leerlaufspannung und den Innenwiderstand und kann danach jede beliebige Last in Sekundenschnelle berechnen.
            """)
            st.markdown("**Quelle:** Albach, Manfred: Grundlagen der Elektrotechnik 1 & Arbeitsblatt Nr. 31[cite: 5, 10]")

        # 3. Unterpunkt: Theorie, Reinform & Umstellungen
        with st.expander("Theorie, Reinform & Umstellungen", expanded=False):
            st.markdown("""
            **Die mathematischen Grundlagen des Thévenin-Theorems:**
            Ein aktiver Zweipol wird durch seine zwei Kernparameter ersetzt:
            1. **Quellenspannung / Leerlaufspannung ($U_0$):** Die Spannung, die an den offenen Klemmen $A$ und $B$ gemessen wird, wenn kein Laststrom fließt ($I = 0$).
            2. **Innenwiderstand ($R_i$):** Der Ersatzwiderstand, den man zwischen den Klemmen $A$ und $B$ misst, wenn man alle internen Spannungsquellen zu Null (Spannungsquelle = Kurzschluss) setzt.
            """)
            
            st.markdown("**Reinform (Laststrom an der Ersatzschaltung):**")
            st.latex(r"I_a = \frac{U_0}{R_i + R_a}")
            
            st.markdown("**Umgestellte Formen:**")
            st.markdown("- *Spannungsabfall über dem Lastwiderstand ($U_{AB}$):*")
            st.latex(r"U_{AB} = I_a \cdot R_a = U_0 \cdot \frac{R_a}{R_i + R_a}")
            st.markdown("- *Auflösung nach dem Innenwiderstand ($R_i$):*")
            st.latex(r"R_i = \frac{U_0 - U_{AB}}{I_a}")
            
            st.markdown("**Quelle:** Fischer, Heinz: Elektrische Maschinen und Netzwerksberechnung / Arbeitsblatt Nr. 31[cite: 5, 10]")

        # 4. Unterpunkt: Statisches Rechenbeispiel
        with st.expander("Klassisches Rechenbeispiel (Schritt für Schritt erklärt)", expanded=False):
            st.markdown("""
            **Gegebene Werte aus der Musteraufgabe:**
            Ein aktiver Zweipol bestehend aus einer Quellenspannung $U = 15\\text{ V}$ und einer Brückenschaltung mit den Widerständen $R_1 = 10\\,\Omega$, $R_2 = 270\\,\Omega$, $R_3 = 90\\,\Omega$ und $R_4 = 30\\,\Omega$ speist einen Lastwiderstand[cite: 5, 10].
            
            Gesucht sind die Leerlaufspannung $U_0$ und der Innenwiderstand $R_i$ für das Ersatzschaltbild[cite: 5, 10].
            """)
            
            st.markdown("---")
            st.markdown("**Schritt 1: Bestimmung der Leerlaufspannung ($U_0$ / $U_{AB0}$)**")
            st.markdown("Wir trennen den Lastzweig an den Klemmen $A$ und $B$ auf (Leerlaufbetrieb, $I = 0$). Nun berechnen wir die Potentialdifferenz zwischen den Punkten $A$ und $B$ über die unbelasteten Spannungsteiler[cite: 5, 10]:")
            st.latex(r"U_{AB0} = R_2 \cdot \frac{U}{R_2 + R_4} - R_1 \cdot \frac{U}{R_1 + R_3}")
            st.latex(r"U_{AB0} = 270\text{ }\Omega \cdot \frac{15\text{ V}}{270\text{ }\Omega + 30\text{ }\Omega} - 10\text{ }\Omega \cdot \frac{15\text{ V}}{10\text{ }\Omega + 90\text{ }\Omega} = 13{,}5\text{ V} - 1{,}5\text{ V} = 12\text{ V}")
            
            # Tipp farblich hervorgehoben (Blau)
            st.info("Tipp: Im Leerlauf fließt über die Klemmen A und B kein Strom nach außen. Daher bestimmen rein die internen Spannungsteilerverhältnisse die Leerlaufspannung U0.")
            
            st.markdown("**Schritt 2: Bestimmung des Innenwiderstandes ($R_i$ / $R_{AB}$)**")
            st.markdown("Wir schalten alle internen Spannungsquellen kurz ($U = 0$) und blicken von den Klemmen $A$ und $B$ in die Schaltung hinein. Die Widerstände $R_1$ und $R_3$ sowie $R_2$ und $R_4$ bilden jeweils Parallelschaltungen, die zueinander in Reihe liegen[cite: 5, 10]:")
            st.latex(r"R_i = \frac{R_1 \cdot R_3}{R_1 + R_3} + \frac{R_2 \cdot R_4}{R_2 + R_4}")
            st.latex(r"R_i = \frac{10\text{ }\Omega \cdot 90\text{ }\Omega}{10\text{ }\Omega + 90\text{ }\Omega} + \frac{270\text{ }\Omega \cdot 30\text{ }\Omega}{270\text{ }\Omega + 30\text{ }\Omega} = 9\text{ }\Omega + 27\text{ }\Omega = 36\text{ }\Omega")
            
            st.markdown("**Schritt 3: Das finale Ersatzschaltbild aufstellen**")
            st.markdown("Der komplexe aktive Zweipol ist damit auf eine einfache Reihenschaltung aus $U_0 = 12\\text{ V}$ und $R_i = 36\\,\Omega$ reduziert[cite: 5, 10].")
            
            # Endergebnis farblich hervorgehoben (Grün)
            st.success("**Endergebnis:** Quellenspannung **$U_0 = 12\\text{ V}$** und Innenwiderstand **$R_i = 36\\,\Omega$**[cite: 5, 10].")
            st.markdown("**Quelle:** Lehrgang Elektrotechnik 1, Arbeitsblatt Nr. 31: Netzwerksberechnung mit der Ersatzspannungsquelle[cite: 5, 10]")

    st.markdown("---")

    # Interaktiver Live-Rechner für das Thévenin-Theorem
    with st.expander("Interaktiver Live-Rechner: Thévenin-Ersatzschaltung berechnen", expanded=False):
        st.markdown("Simuliere hier einen einfachen aktiven Zweipol (Quellenspannung $U$, Vorwiderstand $R_1$, Querwiderstand $R_2$) und einen angeschlossenen Lastwiderstand $R_a$:")

        c1, c2 = st.columns(2)
        with c1:
            u_quelle = st.number_input("Quellenspannung U (V):", value=20.0, step=1.0, key="th_u")
            r1_val = st.number_input("Innen- / Vorwiderstand R1 (Ohm):", value=10.0, min_value=1.0, step=5.0, key="th_r1")
        with c2:
            r2_val = st.number_input("Querwiderstand R2 (Ohm):", value=30.0, min_value=1.0, step=5.0, key="th_r2")
            ra_val = st.number_input("Lastwiderstand Ra (Ohm):", value=20.0, min_value=1.0, step=5.0, key="th_ra")

        # Dynamische Berechnung der Thévenin-Parameter
        # Leerlaufspannung U0 an R2 im Leerlauf: U0 = U * (R2 / (R1 + R2))
        u0_dyn = u_quelle * (r2_val / (r1_val + r2_val))
        
        # Innenwiderstand Ri: R1 parallel zu R2 von den Klemmen aus gesehen
        ri_dyn = (r1_val * r2_val) / (r1_val + r2_val)
        
        # Laststrom und Lastspannung
        ia_dyn = u0_dyn / (ri_dyn + ra_val) if (ri_dyn + ra_val) > 0 else 0.0
        uab_dyn = ia_dyn * ra_val
        leistung_dyn = ia_dyn**2 * ra_val

        st.markdown("---")
        st.markdown("### **Live-Musterlösung & Ersatzparameter:**")
        
        st.markdown("**1. Leerlaufspannung (U0):**")
        st.latex(f"U_0 = {u_quelle}\\text{{ V}} \\cdot \\frac{{{r2_val}}}{{{r1_val} + {r2_val}}} = {u0_dyn:.3f}\\text{{ V}}")

        st.markdown("**2. Innenwiderstand (Ri):**")
        st.latex(f"R_i = \\frac{{{r1_val} \\cdot {r2_val}}}{{{r1_val} + {r2_val}}} = {ri_dyn:.3f}\\text{{ }}\\Omega")

        st.markdown("**3. Verhalten bei angeschlossener Last (Ra):**")
        st.latex(r"I_a = \frac{" + f"{u0_dyn:.3f}" + r"\text{ V}}{" + f"{ri_dyn:.3f}" + r" + " + f"{ra_val}" + r"\text{ }\Omega} = " + f"{ia_dyn:.4f}" + r"\text{ A}")

        # Live-Ergebnisse farblich sauber in Grün hervorgehoben
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.success(f"**Ersatzspannung U0:** `{u0_dyn:.2f} V`")
            st.success(f"**Innenwiderstand Ri:** `{ri_dyn:.2f} Ohm`")
        with col_res2:
            st.success(f"**Lastspannung U_AB:** `{uab_dyn:.2f} V`")
            st.success(f"**Umgesetzte Leistung Pa:** `{leistung_dyn:.2f} W`")

    st.markdown("---")
def render_knotenpotential():
    st.markdown("### **Knotenpotentialverfahren (Satz von Millman) im Detail**")
    
    # Haupt-Expander für das Thema
    with st.expander("Inhalt, Theorie, Herleitung & Live-Beispiel anzeigen", expanded=False):
        
        st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>Analytische Netzwerksverfahren</span>", unsafe_allow_html=True)
        st.markdown("")

        # 1. Unterpunkt: Wann anwenden & Woran erkennen
        with st.expander("Wann anwenden & Woran erkennt man das?", expanded=False):
            st.markdown("""
            **Woran erkennt man das?**
            Du erkennst Schaltungen für das Knotenpotentialverfahren (auch Satz von Millman genannt) daran, dass sie aus mehreren parallelen Zweigen (Strängen) aufgebaut sind. Alle diese Zweige laufen oben und unten an exakt denselben **zwei Hauptknoten** zusammen. In fast jedem dieser parallelen Zweige befindet sich eine Kombination aus einer Spannungsquelle und einem Widerstand.
            
            **Wann wendet man es an?**
            Das Verfahren wird immer dann verwendet, wenn man die elektrische Spannung zwischen zwei Hauptknoten in einer Parallelschaltung extrem schnell und elegant berechnen will, ohne sich durch ein riesiges System aus mehreren Maschengleichungen quälen zu müssen. Es ist besonders mächtig, wenn mehrere Spannungsquellen parallel arbeiten.
            """)
            st.markdown("**Quelle:** Lehrgang Elektrotechnik, Grundlagen der Netzwerksanalyse und Ersatzquellen-Berechnung")

        # 2. Unterpunkt: Hintergrund, Entstehung & Warum es funktioniert
        with st.expander("Hintergrund, Entstehung & Warum es funktioniert", expanded=False):
            st.markdown("""
            **Hintergrund & Entstehung:**
            In der klassischen Elektrotechnik stößt man bei komplexeren Netzen schnell an Grenzen, wenn man nur das Ohmsche Gesetz oder einfache Reihen- und Parallelschaltungen nutzt. Um dieses Problem zu lösen, entwickelten Physiker systematische Analyseverfahren. Das Knotenpotentialverfahren nutzt die Knotensatz-Regeln von Kirchhoff in Verbindung mit den Leitwerten der Bauteile, um Netzwerke auf einen einzigen Rechenschritt zu reduzieren.
            
            **Warum funktioniert das Verfahren? (Das physikalische Prinzip):**
            Jede reale Spannungsquelle (bestehend aus einer idealen Quelle und einem Innenwiderstand) kann physikalisch in eine equivalente Stromquelle umgerechnet werden (Norton-Äquivalent). Wenn man mehrere solcher Zweige parallel schaltet, addieren sich die Ströme im Zähler, während sich die Leitwerte ($G = \\frac{1}{R}$) im Nenner ebenfalls aufaddieren. 
            Nach dem Ohmschen Gesetz ist Spannung gleich Strom geteilt durch den Gesamtleitwert ($U = \\frac{I_{\\text{gesamt}}}{G_{\\text{gesamt}}}$). Genau das macht die Millman-Formel: Sie fasst alle parallelen Zweige zu einer einzigen Ersatzspannungsquelle zusammen.
            """)
            st.markdown("**Quelle:** Aufgabensammlung Grundlagen der Elektrotechnik & Lehrgang Netzwerke")

        # 3. Unterpunkt: Theorie, Reinform & Umstellungen
        with st.expander("Theorie, Reinform & Umstellungen", expanded=False):
            st.markdown("""
            **Die mathematische Formel (Satz von Millman):**
            Wenn drei parallele Zweige vorliegen (z.B. zwei Spannungsquellen und ein reiner Lastwiderstand), lautet die Grundformel zur Berechnung des Knotenpotentials bzw. der Ersatzspannung:
            """)
            
            st.markdown("**Reinform:**")
            st.latex(r"U_q = \frac{\frac{U_1}{R_1} + \frac{U_2}{R_2} + \frac{U_3}{R_3}}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}")
            
            st.markdown("**Umgestellte Formen:**")
            st.markdown("- *Berechnung des Teilstroms in einem Zweig:*")
            st.latex(r"I_n = \frac{U_n}{R_n}")
            st.markdown("- *Darstellung unter Verwendung von Leitwerten ($G = \\frac{1}{R}$):*")
            st.latex(r"U_q = \frac{U_1 \cdot G_1 + U_2 \cdot G_2 + U_3 \cdot G_3}{G_1 + G_2 + G_3}")
            
            st.markdown("**Quelle:** Lehrgang Elektrotechnik, Berechnungsverfahren für lineare Netzwerke")

        # 4. Unterpunkt: Statisches Rechenbeispiel
        with st.expander("Klassisches Rechenbeispiel (Schritt für Schritt erklärt)", expanded=False):
            st.markdown("""
            **Gegebene Werte aus der Musteraufgabe:**
            * Spannungsquelle 1: $U_1 = 4{,}5\\text{ V}$, Vorwiderstand $R_1 = 100\\,\Omega$
            * Spannungsquelle 2: $U_2 = 3{,}0\\text{ V}$, Vorwiderstand $R_2 = 100\\,\Omega$
            * Lastwiderstand (3. Zweig ohne eigene Quelle): $R_3 = 50\\,\Omega$
            
            Gesucht ist die an den Hauptknoten anliegende Spannung $U_q$.
            """)
            
            st.markdown("---")
            st.markdown("**Schritt 1: Ströme in den Quellzweigen ermitteln**")
            st.markdown("Wir betrachten jeden aktiven Zweig einzeln als Kurzschlussstrom ($I = \\frac{U}{R}$), um zu sehen, wie viel Strom jede Quelle in das System einspeist:")
            st.latex(r"I_1 = \frac{U_1}{R_1} = \frac{4{,}5\text{ V}}{100\text{ }\Omega} = 0{,}045\text{ A} \quad (45\text{ mA})")
            st.latex(r"I_2 = \frac{U_2}{R_2} = \frac{3{,}0\text{ V}}{100\text{ }\Omega} = 0{,}030\text{ A} \quad (30\text{ mA})")
            
            # Tipp farblich hervorgehoben (Blau)
            st.info("Tipp: Der dritte Zweig hat keine eigene Spannungsquelle (U3 = 0 V), trägt also zum Zähler keinen Strom bei, wirkt aber über seinen Widerstand im Nenner voll mit.")
            
            st.markdown("**Schritt 2: Leitwerte aller parallelen Zweige berechnen und addieren**")
            st.markdown("Der Nenner der Millman-Formel entspricht der Parallelschaltung aller Leitwerte ($G = \\frac{1}{R}$):")
            st.latex(r"G_1 = \frac{1}{100\text{ }\Omega} = 0{,}01\text{ S}, \quad G_2 = \frac{1}{100\text{ }\Omega} = 0{,}01\text{ S}, \quad G_3 = \frac{1}{50\text{ }\Omega} = 0{,}02\text{ S}")
            st.latex(r"G_{\text{gesamt}} = 0{,}01\text{ S} + 0{,}01\text{ S} + 0{,}02\text{ S} = 0{,}04\text{ S}")
            
            st.markdown("**Schritt 3: Zähler durch Nenner teilen**")
            st.markdown("Zum Schluss teilen wir die Summe aller Teilströme durch den Gesamtleitwert:")
            st.latex(r"U_q = \frac{0{,}045\text{ A} + 0{,}030\text{ A}}{0{,}04\text{ S}} = \frac{0{,}075\text{ A}}{0{,}04\text{ S}} = 1{,}875\text{ V}")
            
            # Endergebnis farblich hervorgehoben (Grün)
            st.success("**Endergebnis:** Zwischen den Hauptknoten liegt exakt eine Spannung von **1,875 V** an.")
            st.markdown("**Quelle:** Aufgabensammlung Grundlagen der Elektrotechnik")

    st.markdown("---")

    # Interaktiver Live-Rechner mit dynamischer Neuberechnung
    with st.expander("Interaktiver Live-Rechner: Eigene Werte eingeben & berechnen", expanded=False):
        st.markdown("Verändere hier die Werte für Spannungen und Widerstände. Die Musterlösung und alle Rechenschritte passen sich unten automatisch in Echtzeit an!")

        c1, c2, c3 = st.columns(3)
        with c1:
            u1_in = st.number_input("Spannung U1 (V):", value=4.5, step=0.5, key="kp_u1")
            r1_in = st.number_input("Widerstand R1 (Ohm):", value=100.0, min_value=1.0, step=10.0, key="kp_r1")
        with c2:
            u2_in = st.number_input("Spannung U2 (V):", value=3.0, step=0.5, key="kp_u2")
            r2_in = st.number_input("Widerstand R2 (Ohm):", value=100.0, min_value=1.0, step=10.0, key="kp_r2")
        with c3:
            u3_in = st.number_input("Spannung U3 (V - oft 0):", value=0.0, step=0.5, key="kp_u3")
            r3_in = st.number_input("Widerstand R3 (Ohm):", value=50.0, min_value=1.0, step=10.0, key="kp_r3")

        # Dynamische Berechnung der Zwischenschritte
        i1_dyn = u1_in / r1_in
        i2_dyn = u2_in / r2_in
        i3_dyn = u3_in / r3_in
        zaehler_dyn = i1_dyn + i2_dyn + i3_dyn

        g1_dyn = 1.0 / r1_in
        g2_dyn = 1.0 / r2_in
        g3_dyn = 1.0 / r3_in
        nenner_dyn = g1_dyn + g2_dyn + g3_dyn

        ergebnis_dyn = zaehler_dyn / nenner_dyn if nenner_dyn > 0 else 0.0

        st.markdown("---")
        st.markdown("### **Live-Musterlösung mit deinen Werten:**")
        
        st.markdown("**Schritt 1: Teilströme der Zweige berechnen**")
        st.latex(r"I_1 = \frac{" + str(u1_in) + r"\text{ V}}{" + str(r1_in) + r"\text{ }\Omega} = " + f"{i1_dyn:.4f}" + r"\text{ A}")
        st.latex(r"I_2 = \frac{" + str(u2_in) + r"\text{ V}}{" + str(r2_in) + r"\text{ }\Omega} = " + f"{i2_dyn:.4f}" + r"\text{ A}")
        st.latex(r"I_3 = \frac{" + str(u3_in) + r"\text{ V}}{" + str(r3_in) + r"\text{ }\Omega} = " + f"{i3_dyn:.4f}" + r"\text{ A}")
        st.markdown(f"**Summe aller Teilströme (Zähler):** `{zaehler_dyn:.4f} A`")

        st.markdown("**Schritt 2: Leitwerte addieren (Nenner)**")
        st.latex(r"G_{\text{gesamt}} = \frac{1}{" + str(r1_in) + r"} + \frac{1}{" + str(r2_in) + r"} + \frac{1}{" + str(r3_in) + r"} = " + f"{nenner_dyn:.4f}" + r"\text{ S}")

        st.markdown("**Schritt 3: Endergebnis berechnen**")
        st.latex(r"U_q = \frac{" + f"{zaehler_dyn:.4f}" + r"\text{ A}}{" + f"{nenner_dyn:.4f}" + r"\text{ S}} = " + f"{ergebnis_dyn:.3f}" + r"\text{ V}")

        # Endergebnis im Live-Rechner ebenfalls sauber in Grün
        st.success(f"**Berechnetes Knotenpotential / Ersatzspannung:** `{ergebnis_dyn:.3f} V`")

    st.markdown("---")
def render_kirchhoff():
    st.markdown("### **Die Kirchhoffschen Gesetze im Detail**")
    st.markdown("Grundlegende Werkzeuge zur Analyse und Berechnung verzweigter elektrischer Netzwerke.")
    st.markdown("---")

    # Haupt-Expander für das gesamte Thema
    with st.expander("Inhalt, Theorie & Beispiele anzeigen", expanded=False):
        
        st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>Grundlagen der Netzwerksanalyse</span>", unsafe_allow_html=True)
        st.markdown("")

        # 1. Unterpunkt: Hintergrund & Entstehung
        with st.expander("Hintergrund & Entstehung", expanded=False):
            st.markdown("""
            Die beiden grundlegenden Gesetze wurden im Jahr 1854 von dem deutschen Physiker Gustav Robert Kirchhoff veröffentlicht[cite: 12]. Damals gab es zwar schon das Ohmsche Gesetz, aber sobald Schaltungen komplizierter wurden und sich der Strom in verschiedene Richtungen verzweigte, reichte das einfache Gesetz nicht mehr aus. Kirchhoff knüpfte an die Forschungen von Georg Simon Ohm an und schuf ein mathematisches Fundament, mit dem man auch die verzweigtesten Netze glasklar berechnen kann[cite: 12].
            
            **Warum funktionieren sie? (Die Physik dahinter):**
            * **Knotensatz (1. Regel):** Basiert auf dem Naturgesetz der Erhaltung der elektrischen Ladung. Elektronen sind winzige Teilchen; sie können in einem Kabel weder magisch verschwinden noch aus dem Nichts auftauchen. Was an einer Weggabelung hineinfließt, muss zwingend auch wieder herausfließen[cite: 12].
            * **Maschensatz (2. Regel):** Basiert auf dem Energieerhaltungssatz. Stell dir vor, du läufst in einem geschlossenen Kreis (einer Masche) einmal komplett herum[cite: 12]. Du zählst alle Spannungsquellen (die dir Energie geben) als Plus und alle Spannungsabfälle an den Widerständen (die dir Energie verbrauchen) als Minus zusammen. Wenn du wieder am Startpunkt ankommst, muss die Bilanz exakt bei Null liegen[cite: 12]. Energie geht im System nicht verloren.
            
            **Wann und wo braucht man das?**
            In der Praxis nutzt man diese Gesetze immer dann, wenn man komplexe Schaltungen (wie Steuerungen im Schaltschrank, Industrieanlagen oder elektronische Platinen) berechnen muss, bei denen klassische Reihen- und Parallelschaltungen nicht ausreichen.
            
            **Reales Praxisbeispiel:**
            Stell dir eine Hauptwasserleitung vor, die sich an einer Kreuzung auf drei kleinere Schläuche aufteilt. Es kann logischerweise niemals mehr Wasser aus den drei Schläuchen herauskommen, als vorne an der Kreuzung hineingeflossen ist – das ist genau die Logik des Knotensatzes.
            """)
            st.markdown("**Quelle:** Lehrgang Elektrotechnik 1, Arbeitsblatt Nr. 26: Knotenpunkt- und Maschen-Regel nach Kirchhoff[cite: 12]")

        # 2. Unterpunkt: Knotenpunktregel
        with st.expander("1. Knotenpunkt-Regel (Knotensatz)", expanded=False):
            st.markdown("""
            **Was ist ein Knoten?** 
            Ein Knoten ist schlicht und einfach jede Stelle in einem Stromkreis, an der sich drei oder mehr Leitungen treffen (eine Weggabelung oder Verzweigung)[cite: 12].
            
            **Was besagt die Regel?**
            Die Summe aller Ströme, die in diesen Knoten hineinfließen, ist zu jedem Zeitpunkt exakt so groß wie die Summe aller Ströme, die wieder herausfließen[cite: 12]. Anders ausgedrückt: Wenn man alle Ströme an einem Knoten mit ihrem Vorzeichen addiert (Hineinfließend = positiv, Hinausfließend = negativ), ist das Ergebnis immer genau Null[cite: 12].
            """)
            
            st.markdown("**Reinform:**")
            st.latex(r"\sum_{k=1}^{n} I_k = 0 \quad \text{bzw.} \quad \sum I_{\text{zu}} = \sum I_{\text{ab}}")
            
            st.markdown("**Umgestellte Formen:**")
            st.markdown("- *Summe der zufließenden Ströme:*")
            st.latex(r"I_{\text{zu}} = I_1 + I_2")
            st.markdown("- *Summe der abfließenden Ströme:*")
            st.latex(r"I_{\text{ab}} = I_3 + I_4 + I_5")
            
            st.markdown("**Quelle:** Lehrgang Elektrotechnik 1, Arbeitsblatt Nr. 26: Knotenpunkt- und Maschen-Regel nach Kirchhoff[cite: 12]")

        # 3. Unterpunkt: Maschenregel
        with st.expander("2. Maschen-Regel (Maschensatz)", expanded=False):
            st.markdown("""
            **Was ist eine Masche?** 
            Eine Masche ist jeder geschlossene Weg in einem Schaltplan, den man mit dem Finger abfahren kann, ohne den Stift abzusetzen, und der am Ende wieder zum Startpunkt zurückführt[cite: 12].
            
            **Was besagt die Regel?**
            In jedem geschlossenen Stromkreis ist die Summe aller Teilspannungen gleich Null[cite: 12]. Du legst eine beliebige Umlaufrichtung fest (z. B. im Uhrzeigersinn)[cite: 12]. Jede Spannungsquelle oder jeder Spannungsabfall, die in diese Richtung zeigen, bekommen ein positives Vorzeichen; alles, was entgegen der Richtung zeigt, bekommt ein negatives Vorzeichen[cite: 12].
            """)
            
            st.markdown("**Reinform:**")
            st.latex(r"\sum_{k=1}^{n} U_k = 0")
            
            st.markdown("**Umgestellte Formen:**")
            st.markdown("- *Quellenspannung als Summe der Teilspannungen (Spannungsabfälle):*")
            st.latex(r"U_q = U_{R1} + U_{R2} + U_{R3}")
            st.markdown("- *Auflösung nach einem bestimmten Spannungsabfall:*")
            st.latex(r"U_{R1} = U_q - U_{R2} - U_{R3}")
            
            st.markdown("**Quelle:** Lehrgang Elektrotechnik 1, Arbeitsblatt Nr. 26: Knotenpunkt- und Maschen-Regel nach Kirchhoff[cite: 12]")

        st.markdown("---")
        st.markdown("**Hinweis zu weiteren Regeln:** In der klassischen Elektrotechnik gibt es physikalisch und historisch genau diese zwei Kirchhoffschen Gesetze (Knotensatz und Maschensatz). Es existieren keine weiteren eigenständigen Kirchhoff-Regeln; diese beiden bilden zusammen das vollständige Fundament für die gesamte Netzwerksanalyse.")

    st.markdown("---")

    # Interaktiver Rechner nun ebenfalls als ausklappbarer Expander
    with st.expander("Interaktiver Rechner: Knoten-Check öffnen", expanded=False):
        st.markdown("Teste hier die Summenbildung von zufließenden und abfließenden Strömen an einem Knotenpunkt:")

        col1, col2 = st.columns(2)
        with col1:
            i_zu_1 = st.slider("Zufließender Strom I1 (A):", min_value=0.0, max_value=10.0, value=5.0, step=0.5, key="k_zu_1")
            i_zu_2 = st.slider("Zufließender Strom I2 (A):", min_value=0.0, max_value=10.0, value=3.0, step=0.5, key="k_zu_2")
        with col2:
            i_ab_1 = st.slider("Abfließender Strom I3 (A):", min_value=0.0, max_value=10.0, value=4.0, step=0.5, key="k_ab_1")
            i_ab_2 = st.slider("Abfließender Strom I4 (A):", min_value=0.0, max_value=10.0, value=4.0, step=0.5, key="k_ab_2")

        summe_zu = i_zu_1 + i_zu_2
        summe_ab = i_ab_1 + i_ab_2

        st.markdown("---")
        st.markdown("**Live-Ergebnis am Knoten:**")

        # Getrennte Anzeigefelder für die exakten Werte
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric(label="Summe zufließende Ströme", value=f"{summe_zu:.2f} A")
        with m_col2:
            st.metric(label="Summe abfließende Ströme", value=f"{summe_ab:.2f} A")

        # Visuelle Balken für den direkten optischen Vergleich
        st.markdown("**Optischer Vergleich (Skala bis 20 A):**")
        max_wert = 20.0
        p_zu = min(summe_zu / max_wert, 1.0)
        p_ab = min(summe_ab / max_wert, 1.0)

        st.markdown("Zufließend:")
        st.progress(p_zu)
        st.markdown("Abfließend:")
        st.progress(p_ab)

        st.markdown("---")
        
        if summe_zu == summe_ab:
            st.success("Knotenregel erfüllt: Die Summe der zufließenden Ströme ist exakt gleich der Summe der abfließenden Ströme.")
        else:
            differenz = abs(summe_zu - summe_ab)
            st.error(f"Abweichung von {differenz:.2f} A! Nach dem 1. Kirchhoffschen Gesetz müssen zufließende und abfließende Ströme im Gleichgewicht sein.")

    st.markdown("---")
def render_formelsammlung():
    # Haupttitel ohne Icons
    st.title("Elektrotechnik-Formelsammlung")
    st.markdown("Umfassende Übersicht aller relevanten Formeln für das Techniker-Studium, inklusive Motorentechnik, Reinformen, umgestellten Formen und präzisen Quellenangaben.")

    # Suchfeld für Formeln
    suchbegriff = st.text_input("🔍 Formel oder Stichwort suchen...", "").lower()

    formeln = [
        # --- Gleichstromtechnik ---
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
        # --- Wechselstromtechnik ---
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
        # --- Antriebs- und Motorentechnik ---
        {
            "titel": "Wirkleistung im Drehstromnetz (Symmetrische Last)",
            "kategorie": "Antriebs- und Energietechnik",
            "beschreibung": "Berechnung der elektrischen Wirkleistung eines Dreiphasen-Drehstrommotors (Stern- oder Dreieckschaltung).",
            "reinform": "P = \\sqrt{3} \\cdot U_L \\cdot I_L \\cdot \\cos(\\varphi)",
            "umgestellte_formen": [
                "Leiterstrom: I_L = \\frac{P}{\\sqrt{3} \\cdot U_L \\cdot \\cos(\\varphi)}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 2 (Grundlagen der Drehstromtechnik), S. 40-44"
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
        },
        {
            "titel": "Schlupf (Asynchronmaschine)",
            "kategorie": "Antriebstechnik",
            "beschreibung": "Relative Abweichung der Rotor-Drehzahl von der synchronen Drehfeld-Drehzahl beim Asynchronmotor.",
            "reinform": "s = \\frac{n_s - n}{n_s}",
            "umgestellte_formen": [
                "Rotordrehzahl: n = n_s \\cdot (1 - s)",
                "Synchrone Drehzahl: n_s = \\frac{n}{1 - s}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 6.2 (Der Schlupf des Asynchronmotors), S. 155-158"
        },
        {
            "titel": "Mechanisches Drehmoment eines Motors",
            "kategorie": "Antriebstechnik",
            "beschreibung": "Zusammenhang zwischen abgegebener mechanischer Leistung (P_mech) und Drehzahl (n).",
            "reinform": "M = \\frac{P_{mech}}{2 \\cdot \\pi \\cdot n}",
            "umgestellte_formen": [
                "Mechanische Leistung: P_{mech} = M \\cdot 2 \\cdot \\pi \\cdot n",
                "Praxisformel mit Drehzahl in min^-1: M \\approx 9{,}55 \\cdot \\frac{P_{mech}}{n}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 3 (Drehmoment und Leistung im Antrieb), S. 75-78"
        },
        {
            "titel": "Wirkungsgrad einer elektrischen Maschine",
            "kategorie": "Antriebs- und Energietechnik",
            "beschreibung": "Verhältnis von abgegebener mechanischer (oder elektrischer) Leistung zur zugeführten Leistung.",
            "reinform": "\\eta = \\frac{P_{ab}}{P_{zu}}",
            "umgestellte_formen": [
                "Zugeführte Leistung: P_{zu} = \\frac{P_{ab}}{\\eta}",
                "Abgegebene Leistung: P_{ab} = P_{zu} \\cdot \\eta",
                "Verlustleistung: P_V = P_{zu} - P_{ab}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 3.4 (Verluste und Wirkungsgrad), S. 82-85"
        },
        {
            "titel": "Ankerspannung / Induzierte Spannung (Gleichstrommaschine)",
            "kategorie": "Antriebstechnik",
            "beschreibung": "Spannungsgleichgewicht am Ankerkreis einer Gleichstrommaschine (Motorbetrieb).",
            "reinform": "U = U_i + I_a \\cdot R_a",
            "umgestellte_formen": [
                "Induzierte Spannung: U_i = U - I_a \\cdot R_a",
                "Ankerstrom: I_a = \\frac{U - U_i}{R_a}"
            ],
            "quelle": "Fischer, Heinz: Elektrische Maschinen, Kapitel 5 (Die Gleichstrommaschine), S. 120-125"
        },
        # --- Pneumatik & Fluidtechnik ---
        {
            "titel": "Zylinderkraft (Pneumatik)",
            "kategorie": "Pneumatik / Fluidtechnik",
            "beschreibung": "Berechnung der theoretischen Schubkraft eines pneumatischen Zylinders beim Ausfahren aus Betriebsdruck und Kolbenfläche.",
            "reinform": "F = p \\cdot A",
            "umgestellte_formen": [
                "Betriebsdruck: p = \\frac{F}{A}",
                "Kolbenfläche: A = \\frac{F}{p}"
            ],
            "quelle": "Wächter, Heinrich: Pneumatik – Grundlagen, Komponenten, Anwendungen, Kapitel 3 (Arbeitselemente und Kraftberechnung), S. 45-48"
        },
        {
            "titel": "Volumenstrom in Rohrleitungen",
            "kategorie": "Pneumatik / Fluidtechnik",
            "beschreibung": "Zusammenhang zwischen Strömungsgeschwindigkeit, Rohrquerschnitt und Volumenstrom in fluidtechnischen Systemen.",
            "reinform": "q_v = v \\cdot A",
            "umgestellte_formen": [
                "Strömungsgeschwindigkeit: v = \\frac{q_v}{A}",
                "Querschnittsfläche: A = \\frac{q_v}{v}"
            ],
            "quelle": "Wächter, Heinrich: Pneumatik – Grundlagen, Komponenten, Anwendungen, Kapitel 2 (Strömungslehre in der Pneumatik), S. 22-25"
        },
        # --- Elektrostatik & Kondensator ---
        {
            "titel": "Elektrische Ladung",
            "kategorie": "Elektrostatik",
            "beschreibung": "Berechnung der gespeicherten elektrischen Ladungsmenge auf den Platten eines Kondensators.",
            "reinform": "Q = C \\cdot U",
            "umgestellte_formen": [
                "Kapazität: C = \\frac{Q}{U}",
                "Spannung: U = \\frac{Q}{C}"
            ],
            "quelle": "Hagmann, Gert: Grundlagen der Elektrotechnik, Kapitel 6 (Das elektrische Feld und der Kondensator), S. 135-138"
        },
        {
            "titel": "Elektrische Energie im Kondensator",
            "kategorie": "Elektrostatik",
            "beschreibung": "Berechnung der im elektrischen Feld eines geladenen Kondensators gespeicherten Energie.",
            "reinform": "W_{el} = \\frac{1}{2} \\cdot C \\cdot U^2",
            "umgestellte_formen": [
                "Kapazität: C = \\frac{2 \\cdot W_{el}}{U^2}",
                "Spannung: U = \\sqrt{\\frac{2 \\cdot W_{el}}{C}}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 1, Kapitel 7 (Das elektrische Feld), S. 180-184"
        },
        # --- Elektromagnetismus & Spulen ---
        {
            "titel": "Magnetischer Fluss",
            "kategorie": "Elektromagnetismus",
            "beschreibung": "Berechnung des magnetischen Flusses durch eine gegebene Fläche bei konstanter magnetischer Flussdichte.",
            "reinform": "\\Phi = B \\cdot A",
            "umgestellte_formen": [
                "Magnetische Flussdichte: B = \\frac{\\Phi}{A}",
                "Fläche: A = \\frac{\\Phi}{B}"
            ],
            "quelle": "Hagmann, Gert: Grundlagen der Elektrotechnik, Kapitel 7 (Das magnetische Feld), S. 165-168"
        },
        {
            "titel": "Magnetische Energie in der Spule",
            "kategorie": "Elektromagnetismus",
            "beschreibung": "Berechnung der im Magnetfeld einer stromdurchflossenen Spule gespeicherten Energie.",
            "reinform": "W_{mag} = \\frac{1}{2} \\cdot L \\cdot I^2",
            "umgestellte_formen": [
                "Induktivität: L = \\frac{2 \\cdot W_{mag}}{I^2}",
                "Stromstärke: I = \\sqrt{\\frac{2 \\cdot W_{mag}}{L}}"
            ],
            "quelle": "Albach, Manfred: Grundlagen der Elektrotechnik 1, Kapitel 8 (Das elektromagnetische Feld), S. 210-214"
        },
        # --- Netz- und Leitungstechnik ---
        {
            "titel": "Spannungsfall auf einer elektrischen Leitung",
            "kategorie": "Leitungstechnik / Anlagenbau",
            "beschreibung": "Berechnung des Spannungsverlusts auf einer einfachen Hin- und Rückleitung bei ohmscher Belastung.",
            "reinform": "\\Delta U = 2 \\cdot I \\cdot l \\cdot \\frac{1}{\\kappa \\cdot A}",
            "umgestellte_formen": [
                "Leiterquerschnitt: A = \\frac{2 \\cdot I \\cdot l}{\\kappa \\cdot \\Delta U}"
            ],
            "quelle": "Measures, R. / Tabellenbuch Elektrotechnik, Abschnitt Kabel und Leitungen / Spannungsfall, S. 98-100"
        },
        # --- Regelungstechnik ---
        {
            "titel": "Zeitkonstante des RC-Gliedes",
            "kategorie": "Regelungs- und Systemtechnik",
            "beschreibung": "Maß für die Trägheit des Lade- und Entladevorgangs einer Reihenschaltung aus Widerstand und Kondensator.",
            "reinform": "\\tau = R \\cdot C",
            "umgestellte_formen": [
                "Widerstand: R = \\frac{\\tau}{C}",
                "Kapazität: C = \\frac{\\tau}{R}"
            ],
            "quelle": "Föllinger, Otto: Regelungstechnik – Einführung in die Methoden und ihre Anwendung, Kapitel 4 (Zeitverhalten von Gliedern), S. 65-68"
        }
    ]

    gefilterte_formeln = [
        f for f in formeln 
        if suchbegriff in f["titel"].lower() or suchbegriff in f["beschreibung"].lower() or suchbegriff in f["kategorie"].lower()
    ]

    st.markdown("---")

    if not gefilterte_formeln:
        st.warning("Keine passenden Formeln gefunden.")
    
    # Jede Formel wird nun in einem sauberen Expander (Ein-/Ausklappen) dargestellt
    for f in gefilterte_formeln:
        with st.expander(f"{f['titel']} — [{f['kategorie']}]"):
            
            # Kategorie im schicken Lilaton via HTML-Badge
            st.markdown(f"*Kategorie:* <span style='color: #b19cd9; font-weight: bold; background-color: rgba(177, 156, 217, 0.15); padding: 2px 8px; border-radius: 4px;'>{f['kategorie']}</span>", unsafe_allow_html=True)
            
            st.markdown(f"**Anwendungsbereich / Erläuterung:** {f['beschreibung']}")
            
            st.markdown("**Reinform:**")
            st.latex(f["reinform"])
            
            st.markdown("**Umgestellte Formen:**")
            for form in f["umgestellte_formen"]:
                parts = form.split(": ")
                bezeichnung = parts[0]
                mathtext = parts[1]
                st.markdown(f"- *{bezeichnung}:*")
                st.latex(mathtext)
                
            st.markdown(f"**Quelle:** {f['quelle']}")
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
    st.markdown("Wähle hier die verschiedenen Berechnungsmethoden für elektrische Netzwerke aus.")
    
    # Hier rufen wir jetzt unsere neue, saubere Funktion für die Kirchhoffschen Gesetze auf:
    render_kirchhoff()
    render_knotenpotential()
    render_maschenstromverfahren()
    render_zweipoltheorie()
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
        