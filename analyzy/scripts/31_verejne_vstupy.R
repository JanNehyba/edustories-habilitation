# 31_verejne_vstupy.R: vytvoří dvě veřejné vstupní tabulky doprovodného repozitáře,
# které čtou notebooky 20 a 30, ale současná linka je nevytvářela (zjištěno při reprodukci
# 12. 10. 2026; kód převzat z notebooků 20 a 30 ve stavu commitu 1927f4f).
#
#   data/processed/srovnani_k1_llm.csv      Studie 2: id + kód člověka a modelu (bez textů)
#   data/processed/kap7_hodnoceni_pseudo.csv Studie 3: hodnocení s pseudonymy anotátorek A1–A6
#
# Vstupy (jen čtení): data/raw/.../srovnani.csv, data/externi/osf-aied-ndtkz/... .
# Skript nevypisuje žádné hodnoty ani jména. Pseudonymy se přidělují podle abecedního
# pořadí jmen v řazení nezávislém na locale (method = "radix").
#
# Užití (z adresáře habilitace-2):  Rscript analyzy/scripts/31_verejne_vstupy.R [výstupní_adresář]

args <- commandArgs(trailingOnly = TRUE)
OUT <- if (length(args) >= 1) args[[1]] else file.path("data", "processed")
dir.create(OUT, showWarnings = FALSE, recursive = TRUE)
# zápis s konci řádků LF na všech platformách (binární spojení), aby soubory byly bajtově stejné
zapis <- function(x, soubor) {
  con <- file(file.path(OUT, soubor), "wb"); on.exit(close(con))
  write.csv(x, con, row.names = FALSE)
}

# Studie 2: archivované srovnání člověk × model
SROV <- file.path("data", "raw", "k1-kvalitativni-kodovani-2023-24", "05-llm-klasifikace-capv", "srovnani.csv")
srov <- read.csv(SROV, sep = ";", encoding = "UTF-8")
zapis(srov, "srovnani_k1_llm.csv")

# Studie 3: autoritativní data OSF, jen analytické sloupce, jména → A1–A6
CSV <- file.path("data", "externi", "osf-aied-ndtkz", "anotace_final_data_bezdiakritiky.csv")
KEEP <- c("Id", "anotator_name", "Otazka", "Hodnoceni", "Reseni_gen_AI",
          "Pristup.I", "Pristup.II", "Pristup.III")
df <- read.csv(CSV, header = TRUE, sep = ",", fileEncoding = "cp1250")
jmena <- sort(unique(df$anotator_name), method = "radix")
pseudo <- setNames(sprintf("A%d", seq_along(jmena)), jmena)
df$anotator_name <- unname(pseudo[df$anotator_name])
df <- df[, KEEP]
zapis(df, "kap7_hodnoceni_pseudo.csv")

cat("31_verejne_vstupy: zapsáno", nrow(srov), "+", nrow(df), "řádků do", OUT, "\n")
