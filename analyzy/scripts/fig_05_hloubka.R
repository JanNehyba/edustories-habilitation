# Hloubkové figury kapitoly 5: rozdělení délek, věk, všechny kategorie K1,
# ko-výskyt chování×řešení, dopad podle typu řešení.
# Vstupy VÝHRADNĚ z vystupy/tabulky/ (CSV generované notebookem 10 + manifest).

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
suppressPackageStartupMessages(library(dplyr))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
TAB <- normalizePath(file.path(SCR, "..", "..", "vystupy", "tabulky"), mustWork = FALSE)
dir.create(FIG, showWarnings = FALSE, recursive = TRUE)

CASTI <- c(description = "popis situace", anamnesis = "anamnéza",
           solution = "řešení", outcome = "výsledek")

# ── Obrázek: rozdělení délek čtyř částí (housle + medián) ──
d <- read.csv(file.path(TAB, "kap5_delky_rozdeleni.csv"), encoding = "UTF-8")
d$cast <- factor(CASTI[d$cast], levels = unname(CASTI))
d <- d[d$slova <= quantile(d$slova, .99), ]        # ořez extrémů jen pro čitelnost
p1 <- ggplot(d, aes(cast, slova)) +
  geom_violin(fill = GREY_FILL, color = GREY_LINE, linewidth = 0.4) +
  geom_boxplot(width = 0.12, outlier.shape = NA, fill = "white",
               color = MUNI_BLUE, linewidth = 0.5) +
  scale_y_continuous(limits = c(0, NA)) +
  labs(x = NULL, y = "počet slov") + theme_book()
save_book_fig(file.path(FIG, "kap5_delky.png"), p1, width = 7.5, height = 3.6)

# ── Obrázek: rozložení věku žáků ──
v <- read.csv(file.path(TAB, "kap5_vek_rozdeleni.csv"), encoding = "UTF-8")
v <- v[v$n > 0 & v$vek >= 4 & v$vek <= 20, ]
p2 <- ggplot(v, aes(vek, n)) +
  geom_col(fill = MUNI_BLUE, width = 0.8) +
  scale_x_continuous(breaks = seq(4, 20, 2)) +
  labs(x = "věk žáka (roky)", y = "počet kazuistik") + theme_book()
save_book_fig(file.path(FIG, "kap5_vek.png"), p2, width = 7, height = 3.2)

# ── Obrázky: všechny kategorie chování a dopadů (řešení už má vlastní graf) ──
k <- read.csv(file.path(TAB, "kap5_k1_kategorie.csv"), encoding = "UTF-8")
beh <- k |> filter(dimenze == "chovani") |> arrange(pripadu)
beh$kategorie <- factor(beh$kategorie, levels = beh$kategorie)
p3 <- ggplot(beh, aes(pripadu, kategorie)) +
  geom_col(fill = MUNI_BLUE, width = 0.7) +
  geom_text(aes(label = pripadu), hjust = -0.15, size = 3, family = "Helvetica") +
  scale_x_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = "počet kazuistik s kategorií", y = NULL) + theme_book_h()
save_book_fig(file.path(FIG, "kap5_k1_chovani.png"), p3, width = 7.5, height = 4.6)

dop <- k |> filter(dimenze == "dopad") |> arrange(pripadu)
dop$kategorie <- factor(dop$kategorie, levels = dop$kategorie)
p4 <- ggplot(dop, aes(pripadu, kategorie)) +
  geom_col(fill = MUNI_BLUE, width = 0.6) +
  geom_text(aes(label = pripadu), hjust = -0.15, size = 3.2, family = "Helvetica") +
  scale_x_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = "počet kazuistik s kategorií", y = NULL) + theme_book_h()
save_book_fig(file.path(FIG, "kap5_k1_dopady.png"), p4, width = 7, height = 2.4)

# ── Obrázek: ko-výskyt P(řešení | chování) — heatmapa ──
kv <- read.csv(file.path(TAB, "kap5_kovyskyt.csv"), encoding = "UTF-8")
ZKRAT <- c("Nevěnování se výuce/Nepozornost při výuce" = "Nepozornost při výuce",
           "Neplnění školních povinností/nepřipravenost na výuku" = "Neplnění povinností",
           "Porušování třídních/školních pravidel" = "Porušování pravidel")
kv$chovani <- ifelse(kv$chovani %in% names(ZKRAT), ZKRAT[kv$chovani], kv$chovani)
ord_b <- kv |> group_by(chovani) |> summarise(n = first(n_chovani)) |> arrange(n)
ord_r <- kv |> group_by(reseni) |> summarise(s = sum(n_spolu)) |> arrange(desc(s))
kv$chovani <- factor(kv$chovani, levels = ord_b$chovani)
kv$reseni <- factor(kv$reseni, levels = ord_r$reseni)
p5 <- ggplot(kv, aes(reseni, chovani, fill = podil)) +
  geom_tile(color = "white", linewidth = 0.4) +
  geom_text(aes(label = sub("^0", "", sprintf("%.2f", podil))),
            size = 2.6, family = "Helvetica",
            color = ifelse(kv$podil > 0.45, "white", "black")) +
  scale_fill_gradient(low = "#EEF0F8", high = MUNI_BLUE, limits = c(0, NA),
                      name = "P(řešení | chování)") +
  labs(x = NULL, y = NULL) + theme_book() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1),
        panel.grid = element_blank(), legend.position = "right")
save_book_fig(file.path(FIG, "kap5_kovyskyt.png"), p5, width = 9, height = 4.6)

# ── Obrázek: podíl dlouhodobého úspěchu podle typu řešení ──
du <- read.csv(file.path(TAB, "kap5_dopad_podle_reseni.csv"), encoding = "UTF-8") |>
  arrange(podil_DU)
du$reseni <- factor(du$reseni, levels = du$reseni)
p6 <- ggplot(du, aes(podil_DU, reseni)) +
  geom_col(fill = MUNI_BLUE, width = 0.68) +
  geom_text(aes(label = paste0(sprintf("%.0f", 100 * podil_DU), " % (n=", n, ")")),
            hjust = -0.06, size = 2.9, family = "Helvetica") +
  scale_x_continuous(labels = function(x) paste0(100 * x, " %"),
                     expand = expansion(mult = c(0, 0.22))) +
  labs(x = "podíl kazuistik s dlouhodobým úspěchem", y = NULL) + theme_book_h()
save_book_fig(file.path(FIG, "kap5_dopad_reseni.png"), p6, width = 7.5, height = 3.8)

cat("OK: kap5_delky, kap5_vek, kap5_k1_chovani, kap5_k1_dopady, kap5_kovyskyt, kap5_dopad_reseni →", FIG, "\n")
