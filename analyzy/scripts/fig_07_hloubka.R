# Hloubkové figury kapitoly 7 (Studie 3): forest reliability α (K2, 4 dimenze)
# a forest CLMM (poměry šancí, log osa). Hodnoty VÝHRADNĚ z manifestu
# kap7_k2_shoda_cisla.csv (notebook 30).

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

# ── Obrázek: reliabilita hodnocení — ordinální α podle dimenzí (95% CI) ──
al <- do.call(rbind, lapply(names(DIMY), function(d) {
  data.frame(dim = DIMY[[d]],
             a = val(paste0("alpha_ord_final_", d)),
             lo = val(paste0("alpha_ci_lo_", d)),
             hi = val(paste0("alpha_ci_hi_", d)))
}))
al$dim <- factor(al$dim, levels = rev(unname(DIMY)))
p1 <- ggplot(al, aes(a, dim)) +
  geom_vline(xintercept = c(0.667, 0.8), linetype = c("dashed", "dotted"),
             color = GREY_TEXT, linewidth = 0.35) +
  geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.15,
                 color = MUNI_BLUE, linewidth = 0.7) +
  geom_point(color = MUNI_BLUE, size = 3) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2),
                     labels = function(x) format(x, decimal.mark = ",")) +
  labs(x = "Krippendorffovo ordinální α (95% CI)", y = NULL) + theme_book_h()
save_book_fig(file.path(FIG, "kap7_alpha.png"), p1, width = 7.5, height = 2.8)

# ── Obrázek: CLMM — poměry šancí pro zdroj=učitel (log osa, 95% Wald CI) ──
or_ <- do.call(rbind, lapply(names(DIMY), function(d) {
  data.frame(dim = DIMY[[d]],
             or = val(paste0("clmm_or_ucitel_", d)),
             lo = val(paste0("clmm_or_ci_lo_", d)),
             hi = val(paste0("clmm_or_ci_hi_", d)))
}))
or_$dim <- factor(or_$dim, levels = rev(unname(DIMY)))
p2 <- ggplot(or_, aes(or, dim)) +
  geom_vline(xintercept = 1, linetype = "dashed", color = GREY_TEXT) +
  geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.15,
                 color = MUNI_BLUE, linewidth = 0.7) +
  geom_point(color = MUNI_BLUE, size = 3) +
  scale_x_log10(breaks = c(0.05, 0.1, 0.25, 0.5, 1, 2, 5),
                labels = function(x) format(x, decimal.mark = ",", drop0trailing = TRUE)) +
  annotate("text", x = 0.06, y = 4.42, label = "vyšší hodnoty u AI",
           size = 2.9, family = "Helvetica", color = GREY_TEXT, hjust = 0) +
  annotate("text", x = 1.15, y = 4.42, label = "vyšší hodnoty u učitelů",
           size = 2.9, family = "Helvetica", color = GREY_TEXT, hjust = 0) +
  labs(x = "poměr šancí pro zdroj = učitel (log. osa, 95% CI)", y = NULL) +
  theme_book_h() + coord_cartesian(clip = "off")
save_book_fig(file.path(FIG, "kap7_clmm.png"), p2, width = 7.5, height = 2.9)

cat("OK: kap7_alpha, kap7_clmm →", FIG, "\n")
