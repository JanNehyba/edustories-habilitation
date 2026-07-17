# Figury kapitoly 6 (Studie 2): shoda člověk × model po kategoriích,
# konfuzní matice a forest reliability (α lidí, κ člověk×model).
# Vstupy VÝHRADNĚ z vystupy/tabulky/ (CSV + manifest z notebooku 20).

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
TAB <- normalizePath(file.path(SCR, "..", "..", "vystupy", "tabulky"), mustWork = FALSE)
dir.create(FIG, showWarnings = FALSE, recursive = TRUE)
man <- read.csv(file.path(TAB, "kap6_kodovani_cisla.csv"), encoding = "UTF-8")
val <- function(k) man$value[man$metric == k]

# ── Obrázek: shoda modelu s člověkem po kategoriích (n = počet dle člověka) ──
pk <- read.csv(file.path(TAB, "kap6_shoda_kategorie.csv"), encoding = "UTF-8")
pk <- pk[order(pk$shoda), ]
pk$kategorie <- factor(pk$kategorie, levels = pk$kategorie)
p1 <- ggplot(pk, aes(shoda, kategorie)) +
  geom_col(fill = MUNI_BLUE, width = 0.7) +
  geom_text(aes(label = paste0(sprintf("%.0f", 100 * shoda), " % (n=", n_clovek, ")")),
            hjust = -0.06, size = 2.9, family = "Helvetica") +
  scale_x_continuous(labels = function(x) paste0(100 * x, " %"), limits = c(0, 1.25),
                     breaks = seq(0, 1, 0.25), expand = expansion(mult = c(0, 0))) +
  labs(x = "shoda modelu s lidským kódem", y = NULL) + theme_book_h()
save_book_fig(file.path(FIG, "kap6_shoda_kategorie.png"), p1, width = 7.5, height = 3.9)

# ── Obrázek: konfuzní matice (řádky = člověk, sloupce = model; řádkově norm.) ──
kf <- read.csv(file.path(TAB, "kap6_konfuzni_matice.csv"), encoding = "UTF-8")
ord <- pk$kategorie[order(-pk$n_clovek)]              # podle četnosti u člověka
kf$clovek <- factor(kf$clovek, levels = rev(ord))
kf$model <- factor(kf$model, levels = ord)
p2 <- ggplot(kf, aes(model, clovek, fill = podil)) +
  geom_tile(color = "white", linewidth = 0.4) +
  geom_text(aes(label = ifelse(podil < 0.005, "",
                               sub("^0", "", sprintf("%.2f", podil)))),
            size = 2.4, family = "Helvetica",
            color = ifelse(kf$podil > 0.45, "white", "black")) +
  scale_fill_gradient(low = "#EEF0F8", high = MUNI_BLUE, limits = c(0, 1),
                      name = "podíl řádku") +
  labs(x = "kód modelu", y = "kód člověka") + theme_book() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1),
        panel.grid = element_blank(), legend.position = "right")
save_book_fig(file.path(FIG, "kap6_konfuzni.png"), p2, width = 8.5, height = 5.2)

# ── Obrázek: forest reliability — α lidí (K1, 3 dimenze) + κ člověk×model ──
fr <- rbind(
  data.frame(co = "chování (α, lidé)", est = val("k1_alpha_nom_chovani"),
             lo = val("k1_alpha_ci_lo_chovani"), hi = val("k1_alpha_ci_hi_chovani"),
             skupina = "shoda mezi lidmi"),
  data.frame(co = "řešení (α, lidé)", est = val("k1_alpha_nom_reseni"),
             lo = val("k1_alpha_ci_lo_reseni"), hi = val("k1_alpha_ci_hi_reseni"),
             skupina = "shoda mezi lidmi"),
  data.frame(co = "dopad (α, lidé)", est = val("k1_alpha_nom_dopad"),
             lo = val("k1_alpha_ci_lo_dopad"), hi = val("k1_alpha_ci_hi_dopad"),
             skupina = "shoda mezi lidmi"),
  data.frame(co = "řešení (κ, člověk × model)", est = val("kappa_llm_clovek"),
             lo = val("kappa_ci_lo"), hi = val("kappa_ci_hi"),
             skupina = "člověk × model"))
fr$co <- factor(fr$co, levels = rev(fr$co))
p3 <- ggplot(fr, aes(est, co, color = skupina)) +
  geom_vline(xintercept = c(0, 0.667, 0.8), linetype = c("solid", "dashed", "dotted"),
             color = GREY_TEXT, linewidth = 0.35) +
  geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.18, linewidth = 0.7) +
  geom_point(size = 3) +
  scale_color_manual(values = c("shoda mezi lidmi" = MUNI_BLUE,
                                "člověk × model" = PED_ORANGE), name = NULL) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2),
                     labels = function(x) format(x, decimal.mark = ",")) +
  labs(x = "koeficient shody (95% CI)", y = NULL) +
  theme_book_h() + theme(legend.position = "top")
save_book_fig(file.path(FIG, "kap6_forest.png"), p3, width = 7.5, height = 3.2)

cat("OK: kap6_shoda_kategorie, kap6_konfuzni, kap6_forest →", FIG, "\n")
