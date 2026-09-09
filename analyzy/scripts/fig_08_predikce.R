# Figura oddílu 8.6: predikce dopadu jazykovým modelem.
# Hodnoty VÝHRADNĚ z manifestu kap8_predikce_cisla.csv (skript 26_k3_predikce_llm.py);
# matice záměn z data/processed/k3_predikce_raw.csv (bez textů kazuistik).
# Výstup (vystupy/obrazky/): kap8_predikce {png,pdf}.
# Barvy: lidé = MUNI modrá (odstíny K3), model = PdF oranžová (GRAFICKY-MANUAL: AI = oranžová).

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
TAB <- normalizePath(file.path(SCR, "..", "..", "vystupy", "tabulky"), mustWork = FALSE)
PROC <- normalizePath(file.path(SCR, "..", "..", "data", "processed"), mustWork = FALSE)
man <- read.csv(file.path(TAB, "kap8_predikce_cisla.csv"), encoding = "UTF-8")
val <- function(k) { v <- man$value[man$metric == k]; if (length(v) != 1) NA_real_ else v }
cz <- function(x) format(x, decimal.mark = ",")

# primární model = ten, jehož klíče jsou v manifestu jako první (běh 26 je řadí)
modely <- unique(sub("^predikce_(.+)_zero_shot_.*$", "\\1",
                     grep("_zero_shot_a12_bal_acc$", man$metric, value = TRUE)))
stopifnot(length(modely) >= 1)
prim <- modely[1]

# ── panel A: vyvážená přesnost modelu proti majoritě a lidskému stropu ─────────
poradi <- c(prim, setdiff(modely, prim))   # primární model nahoře
radky <- do.call(rbind, lapply(poradi, function(m) {
  nm <- gsub("_", "-", m)
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
  data.frame(co = "hádání většinové třídy", ref = "báze",
             bal = val("predikce_majorita_bal_acc"), typ = "báze"))
radky <- radky[!is.na(radky$bal), ]
radky$lab <- factor(paste0(radky$co, " (", radky$ref, ")"),
                    levels = rev(paste0(radky$co, " (", radky$ref, ")")))
pA <- ggplot(radky, aes(100 * bal, lab, color = typ)) +
  geom_segment(aes(x = 100 / 3, xend = 100 * bal, yend = lab), linewidth = 0.7,
               color = GREY_LINE) +
  geom_point(size = 3.4) +
  scale_color_manual(values = c(model = PED_ORANGE, `lidé` = MUNI_BLUE, `báze` = GREY_TEXT),
                     guide = "none") +
  scale_x_continuous(limits = c(0, 100), labels = function(x) paste0(cz(x), " %")) +
  labs(x = "vyvážená přesnost (báze hádání = 33,3 %)", y = NULL) +
  theme_book_h()
save_book_fig(file.path(FIG, "kap8_predikce.png"), pA, width = 8, height = 3.2)
cat("OK: kap8_predikce →", FIG, "\n")
