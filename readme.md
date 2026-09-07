A repozitórium a "Közgyűjteményi kulturális adatok modellezése, vizualizációja és elemzése digitális bölcsészeti megközelítésben" c. doktori disszertáció adatvizualizációit, és az adatvizualizációk előállításához szükséges, adatokkal kapcsolatos műveletek scriptjeit tartalmazza.

Szerző: Horváth Dániel
Egyetem: Moholy-Nagy Művészeti Egyetem, Doktori Iskola, Művészettudomány (designelmélet) PhD, Designkltúra-tudományi tagozat
Hely és idő: Budapest, 2026. augusztus
Témavezetők: Ruttkay Zsófia PhD habil., Maróthy Szilvia PhD

A repozitórium az alábbi szerkezetben tárolja a doktori kutatás mellékleteként közölt fájlokat.
1. scripts 
A dolgozat. 3 fejezetében ("Közgyűjteményi rekordokból tudásmodell: A Hét és a Nyugat folyóiratok adatainak rendszere") bemutatott adatmodellezési aljárás során alkalmazott scripteket tartalmazza. Az egyes scriptek működéséről dokumentáció olvasható a scriptek elején.
- A 'system_prompts' almappa három rendszerutasítást tartalmaz. Ezek a disszertációban ismertetett módon az MTA kézirattárának adataid egységesítették az elvárt adatszerkezethez.
- A 'logic_gate.ipynb' jupyter notebook feájl scriptek láncolatát tartalmazza, mely segítségével a PIM OPAC felületéről lekérdezett nyers XML fájlok hozzáilleszthetőek voltak az adatsémához, és a korábban összegyűjtött rekordokhoz anélkül, hogy duplikáció keletkezne.
- A 'count_weight.py' az összegűjtött kapcsolatokhoz tartozó csomópontok súlyát számolja ki.

2. structured data
- A 'gephi_edges.xlsx' és a 'gephi_nodes.xlsx' a teljes, adatséma szerint strukturált adathalmazt tartalmazza. Ezekben megtalálható az összes összegyűjtött, 1915 előtti kapcsolat és a szereplők, akik között létrejöttek a kapcsolatok. A két fájl gephi-be történő beolvasásával a hálózatvizualizáció reprodukálható.
- A 'gephi_aggregated_edges.xlsx' fájl a disszertáció 4.2 ("A hálózati modell kiindulási helyezete") fejezet proveniencia vizsgálataihoz használt adatmodellt tartalmazzák. A fájlban található provenienciákat a disszertáció 4/1. ábrája mutatja.
- A 'gephi_nodes_enriched_jobs.xlsx' fájl a 'gephi_nodes.xlsx' fájl csomópontjainak PIM-névtér azonosítója alapján lekérdezett szereplők foglalkozásait tartalmazza. Tartalmazában ugyan az, mint a 'gephi_nodes.xlsx', kiegészítve foglalkozási kategóriákkal.

3. visualisations
A mappa a disszertációban található adatvizualizációk SVG formátumú fájljait tartalmazza. A mappa két almappája a dolgozat fejezetei alapján lettek elnevezve: a '4._a_hálózat_elemzése' mappa a disszertáció 4., "A hálózat elemzése" c. fejezetének adatvizualizációit tartalmazza, a fejezetben látható sorszámozást konvenvencionálisan átvéve. A 'mellekletek' mappa a dolgozat mellékleteit tartalmazza, szintén az ott látható sorszámozást követve.