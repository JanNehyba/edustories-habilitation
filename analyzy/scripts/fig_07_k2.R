# Figury kapitoly 7 (Studie 3): srovnání AI vs. učitel na 4 dimenzích.
# Hodnoty VÝHRADNĚ z manifestu kap7_k2_shoda_cisla.csv.
# Výstup: kap7_prumery.{png,pdf} (dumbbell), kap7_lmm_efekty.{png,pdf} (forest).

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
dir.create(FIG, showWarnings = FALSE, recursive = TRUE)
man <- read.csv(file.path(SCR, "..", "..", "vystupy", "tabulky", "kap7_k2_shoda_cisla.csv"),
                encoding = "UTF-8")
val <- function(k) man$value[man$metric == k]

DIMY <- c(vhodnost = "vhodnost",
          reaktivni = "reaktivní–proaktivní",
          humanisticke = "humanistická–behaviorální",
          systemove = "systémová–situační")

# ── Obrázek 7.1: průměrná hodnocení podle zdroje (dumbbell, učitel vs AI) ──
prum <- do.call(rbind, lapply(names(DIMY), function(d) {
  data.frame(dim = DIMY[[d]],
             zdroj = c("AI", "Učitel"),
             m = c(val(paste0("mean_AI_", d)), val(paste0("mean_teacher_", d))))
}))
prum$dim <- factor(prum$dim, levels = rev(unname(DIMY)))
p1 <- ggplot(prum, aes(m, dim)) +
  geom_line(aes(group = dim), color = GREY_LINE, linewidth = 1.1) +
  geom_vline(xintercept = 0, linetype = "dashed", color = GREY_TEXT) +
  geom_point(aes(color = zdroj), size = 3.4) +
  scale_color_manual(values = PAL_ZDROJ, name = NULL) +
  scale_x_continuous(limits = c(-2, 2), breaks = -2:2,
                     labels = function(x) format(x, decimal.mark = ",")) +
  labs(x = "průměrné hodnocení (−2 až +2)", y = NULL) +
  theme_book_h() + theme(legend.position = "top")
save_book_fig(file.path(FIG, "kap7_prumery.png"), p1, width = 7.5, height = 3.4)

# ── Obrázek 7.2: efekty LMM (rozdíl učitel − AI, 95% CI) ──
ef <- do.call(rbind, lapply(names(DIMY), function(d) {
  data.frame(dim = DIMY[[d]],
             b = val(paste0("lmm_b1_ucitel_", d)),
             lo = val(paste0("lmm_b1_ci_lo_", d)),
             hi = val(paste0("lmm_b1_ci_hi_", d)))
}))
ef$dim <- factor(ef$dim, levels = rev(unname(DIMY)))
p2 <- ggplot(ef, aes(b, dim)) +
  geom_vline(xintercept = 0, linetype = "dashed", color = GREY_TEXT) +
  geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.16,
                 color = MUNI_BLUE, linewidth = 0.8) +
  geom_point(color = MUNI_BLUE, size = 3) +
  scale_x_continuous(labels = function(x) format(x, decimal.mark = ",")) +
  labs(x = "rozdíl učitel − AI v bodech škály (LMM, 95% CI)",
       y = NULL) +
  theme_book_h()
save_book_fig(file.path(FIG, "kap7_lmm_efekty.png"), p2, width = 7.5, height = 3.2)

cat("OK: kap7_prumery + kap7_lmm_efekty →", FIG, "\n")
