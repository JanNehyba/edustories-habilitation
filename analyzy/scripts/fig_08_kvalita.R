# Figury kapitoly 8 (Studie 4): třetí anotační etapa (K3) a spojení K1 × K3.
# Hodnoty VÝHRADNĚ z manifestu kap8_kvalita_cisla.csv a odvozených tabulek
# kap8_matice_zamen.csv / kap8_reseni_dopad.csv (notebook 40_kvalita.qmd).
# Výstupy (vystupy/obrazky/): kap8_rozdeleni, kap8_matice_zamen, kap8_shoda_etapy,
# kap8_reseni_dopad {png,pdf}. Barvy: obě anotátorky = lidské (odstíny K3 modré);
# K1/K2/K3 = fixní odstíny (GRAFICKY-MANUAL); AI oranžová se zde nevyskytuje.

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
TAB <- normalizePath(file.path(SCR, "..", "..", "vystupy", "tabulky"), mustWork = FALSE)
dir.create(FIG, showWarnings = FALSE, recursive = TRUE)
man <- read.csv(file.path(TAB, "kap8_kvalita_cisla.csv"), encoding = "UTF-8")
val <- function(k) { v <- man$value[man$metric == k]; stopifnot(length(v) == 1); v }
cz <- function(x) format(x, decimal.mark = ",")
PAL_ANOT <- c(A12 = "#003366", A2 = "#99BBEE")   # dvě lidské posuzovatelky, odstíny modré

# ── Obrázek 8.1: rozdělení tří dimenzí podle anotátorky ──────────────────────
roz <- rbind(
  data.frame(dim = "Kvalita kazuistiky", kat = c("plná", "plochá"),
             A12 = c(1 - val("kvalita_plocha_podil_A12"), val("kvalita_plocha_podil_A12")),
             A2  = c(1 - val("kvalita_plocha_podil_A2"),  val("kvalita_plocha_podil_A2"))),
  data.frame(dim = "Dopad řešení", kat = c("neúspěch", "krátkodobý
úspěch", "dlouhodobý
úspěch"),
             A12 = c(val("dopad_NEU_podil_A12"), val("dopad_KU_podil_A12"), val("dopad_DU_podil_A12")),
             A2  = c(val("dopad_NEU_podil_A2"),  val("dopad_KU_podil_A2"),  val("dopad_DU_podil_A2"))),
  data.frame(dim = "Vhodnost řešení (1–4)", kat = as.character(1:4),
             A12 = sapply(1:4, function(v) val(paste0("vhodnost_", v, "_podil_A12"))),
             A2  = sapply(1:4, function(v) val(paste0("vhodnost_", v, "_podil_A2")))))
roz <- tidyr::pivot_longer(roz, c(A12, A2), names_to = "anotatorka", values_to = "podil")
roz$dim <- factor(roz$dim, levels = unique(roz$dim))
roz$kat <- factor(roz$kat, levels = unique(roz$kat))
p1 <- ggplot(roz, aes(kat, 100 * podil, fill = anotatorka)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.62) +
  facet_wrap(~dim, scales = "free_x") +
  scale_fill_manual(values = PAL_ANOT, name = NULL) +
  scale_y_continuous(labels = function(x) paste0(cz(x), " %")) +
  labs(x = NULL, y = "podíl vyplněných hodnocení") +
  theme_book() + theme(legend.position = "top", strip.text = element_text(color = "black"))
save_book_fig(file.path(FIG, "kap8_rozdeleni.png"), p1, width = 8.5, height = 3.6)

# ── Obrázek 8.2: matice záměn (dopad, vhodnost) na plném překryvu ───────────
mz <- read.csv(file.path(TAB, "kap8_matice_zamen.csv"), encoding = "UTF-8")
mz <- mz[mz$dimenze %in% c("dopad", "vhodnost"), ]
lev <- list(dopad = c("Neúspěch", "Krátkodobý úspěch", "Dlouhodobý úspěch"), vhodnost = c("1", "2", "3", "4"))
zalom <- function(x) sub(" úspěch", "
úspěch", x)
mz$A12 <- as.character(mz$A12); mz$A2 <- as.character(mz$A2)
mz <- do.call(rbind, lapply(names(lev), function(d) {
  m <- mz[mz$dimenze == d, ]
  m$A12 <- factor(zalom(m$A12), levels = rev(zalom(lev[[d]]))); m$A2 <- factor(zalom(m$A2), levels = zalom(lev[[d]]))
  m$dimenze <- ifelse(d == "dopad", "Dopad řešení", "Vhodnost řešení"); m
}))
mz$dimenze <- factor(mz$dimenze, levels = c("Dopad řešení", "Vhodnost řešení"))
p2 <- ggplot(mz, aes(A2, A12, fill = n)) +
  geom_tile(color = "white") +
  geom_text(aes(label = n, color = n > max(n) * 0.55), size = 3.4) +
  scale_color_manual(values = c(`FALSE` = "black", `TRUE` = "white"), guide = "none") +
  scale_fill_gradient(low = "#F2F5FC", high = "#003366", name = "počet") +
  facet_wrap(~dimenze, scales = "free") +
  labs(x = "anotátorka A2", y = "anotátorka A12") +
  theme_book() + theme(panel.grid.major.y = element_blank(),
                       strip.text = element_text(color = "black"))
save_book_fig(file.path(FIG, "kap8_matice_zamen.png"), p2, width = 8.5, height = 3.8)

# ── Obrázek 8.3: shoda napříč etapami (forest) ──────────────────────────────
k6 <- read.csv(file.path(TAB, "kap6_kodovani_cisla.csv"), encoding = "UTF-8")
k7 <- read.csv(file.path(TAB, "kap7_k2_shoda_cisla.csv"), encoding = "UTF-8")
v6 <- function(k) k6$value[k6$metric == k]; v7 <- function(k) k7$value[k7$metric == k]
et <- data.frame(
  label = c("K1 · dopad (α)", "K1 · typ řešení (α)",
            "K2 · vhodnost (α)", "K2 · reaktivní–proaktivní (α)",
            "K3 · kvalita (κ)", "K3 · dopad (κ)", "K3 · vhodnost (vážená κ)",
            "K1 × K3 · dopad (κ)"),
  etapa = c("K1", "K1", "K2", "K2", "K3", "K3", "K3", "K3"),
  est = c(v6("k1_alpha_nom_dopad"), v6("k1_alpha_nom_reseni"),
          v7("alpha_ord_final_vhodnost"), v7("alpha_ord_final_reaktivni"),
          val("shoda_kvalita_kappa"), val("shoda_dopad_kappa"), val("shoda_vhodnost_wkappa"),
          val("k1k3_dopad_kappa")),
  lo = c(v6("k1_alpha_ci_lo_dopad"), v6("k1_alpha_ci_lo_reseni"),
         v7("alpha_ci_lo_vhodnost"), v7("alpha_ci_lo_reaktivni"),
         val("shoda_kvalita_kappa_ci_lo"), val("shoda_dopad_kappa_ci_lo"), val("shoda_vhodnost_wkappa_ci_lo"),
         val("k1k3_dopad_kappa_ci_lo")),
  hi = c(v6("k1_alpha_ci_hi_dopad"), v6("k1_alpha_ci_hi_reseni"),
         v7("alpha_ci_hi_vhodnost"), v7("alpha_ci_hi_reaktivni"),
         val("shoda_kvalita_kappa_ci_hi"), val("shoda_dopad_kappa_ci_hi"), val("shoda_vhodnost_wkappa_ci_hi"),
         val("k1k3_dopad_kappa_ci_hi")))
et$label <- factor(et$label, levels = rev(et$label))
p3 <- ggplot(et, aes(est, label, color = etapa)) +
  geom_vline(xintercept = c(0.667, 0.8), linetype = "dashed", color = GREY_TEXT) +
  geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.18, linewidth = 0.8) +
  geom_point(size = 3) +
  scale_color_manual(values = PAL_KAMPANE, name = NULL) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2), labels = cz) +
  labs(x = "koeficient shody (95% interval spolehlivosti)", y = NULL) +
  theme_book_h() + theme(legend.position = "top")
