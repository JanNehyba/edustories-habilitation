# Jednotné téma a palety figur knihy — implementace kniha/GRAFICKY-MANUAL.md.
# Použití: source(file.path(dirname(sys.frame(1)$ofile), "theme_book.R"))
# nebo source("theme_book.R") při spuštění z analyzy/scripts/.
# KLÍČOVÉ PRAVIDLO: učitel/lidské = MUNI modrá, AI/LLM = PdF oranžová.

suppressPackageStartupMessages(library(ggplot2))

MUNI_BLUE  <- "#0000DC"   # učitel / lidské / základ knihy
PED_ORANGE <- "#FF7300"   # AI / LLM / generované
GREY_TEXT  <- "#666666"   # chybění, vyřazené, limity
GREY_LINE  <- "#B8B8B8"
GREY_FILL  <- "#EFEFEF"

PAL_ZDROJ <- c(
  "Učitel" = MUNI_BLUE,
  "AI"          = PED_ORANGE
)
PAL_KAMPANE <- c(K1 = "#003366", K2 = "#3366CC", K3 = "#99BBEE")

theme_book <- function(base_size = 12) {
  theme_minimal(base_size = base_size, base_family = "Helvetica") +
    theme(
      panel.grid.minor   = element_blank(),
      panel.grid.major.y = element_line(color = GREY_FILL),
      panel.grid.major.x = element_blank(),
      axis.text  = element_text(color = "black"),
      axis.title = element_text(color = "black"),
      legend.title = element_text(size = base_size - 1),
      legend.text  = element_text(size = base_size - 2),
      plot.title = element_blank(),      # nadpis nese popisek v knize
      plot.subtitle = element_blank(),
      plot.background  = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA)
    )
}

# horizontální grafy (kategorie na ose y): mřížka po x
theme_book_h <- function(base_size = 12) {
  theme_book(base_size) +
    theme(panel.grid.major.y = element_blank(),
          panel.grid.major.x = element_line(color = GREY_FILL))
}

# čtení manifestu čísel (jediný povolený zdroj hodnot figur)
read_manifest <- function(name) {
  p <- file.path(dirname(sys.frames()[[1]]$ofile %||% "."), "..", "..",
                 "vystupy", "tabulky", paste0(name, ".csv"))
  if (!file.exists(p)) p <- file.path("..", "..", "vystupy", "tabulky", paste0(name, ".csv"))
  df <- read.csv(p, encoding = "UTF-8")
  setNames(df$value, df$metric)
}
`%||%` <- function(a, b) if (is.null(a)) b else a

# uložení: PDF (vektor, sazba) + PNG 300 dpi (náhled/companion); cairo kvůli unicode
save_book_fig <- function(path_png, plot, width = 8, height = 4.5) {
  ggsave(path_png, plot, width = width, height = height, dpi = 300,
         bg = "white", type = "cairo")
  ggsave(sub("\\.png$", ".pdf", path_png), plot, width = width,
         height = height, bg = "white", device = grDevices::cairo_pdf)
  invisible(path_png)
}
