# Preprocess INEGI 2020 Census

This script consolidates the census CSVs into a single DataFrame. The script derives a "cvegeo" which is useful to do AGEB-level join operations.

The ["Censo de Población y Vivienda 2020"](https://inegi.org.mx/programas/ccpv/2020/#Microdatos) tabulates sociodemographic indicators across Mexico at the AGEB level. AGEBS are the minimal geographic observational unit at which [INEGI](https://inegi.org.mx/) reports indicators - these can be considered analogous to USA's Census Block Groups.

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt

## Run

    python3 -m src.run
