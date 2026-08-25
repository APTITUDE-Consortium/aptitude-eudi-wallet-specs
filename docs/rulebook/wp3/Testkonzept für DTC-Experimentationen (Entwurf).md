# Testkonzept für DTC-Experimentationen (Entwurf)

## Einführung

Dieses Dokument richtet sich an Testmanager, Entwickler, Tester, Product Owner und Stakeholder (z. B. Airlines, Border Authorities, EUDIW-Anbieter).

Das Testkonzept gilt für die agile Entwicklung und Validierung der DTC-Experimentationen im Rahmen von WP3. Es ist im Zusammenspiel mit der verlinkten agilen Teststrategie zu gebrauchen.

Spezifische Abweichungen von der agilen Teststrategie:

- Keine White Box Tests geplant (Fokus auf Black Box und Systemtests).
- Test Engineer übernimmt Aufgaben des Test Managers (Rolle nicht vorgesehen).
- Integration von externen Stakeholdern (z. B. Airlines, Border Authorities) in Testaktivitäten.

Das Projekt umfasst die Entwicklung und Validierung von DTC-Experimentationen im Rahmen von WP3. Die Testaktivitäten umfassen alle in Deliverable-D32.md beschriebenen Szenarien.

## Grundlagen

Testbasis:

- Deliverable-D32.md (funktionale und technische Spezifikationen).
- EUDIW-Spezifikationen und -Richtlinien.
- DTC-Rulebook (dtc-rulebook.md).
- Business Rules aus Deliverable-D32.md (z. B. BR-1.1 bis BR-12.6).

Übersicht über das Gesamtsystem:

Modularer Aufbau mit gemeinsamen technischen Baselines und unterschiedlichen funktionalen Implementierungen. Integration von EUDIW, DTC-VC, Relying Parties (Airlines, Border Authorities, etc.). Use Cases: DTC-Generierung, Flight Booking, Loyalty Programme, Visa/DTA, Border Control, etc.

## Testobjekte

Die Testobjekte umfassen:

- DTC-VC-Generierung (EUDIW-Integration).
- Flight Booking System (Airlines).
- Loyalty Programme Systeme.
- Visa/DTA-Application Portale.
- Border Control Systeme (Pre-Screening, Border Crossing).
- Airport Check-in Kioske.
- Mobile Apps (EUDIW, Airlines, Border Authorities).

## Testaufgaben/Testmanagement

Agile Testteams mit Entwicklern, Testern und Stakeholdern. Regelmäßige Abstimmungen mit Projektmanagement und Stakeholdern.

## Rollen und Verantwortung

Rollen:

- Projekleiter: Steuerung des Gesamtprojekts über die einzelnen Services und Konfigurationen, Sicherstellung der Testeingangskriterien.
- Testmanager: Planung, Konzeption, Überwachung und Eskalation.
- Tester: Testfallspezifikation, Durchführung, Bericht und Freigabe.

Zuständigkeiten:

- Testkonzept: Testmanager.
- Testfallkonzeption: Tester, Entwickler.
- Testdurchführung: Tester.
- Regressionstests, Testautomatisierung: Tester, Entwickler.
- Testmanagement: Testmanager.

## Testinfrastruktur/Anforderungen an die Testumgebung

Werkzeuge und Simulatoren:

- Testautomatisierungs-Tools (z. B. Selenium, Appium).
- Fehlermanagement-Tools (z. B. Jira, Bugzilla).
- Testtools für Durchführung (z. B. Postman, SoapUI).
- Simulatoren für NFC-Passport-Reading, Biometrie, Liveness Detection.

Software:

- EUDIW (Testversion).
- DTC-VC-Generierungstools.
- Airlines-Booking-Systeme (Mocks).
- Border Control Systeme (Mocks).
- Mobile Apps (Testversionen).

Hardware:

- Smartphones (verschiedene Modelle und Betriebssysteme).
- NFC-Reader für Passport-Reading.
- Biometrie-Scanner (Facial Recognition).
- Airport Check-in Kioske (Mocks).

Mocks:

- Mocks für EUDIW, DTC-VC, Airlines, Border Authorities.
- Mocks für Backend-Systeme (z. B. Visa/DTA-Application Portale).

Logging:

Logging der Testaktivitäten (Testartefakte, Protokolle). Aufbewahrung von Testartefakten für 6 Monate.

## Zeitplan

Meilensteine:

- MS1 (Testvorbereitung): Testkonzept, Testfallkonzeption, Testumgebung setup.
- MS2 (Testdurchführung): Systemtests, Integrationstests, End-to-End-Tests.
- MS3 (Testabschluss): Regressionstests, Testautomatisierung, Testbericht.

Abstimmungen:

Regelmäßige Abstimmungen zwischen Testmanagement und Projektmanagement. Feedbackschleifen mit Stakeholdern (Airlines, Border Authorities, etc.).

## Ressourcen

Personelle Ressourcen:

- Testmanager (1).
- Tester (2-3).
- Entwickler (2-3, Unterstützung bei Testautomatisierung).
- Stakeholder (Airlines, Border Authorities, etc., Support und Feedback).

Schulungen:

- Schulungen für Tester und Entwickler (z. B. EUDIW, DTC-VC, Testtools).
- Schulungen für Stakeholder (z. B. Testumgebung, Testprozesse).

## Risiken

Risiken und Mitigationsmaßnahmen:

- Verzögerungen bei Lieferungen: Regelmäßige Abstimmungen mit Stakeholdern, Pufferzeiten einplanen.
- Nicht ausreichend Personal: Priorisierung von Testaktivitäten, externe Unterstützung (z. B. Testdienstleister).
- Krankheitsbedingte Ausfälle: Backup-Plan für kritische Rollen.
- Prioritäten ändern sich: Flexible Anpassung des Testplans, regelmäßige Reviews.
- Technische Herausforderungen: Early Testing, Mocks und Simulatoren nutzen, enge Zusammenarbeit mit Entwicklern.

## Anlageverzeichnis und Referenzen

Externe Referenzen:

- Deliverable-D32.md (funktionale und technische Spezifikationen).
- EUDIW-Spezifikationen und -Richtlinien.
- DTC-Rulebook (dtc-rulebook.md).
- ISO/IEC/IEEE 29119-1 (Concepts & Definitions).
- ISO/IEC/IEEE 29119-3 (Test Documentation).
- PD ISO/IEC TR 29119-6:2021 (Guidelines for the use of ISO/IEC/IEEE 29119 in agile projects).

Interne Referenzen:

- bdr Prozesssystem (ADONIS).
- Agile Teststrategie (freigegebene Version v30).