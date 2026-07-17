# Figury kapitoly 5 (Studie 1): růst korpusu + frekvence typů řešení K1.
# Hodnoty VÝHRADNĚ z manifestu kap5_korpus_cisla.csv (brána: žádná ruční čísla).
# Výstup: vystupy/obrazky/kap5_rust_korpusu.{png,pdf}, kap5_k1_reseni.{png,pdf}

SCR <- tryCatch(dirname(sys.frame(1)$ofile), error = function(e) getwd())
source(file.path(SCR, "theme_book.R"))
FIG <- normalizePath(file.path(SCR, "..", "..", "vystupy", "obrazky"), mustWork = FALSE)
dir.create(FIG, showWarnings = FALSE, recursive = TRUE)
man <- read.csv(file.path(SCR, "..", "..", "vystupy", "tabulky", "kap5_korpus_cisla.csv"),
                encoding = "UTF-8")
val <- function(k) man$value[man$metric == k]

# ── Obrázek 5.1: růst korpusu (chronologické řezy; HF výběr záměrně mimo) ──
rust <- data.frame(
  rez = factor(c("2023", "duben 2024", "srpen 2024", "květen 2026"),
               levels = c("2023", "duben 2024", "srpen 2024", "květen 2026")),
  n = c(val("rust_S12023"), val("rust_S3042024"),
        val("rust_S4082024"), val("rust_S6052026"))
)
p1 <- ggplot(rust, aes(rez, n)) +
  geom_col(fill = MUNI_BLUE, width = 0.62) +
  geom_text(aes(label = format(n, big.mark = " ")),
            vjust = -0.45, size = 3.4, family = "Helvetica") +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12)),
                     labels = function(x) format(x, big.mark = " ")) +
  labs(x = NULL, y = "počet kazuistik v řezu") +
  theme_book()
save_book_fig(file.path(FIG, "kap5_rust_korpusu.png"), p1, width = 7, height = 3.8)

# ── Obrázek 5.2: typy řešení K1 (počet kazuistik s kategorií, top 8) ──
res <- man[grepl("^k1_reseni_pripadu:", man$metric), ]
res$kategorie <- sub("^k1_reseni_pripadu:", "", res$metric)
res <- res[order(res$value), ]
res <- tail(res, 8)
res$kategorie <- factor(res$kategorie, levels = res$kategorie)
p2 <- ggplot(res, aes(value, kategorie)) +
  geom_col(fill = MUNI_BLUE, width = 0.68) +
  geom_text(aes(label = format(value, big.mark = " ")),
            hjust = -0.15, size = 3.2, family = "Helvetica") +
  scale_x_continuous(expand = expansion(mult = c(0, 0.14))) +
  labs(x = "počet kazuistik s kategorií", y = NULL) +
  theme_book_h()
save_book_fig(file.path(FIG, "kap5_k1_reseni.png"), p2, width = 7.5, height = 3.6)

cat("OK: kap5_rust_korpusu + kap5_k1_reseni →", FIG, "\n")
