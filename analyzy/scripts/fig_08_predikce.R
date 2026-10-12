# Figura oddílu 8.6: predikce dopadu jazykovým modelem.
# Hodnoty VÝHRADNĚ z manifestu kap8_predikce_cisla.csv (zapisuje ho skript
# 29_predikce_offline.py z odpovědí modelů v data/processed/k3_predikce_raw.csv,
# které pořídil běh 26_k3_predikce_llm.py). Výstup (vystupy/obrazky/): kap8_predikce {png,pdf}.
# Barvy: lidé = MUNI modrá (odstíny K3), model = PdF oranžová (GRAFICKY-MANUAL: AI = oranžová).

# ── Parametry ────────────────────────────────────────────────────────────────
# Primární model (v grafu nahoře). Manifest kap8_predikce_cisla.csv pro něj klíč nemá,
# proto je zapsán zde. Plyne z výběru modelu na vývojové množině (kritérium: nejvyšší
# vyvážená přesnost; výsledky v analyzy/vystupy/predikce/vysledky_dev_zero_shot.csv,
# záznam v PLAN.md z 9. 9. 2026; popis v oddílu 8.6). Při jiném výběru změnit zde.
PRIMARNI_MODEL <- "kimi_k3"
# Názvy modelů v grafu: klíče manifestu nesou slug (tečka → podtržítko), proto se
# mapují výslovně, shodně s Tabulkou 8.4 (glm-5.3, ne glm-5-3). Neznámý model = chyba.
JMENA <- c(kimi_k3 = "kimi-k3", glm_5_3 = "glm-5.3")

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
TAB <- normalizePath(file.path(SCR, "..", "..", "vystupy", "tabulky"), mustWork = FALSE)
man <- read.csv(file.path(TAB, "kap8_predikce_cisla.csv"), encoding = "UTF-8")
val <- function(k) { v <- man$value[man$metric == k]; if (length(v) != 1) NA_real_ else v }
cz <- function(x) format(x, decimal.mark = ",")

# modely = všechny, které mají v manifestu klíče predikce_<model>_zero_shot_*;
# který z nich je primární, určuje parametr PRIMARNI_MODEL výše (ne pořadí klíčů)
modely <- unique(sub("^predikce_(.+)_zero_shot_.*$", "\\1",
                     grep("_zero_shot_a12_bal_acc$", man$metric, value = TRUE)))
stopifnot(length(modely) >= 1)
chybi <- setdiff(modely, names(JMENA))
if (length(chybi) > 0) stop("Model bez názvu pro graf (doplň JMENA): ", paste(chybi, collapse = ", "))
prim <- PRIMARNI_MODEL
stopifnot(prim %in% modely)
# výchozí srovnání (hádání většinové třídy): odsud začínají vodorovné úsečky
baze <- val("predikce_majorita_bal_acc")
stopifnot(!is.na(baze))

# ── panel A: vyvážená přesnost modelu proti majoritě a lidskému stropu ─────────
poradi <- c(prim, setdiff(modely, prim))   # primární model nahoře
radky <- do.call(rbind, lapply(poradi, function(m) {
  nm <- JMENA[[m]]
  r <- data.frame(
    co = paste0("model ", nm),
    ref = c("vůči A12", "vůči A2", "vůči shodě obou"),
    bal = c(val(paste0("predikce_", m, "_zero_shot_a12_bal_acc")),
            val(paste0("predikce_", m, "_zero_shot_a2_bal_acc")),
            val(paste0("predikce_", m, "_zero_shot_konsenzus_bal_acc"))),
    typ = "model")
  fs <- val(paste0("predikce_", m, "_few_shot_konsenzus_bal_acc"))
  if (!is.na(fs)) r <- rbind(r, data.frame(
    co = paste0("model ", nm, " s příklady"), ref = "vůči shodě obou", bal = fs, typ = "model"))
  r
}))
radky <- rbind(radky,
  data.frame(co = "shoda dvou anotátorek", ref = "A12 vůči A2",
             bal = val("predikce_clovek_clovek_bal_acc"), typ = "lidé"),
  # vyvážená přesnost konstantní předpovědi nezávisí na referenci; počítá se vůči A12
  # (29_predikce_offline.py). „Báze“ je kalk z baseline, v knize „výchozí srovnání“ (G6-023).
  data.frame(co = "hádání většinové třídy", ref = "vůči A12",
             bal = baze, typ = "výchozí srovnání"))
radky <- radky[!is.na(radky$bal), ]
radky$typ <- factor(radky$typ, levels = c("výchozí srovnání", "lidé", "model"))  # pořadí panelů
radky$lab <- factor(paste0(radky$co, " (", radky$ref, ")"),
                    levels = rev(paste0(radky$co, " (", radky$ref, ")")))
pA <- ggplot(radky, aes(100 * bal, lab, color = typ, shape = typ)) +
  geom_segment(aes(xend = 100 * bal, yend = lab), x = 100 * baze, linewidth = 0.7,
               color = GREY_LINE) +
  geom_point(size = 3.4) +
  scale_color_manual(values = c(model = PED_ORANGE, `lidé` = MUNI_BLUE,
                                `výchozí srovnání` = GREY_TEXT), guide = "none") +
  scale_x_continuous(limits = c(0, 100), labels = function(x) paste0(cz(x), " %")) +
  scale_shape_manual(values = c(model = 16, `lidé` = 17, `výchozí srovnání` = 15),
                     guide = "none") +
  labs(x = "vyvážená přesnost / shoda (odlišné úlohy)", y = NULL) +
  facet_grid(typ ~ ., scales = "free_y", space = "free_y",
             labeller = labeller(typ = c(`výchozí srovnání` = "výchozí\nsrovnání",
                                         `lidé` = "lidé", model = "model"))) +
  theme_book_h() +
  theme(strip.text.y = element_text(angle = 0, hjust = 0))   # vodorovně: delší popis se vejde
save_book_fig(file.path(FIG, "kap8_predikce.png"), pA, width = 8, height = 5)
cat("OK: kap8_predikce →", FIG, "\n")
