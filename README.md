## a 2022-es OGY választások ellenzéki szavazatszámlálóinak a megbízólevelei

Ez a script ebben a formában a GCP Vertex AI notebookjában fut.

- **/src/datagen.ipynb:** tesztadat generálás, hogy lehessen a szkriptet sok adattal megtolni még a beosztás befejezése előtt
- **/src/docugen.ipynb:** dokumentumok legenerálása sablon és tesztadat alapján: Jinja > ~500 html > LibreOffice > pdf > zip
- **/pub/500_megbizo_html.zip:** a legenerált TESZT pdf-ek tömörítve, aláírásra várva
- **/input/user_testdata.json:** a legenerált tesztadat, OEVK-k szintjéig valós, utána fiktív, és 30 helyett csak 6 település per OEVK, 1-5 szavazókör per település, mert 500 dokumentummal tesztelünk, nem 3200-al