save_book_fig(file.path(FIG, "kap8_shoda_etapy.png"), p3, width = 8, height = 4.2)

# ── Obrázek 8.4: typ řešení (K1) × podíl dlouhodobého úspěchu (K3) ─────────
rd <- read.csv(file.path(TAB, "kap8_reseni_dopad.csv"), encoding = "UTF-8")
rd <- rd[rd$n_kazuistik >= 20, ]
rd$lab <- paste0(rd$res, " (n = ", rd$n_kazuistik, ")")
rd$lab <- factor(rd$lab, levels = rd$lab[order(rd$du_podil)])
p4 <- ggplot(rd, aes(100 * du_podil, lab)) +
  geom_errorbarh(aes(xmin = 100 * du_ci_lo, xmax = 100 * du_ci_hi), height = 0.2,
                 color = GREY_LINE, linewidth = 0.8) +
  geom_point(aes(x = 100 * du_podil_k1, shape = "první etapa (2024)"),
             color = PAL_KAMPANE[["K1"]], size = 2.6, stroke = 1.1) +
  geom_point(aes(shape = "třetí etapa (2026)"), color = MUNI_BLUE, size = 3.2) +
  scale_shape_manual(values = c(`první etapa (2024)` = 1, `třetí etapa (2026)` = 16),
                     name = NULL) +
  scale_x_continuous(limits = c(0, 100), labels = function(x) paste0(cz(x), " %")) +
  labs(x = "podíl kazuistik s dlouhodobým úspěchem (interval spolehlivosti u třetí etapy)",
       y = NULL) +
  theme_book_h() + theme(legend.position = "top")
save_book_fig(file.path(FIG, "kap8_reseni_dopad.png"), p4, width = 8, height = 4.2)

cat("OK: kap8_rozdeleni + kap8_matice_zamen + kap8_shoda_etapy + kap8_reseni_dopad →", FIG, "\n")
